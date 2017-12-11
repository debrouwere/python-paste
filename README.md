# Paste

```python3
>>> records = [('k1', 'v1'), ('k2', 'v2')]
>>> paste(records, '=;')
'k1=v1;k2=v2'
>>> paste(records, (' is ', ' and '))
'k1 is v1 and k2 is v2'
>>> paste({'first': 'Lee', 'last': 'Konitz'}.items(), ':+')
'first:Lee+last:Konitz'
>>> cut('k1=v1;k2=v2', ';=')
[['k1', 'v1'], ['k2', 'v2']]
```

`paste` concatenates smaller units first, then larger ones, whereas
`cut` works in reverse and splits bigger units first, then smaller ones.

```python3
>>> records = [('k1', 'v1'), ('k2', 'v2')]
>>> paste(records, '=;')
'k1=v1;k2=v2'
>>> cut('k1=v1;k2=v2', ';=')
[['k1', 'v1'], ['k2', 'v2']]
```

If you prefer, `recut` accepts delimiters ordered from smaller to larger
units like `paste`, which feels less natural but makes these functions
the exact inverse of each other.

```python3
>>> records = [['k1', 'v1'], ['k2', 'v2']]
>>> recut(paste(records, '=;'), '=;')
[['k1', 'v1'], ['k2', 'v2']]
>>> cut(paste(records, '=;'), ';=')
[['k1', 'v1'], ['k2', 'v2']]
```
