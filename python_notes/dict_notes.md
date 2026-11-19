# Dict notes

Each dict key MUST be **HASHABLE/immutable**.

```python
dict.get(char,0) # avoid ```KeyError```
```

```python
freq_map = Counter(char) # count all elements
```

```python
key_to_words.setdefault(sorted_s, []) # if key doesn't exist - set [] value, else return existing value
```

```python
test_dict = defaultdict(list) # or simply create defeaultdict, automatically sets [] /no extra check
```
