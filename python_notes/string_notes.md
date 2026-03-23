# String notes

---

## Immutable strings

Strings are immutable.
Any operation like `replace()` returns a new string.

```python
s = "hello world"
new_s = s.replace(" ", "-")

print(s)      # hello world
print(new_s)  # hello-world
```

## Escape sequences

A backslash starts an escape sequence.
Use `repr()` or a raw string if needed.

```python
s = "C:\new\test"
print(s)
print(repr(s))
```

## strip()

`strip(chars)` does not remove an exact substring.
It removes any matching characters from both ends.

```python
s = "  hello world  "
print(s.strip("hd "))
# ello worl
```

## split()

`split()` keeps empty items between separators.

```python
s = "a,,b,c"
print(s.split(","))
# ['a', '', 'b', 'c']
```

## join()

`join()` inserts a separator between items in an iterable.

```python
s = "hello"
print("-".join(s))
# h-e-l-l-o
```

## Slicing

General form:

```python
s[start:stop:step]
```

Reverse a string:

```python
s[::-1]
```

## Sorting characters

Strings do not have a built-in method that returns a sorted string.
`sorted()` returns a list, so combine it with `join()`.

```python
s = "dcab"
sorted_string = "".join(sorted(s))
print(sorted_string)
# abcd
```
