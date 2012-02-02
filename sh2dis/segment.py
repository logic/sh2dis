#!/usr/bin/env python


from __future__ import print_function


import bisect
import textwrap


class SegmentError(Exception):
    pass


class SegmentData(object):
    """Metaclass for segment data types."""
    def __init__(self, location, width, model, comment=None,
                 unknown_prefix='unk', extra=None, member_of=None):
        object.__init__(self)
        self.location = location  # Our absolute memory location.
        self.width = width        # The size of the data type in bytes.
        self.model = model        # The memeory model we're a part of.
        self.comment = comment    # A comment for this location.
        self.extra = extra
        self.unknown_prefix = unknown_prefix
        self.member_of = member_of

    def __str__(self):
        if self.member_of is not None:
            if self.member_of.members[0] == self:
                return self.member_of.__str__()
            return ''

        instruction = self.get_instruction()

        label = self.model.get_label(self.location)
        if label is None or '+' in label:
            label = ''
        else:
            label += ':'

        # Ask children if they have any custom comments.
        comments = self.generate_comments()

        # Ask the model if it has any comments for us.
        comments.extend(self.model.generate_comments(self.location))

        val = []
        if len(comments) > 0:
            if len(instruction) > 21:
                val.append('%08X %-16s %s' % (self.location, label,
                                              instruction))
            else:
                c = comments.pop(0)
                val.append('%08X %-16s %-21s ! %s' % (self.location, label,
                                                      instruction, c))
            for c in comments:
                val.append('%47s ! %s' % ('', c))
        else:
            val.append('%08X %-16s %s' % (self.location, label, instruction))

        return '\n'.join(val)

    def generate_comments(self):
        if self.comment is not None:
            return self.comment.split('\n')
        return []

    def get_label(self):
        return None


class CompositeData(SegmentData):
    """Collection of segment data."""
    def __init__(self, members=None, items_per_line=1, model=None,
                 comment=None, extra=None):
        self.members = members if members is not None else []
        self.items_per_line = items_per_line
        self.model = model
        self.comment = comment
        self.extra = extra

    def __str__(self):
        val = []
        label = None
        per_line = 1
        for member in self.members:
            if per_line == 1:
                if label is None:
                    label = self.model.get_label(member.location)
                    if label is None or '+' in label:
                        label = ''
                    else:
                        label += ':'
                else:
                    label = ''
                val.append('%08X %-16s ' % (member.location, label))
                val.append(member.get_instruction(no_cmd=False))
            else:
                val.append(member.get_instruction(no_cmd=True))
            val.append(', ')
            per_line += 1
            if per_line > self.items_per_line:
                val[-1] = '\n'
                per_line = 1
        if len(val) and val[-1] == '\n':
            val.pop()
        return ''.join(val)


class Segment(object):

    VALUE = 0
    XREFS = 1
    LABEL = 2

    def __init__(self, start, end, phys=None, name=None, model=None):
        object.__init__(self)
        self.start = start
        self.end = end
        self.phys = phys
        self.name = name
        self.model = model
        # Initialize to a list of [value, references, label].
        self.space = [ [None, [], None] for _ in range(end-start)]

    def get_phys(self, location, width=1):
        if self.phys is None:
            return chr(0)
        relative_location = location - self.start
        return self.phys[relative_location:(relative_location + width)]

    def get_location(self, location):
        relative_location = location - self.start
        meta = self.space[relative_location][self.VALUE]
        if type(meta) is int:
            meta = self.space[relative_location + meta][self.VALUE]
        return meta

    def set_location(self, value):
        comments = []
        rel_loc = value.location - self.start
        rel_end = rel_loc + value.width
        for i in range(rel_loc, rel_loc + value.width):
            meta = self.space[i][self.VALUE]
            if meta is not None:
                if i + meta.width <= rel_end:
                    if meta.comment is not None:
                        comments.append(meta.comment)
                    for j in self.space[meta.location-self.start][self.XREFS]:
                        self.model.add_reference(value.location, j)
                    self.unset_location(meta.location)
                else:
                    raise SegmentError('conflict with data at %#x' % i)
        if len(comments) > 0:
            if value.comment is not None:
                comments.insert(0, value.comment)
            value.comment = '\n'.join(comments)
        self.space[rel_loc][self.VALUE] = value
        for i in range(1, value.width):
            self.space[rel_loc + i][self.VALUE] = -i

    def unset_location(self, location):
        meta = self.get_location(location)
        if meta is not None:
            rel_loc = location - self.start
            for i in range(rel_loc, rel_loc + meta.width):
                self.space[i][self.VALUE] = None

    def get_label(self, location):
        meta = self.get_location(location)
        if meta is None and (location - self.start) > 0:
            meta = self.get_location(location - 1)
        if meta is None:
            new_location = location
            unknown_prefix = 'unk'
        else:
            new_location = meta.location
            unknown_prefix = meta.unknown_prefix
        label = self.space[new_location-self.start][self.LABEL]
        if (len(self.space[new_location - self.start][self.XREFS]) > 0 and
            label is None):
            label = '%s_%X' % (unknown_prefix, new_location)
        if new_location < location and label is not None:
            label = '%s+%d' % (label, location-new_location)
        return label

    def set_label(self, location, label):
        self.space[location-self.start][self.LABEL] = label

    def generate_comments(self, location):
        """ Generate cross-reference comments. """
        references = self.space[location-self.start][self.XREFS]
        if len(references):
            count = 0
            max_xrefs = 6
            xrefs = ['XREF: ']
            for r in references:
                l = self.model.get_label(r) or '0x%X' % r
                xrefs.append(l)
                count += 1
                if count == max_xrefs:
                    if len(references) > max_xrefs:
                        xrefs.append('...')
                    break
                if count != len(references):
                    xrefs.append(', ')
            return textwrap.wrap(''.join(xrefs), 29)
        return []

    def add_reference(self, location, reference):
        """Track references in numerically sorted order."""
        if reference == location:
            return
        references = self.space[location-self.start][self.XREFS]
        bl = bisect.bisect_left(references, reference)
        if bl == len(references) or references[bl] != reference:
            references.insert(bl, reference)

    def get_references(self, location):
        """Return a list of all references to a given location."""
        return list(self.space[location-self.start][self.XREFS])

    def remove_reference(self, location, reference):
        references = self.space[location-self.start][self.XREFS]
        bl = bisect.bisect_left(references, reference)
        if bl != len(references) and references[bl] == reference:
            references.pop(bl)


class MemoryModel(object):
    def __init__(self, segments):
        object.__init__(self)
        self.segments = []
        for name, start, end, phys in segments:
            self.segments.append(Segment(name=name, start=start, end=end,
                                         phys=phys, model=self))

    def __lookup_segment(self, location):
        for segment in self.segments:
            if location >= segment.start and location < segment.end:
                return segment
        raise SegmentError('invalid segment address: %#x' % location)

    def get_phys(self, location, width=1):
        seg = self.__lookup_segment(location)
        if seg.phys is None:
            raise SegmentError('%#x is not a physical location' % location)
        return seg.get_phys(location, width)

    def get_phys_ranges(self):
        ranges = []
        for segment in self.segments:
            if segment.phys is not None:
                ranges.append((segment.start, segment.end))
        return ranges

    def get_segment_name(self, location):
        return self.__lookup_segment(location).name

    def get_location(self, location):
        return self.__lookup_segment(location).get_location(location)

    def set_location(self, value):
        self.__lookup_segment(value.location).set_location(value)

    def unset_location(self, location):
        self.__lookup_segment(location).unset_location(location)

    def get_label(self, location):
        return self.__lookup_segment(location).get_label(location)

    def set_label(self, location, label):
        self.__lookup_segment(location).set_label(location, label)

    def generate_comments(self, location):
        return self.__lookup_segment(location).generate_comments(location)

    def get_references(self, location):
        return self.__lookup_segment(location).get_references(location)

    def add_reference(self, location, reference):
        self.__lookup_segment(location).add_reference(location, reference)

    def remove_reference(self, location, reference):
        self.__lookup_segment(location).remove_reference(location, reference)

    def location_isset(self, location):
        try:
            ref = self.__lookup_segment(location).get_location(location)
            return ref is not None
        except SegmentError:
            return False


if __name__ == '__main__':
    print('no tests yet')
