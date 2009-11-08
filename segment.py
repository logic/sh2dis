#!/usr/bin/env python


class SegmentError(StandardError):
    pass


class SegmentData(object):
    """Metaclass for segment data types."""
    def __init__(self, location, width, model, label=None, comment=None, references=None, unknown_prefix='unk', extra=None):
        if references is None:
            references = { }
        self.location = location     # Our absolute memory location.
        self.width = width           # The size of the data type in bytes.
        self.model = model           # The memeory model we're a part of.
        self.label = label           # A string label for this location.
        self.comment = comment       # A comment for this location.
        self.references = references # A list of references to this location.
        self.extra = extra
        self.unknown_prefix = unknown_prefix

    def __str__(self):
        instruction = self.get_instruction()

        label = self.model.get_label(self.location)
        if label is None or '+' in label:
            label = ''
        else:
            label += ':'

        comments = self.generate_comments()
        count = 1
        for r in sorted(self.references.keys()):
            if r == self.location:
                continue
            l = self.model.get_label(r)
            if l is None:
                l = '0x%X' % r
            if count > 0:
                comments.append('XREF: %s' % l)
                count -= 1
            else:
                comments.append('XREF: %s ...' % l)
                break
        if self.comment is not None:
            comments.extend(self.comment.split('\n'))

        val = [ ]
        if len(comments) > 0:
            if len(instruction) > 21:
                val.append('%08X %-16s %s' % (self.location, label, instruction))
            else:
                c = comments.pop(0)
                val.append('%08X %-16s %-21s ! %s' % (self.location, label, instruction, c))
            for c in comments:
                val.append('%47s ! %s' % ('', c))
        else:
            val.append('%08X %-16s %s' % (self.location, label, instruction))

        return '\n'.join(val)

    def generate_comments(self):
        return [ ]

    def get_label(self):
        return None


class Segment(object):
    def __init__(self, start, length, phys=None, name=None):
        self.start = start
        self.length = length
        self.phys = phys
        self.name = name
        self.space = [None] * self.length

    def __get_relative_location(self, location):
        relative_location = location - self.start
        if relative_location < 0 or relative_location > self.length:
            raise SegmentError, 'invalid segment location: %#x' % location
        return self.space[relative_location]

    def get_phys(self, location, width=1):
        if self.phys is None:
            return chr(0)
        relative_location = location - self.start
        if relative_location + width > len(self.phys):
            raise SegmentError, 'requested width exceeds segment size'
        return self.phys[relative_location:relative_location+width]

    def get_location(self, location):
        meta = self.__get_relative_location(location)
        if type(meta) is int:
            return self.get_location(location+meta)
        return meta

    def set_location(self, value):
        comments = [ ]
        rel_loc = value.location - self.start
        rel_end = rel_loc + value.width
        for i in range(rel_loc, rel_loc + value.width):
            meta = self.space[i]
            if meta is not None:
                if i + meta.width <= rel_end:
                    if meta.comment is not None:
                        comments.append(meta.comment)
                    for j in meta.references.keys():
                        value.references[j] = 1
                    self.unset_location(meta.location)
                else:
                    raise SegmentError, 'conflict with data at %#x' % i
        if len(comments) > 0:
            if value.comment is not None:
                comments.insert(0, value.comment)
            value.comment = '\n'.join(comments)
        self.space[rel_loc] = value
        for i in range(1, value.width):
            self.space[rel_loc + i] = -i

    def unset_location(self, location):
        meta = self.get_location(location)
        if meta is not None:
            rel_loc = location - self.start
            for i in range(rel_loc, rel_loc + meta.width):
                self.space[i] = None

    def get_label(self, location):
        label = None
        meta = self.get_location(location)
        if meta is None and location-self.start > 0:
            meta = self.get_location(location - 1)
        if meta is not None:
            label = meta.label
            if len(meta.references) > 0 and label is None:
                label = '%s_%X' % (meta.unknown_prefix, meta.location)
            if meta.location < location and label is not None:
                label = '%s+%d' % (label, location-meta.location)
        return label


class MemoryModel(object):
    def __init__(self, segments):
        self.segments = [ ]
        for name, start, len, phys in segments:
            self.segments.append(Segment(name=name, start=start, length=len, phys=phys))

    def __lookup_segment(self, location):
        if not isinstance(location, (int, long)):
            raise SyntaxError, 'invalid location: %s' % repr(location)
        for segment in self.segments:
            if location >= segment.start and location < segment.start + segment.length:
                return segment
        raise SegmentError, 'invalid segment address: %#x' % location

    def get_phys(self, location, width=1):
        seg = self.__lookup_segment(location)
        if seg.phys is None:
            raise SegmentError, '%#x is not a physical location' % location
        return seg.get_phys(location, width)

    def get_phys_ranges(self):
        ranges = [ ]
        for segment in self.segments:
            if segment.phys is not None:
                 ranges.append((segment.start, segment.length))
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


if __name__ == '__main__':
    print 'no tests yet'
