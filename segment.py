#!/usr/bin/env python


class SegmentError(StandardError):
    pass


class SegmentData:
    """Metaclass for segment data types."""
    def __init__(self, location, width, model, label=None, comment=None, references=None, extra=None):
        if references is None:
            references = [ ]
        self.location = location     # Our absolute memory location.
        self.width = width           # The size of the data type in bytes.
        self.model = model           # The memeory model we're a part of.
        self.label = label           # A string label for this location.
        self.comment = comment       # A comment for this location.
        self.references = references # A list of references to this location.
        self.extra = extra

    def __str__(self):
        instruction = self.get_instruction()

        label = self.get_label()
        if label is None:
            label = ''
        else:
            label += ':'

        comments = self.generate_comments()
        count = 1
        for r in sorted(self.references):
            if r == self.location:
                continue
            l = None
            meta = self.model.get_location(r)
            if meta is not None:
                l = meta.get_label()
            if l is None:
                l = '0x%X' % r
            if count > 0:
                comments.append('XREF: %s' % l)
                count -= 1
            else:
                comments.append('XREF: %s ...' % l)
                break
        if self.comment is not None:
            comments.append(self.comment.split('\n'))

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


class Segment:
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
        references = { }
        rel_loc = value.location - self.start
        rel_end = rel_loc + value.width
        for i in range(rel_loc, rel_loc + value.width):
            meta = self.space[i]
            if meta is not None:
                if i + meta.width <= rel_end:
                    if meta.comment is not None:
                        comments.append(meta.comment)
                    for j in meta.references:
                        references[i+self.start] = 1
                    self.unset_location(meta.location)
                else:
                    raise SegmentError, 'conflict with data at %#x' % i
        if len(comments) > 0:
            if value.comment is not None:
                comments.insert(0, value.comment)
            value.comment = ''.join(comments)
        for i in references.keys():
            if i not in value.references:
                value.references.append(i)
        self.space[rel_loc] = value
        for i in range(1, value.width):
            self.space[rel_loc + i] = -i

    def unset_location(self, location):
        meta = self.get_location(location)
        if meta is not None:
            rel_loc = location - self.start
            for i in range(rel_loc, rel_loc + meta.width):
                self.space[i] = None


class MemoryModel:
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

    def get_segment_name(self, location):
        return self.__lookup_segment(location).name

    def get_location(self, location):
        return self.__lookup_segment(location).get_location(location)

    def set_location(self, value):
        self.__lookup_segment(value.location).set_location(value)

    def unset_location(self, location):
        self.__lookup_segment(location).unset_location(location)


if __name__ == '__main__':
    print 'no tests yet'
