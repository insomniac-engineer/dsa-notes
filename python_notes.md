# Python notes

## Dict

Get value from dict without ```KeyError```:

```python
dict.get(char,0)
```

Create dict with character counts (from list):

```python
freq_map = Counter(char)
```

Returns reference to the value stored under that key:

```python
key_to_words.setdefault(sorted_s, [])
```

## String

Python strings do not have a built-in method that returns a sorted string.
sorted() returns a list.

```python
sorted_string = "".join(sorted(s))
```
