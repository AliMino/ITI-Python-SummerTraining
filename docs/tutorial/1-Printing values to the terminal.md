# Python Training - Tutorial - Printing values to the terminal

- [Python Training - Tutorial - Printing values to the terminal](#python-training---tutorial---printing-values-to-the-terminal)
  - [Printing values to the terminal](#printing-values-to-the-terminal)
    - [Modifying values separator](#modifying-values-separator)
    - [Modifying the end of the line](#modifying-the-end-of-the-line)

## Printing values to the terminal

[Go to code](../../tutorial/1-hello-world.py#L2)

```python
# printing strings
print('something to be printed')
# Output: something to be printed

# printing numbers
print(123)
# Output: 123

# printing multiple values
print('My name is', 'Ali')
```

---

### Modifying values separator

[Go to code](../../tutorial/1-hello-world.py#L16)

By default, the `print()` function prints a single whitespace as a separator between values, you can override the separator as following...

```python
# 'Python' '3.6' -> 'Python:3.6'
print('Python', '3.6', sep=':')
```

---

### Modifying the end of the line

[Go to code](../../tutorial/1-hello-world.py#L33)

By default, the `print()` function inserts a new line after the passed value(s). To override this behavior; pass the `end` parameter to the `print()` function: print('something', end=''). The following example prints the phrase 'Hi there' then insert two new lines

```python
print('Hi there', end='\n\n')
```

<span style="text-align:center">

<hr style="width:70%">

[Top](#python-training---tutorial---printing-values-to-the-terminal) &emsp; | &emsp; [Home](../README.md) &emsp; • &emsp; [Tutorials](index.md) &emsp; • &emsp; [Summary](../summary.md)

[Coming Next: Reading values from the user](./2-Reading%20values%20from%20the%20user.md)

</span>
