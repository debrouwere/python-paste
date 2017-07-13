def kv(obj):
    if isinstance(obj, dict):
        return obj.items()
    else:
        return obj

# a supercharged `join` function, analogous to `paste` in the R language
def paste(rows, delimiters, serialize=str):
    delimiter = delimiters[-1]
    delimiters = delimiters[:-1]

    if len(delimiters):
        return paste([paste(row, delimiters, serialize) for row in kv(rows)], (delimiter,), serialize)
    else:
        return delimiter.join(map(serialize, rows))


# a supercharged `split` function, the inverse of `paste`
def cut(s, delimiters):
    delimiter = delimiters[-1]
    delimiters = delimiters[:-1]

    if len(delimiters):
        return [cut(ss, *delimiters) for ss in cut(s, delimiter)]
    else:
        return s.split(delimiter)
