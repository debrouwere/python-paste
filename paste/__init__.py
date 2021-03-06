import re


def kv(obj):
    if isinstance(obj, dict):
        return obj.items()
    else:
        return obj

# a supercharged `join` function, analogous to `paste` in the R language
# specify delimiters from inner to outer
def paste(rows, delimiters, serialize=str):
    delimiter = delimiters[-1]
    delimiters = delimiters[:-1]

    if len(delimiters):
        return paste([paste(row, delimiters, serialize) for row in kv(rows)], (delimiter,), serialize)
    else:
        return delimiter.join(map(serialize, rows))


# a supercharged `split` function, the inverse of `paste`;
# specify delimiters from outer to inner
def cut(s, delimiters, **kwargs):
    delimiter = delimiters[0]
    delimiters = delimiters[1:]

    segments = re.split(delimiter, s, **kwargs)

    if len(delimiters):
        return [cut(segment, delimiters) for segment in segments]
    else:
        return segments


# a supercharged `split` function, the inverse of `paste`
# specify delimiters from inner to outer
def recut(s, delimiters, **kwargs):
    return cut(s, delimiters[::-1], **kwargs)
