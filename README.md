# Python Training

- [Python Training](#python-training)
  - [Installing Python](#installing-python)
  - [Tutorial](#tutorial)
    - [Printing values to the terminal](#printing-values-to-the-terminal)
      - [Modifying values separator](#modifying-values-separator)
      - [Modifying the end of the line](#modifying-the-end-of-the-line)
  - [Glossary](#glossary)
  - [Appendix](#appendix)
    - [Special Characters](#special-characters)

## Installing Python

To install Python on Windows, Visit [Python Releases for Windows](https://www.python.org/downloads/windows/) and choose the desired version of Python.

To install Python on macOS, Visit [Python Releases for macOS](https://www.python.org/downloads/macos/) and choose your installer.

Python is preinstalled on almost every Linux system. However, it's more favorable to use [Python's Docker container](https://hub.docker.com/_/python).

---

## Tutorial

### Printing values to the terminal

[Go to code](tutorial/1-hello-world.py)

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

#### Modifying values separator

```python
# 'Python' '3.6' -> 'Python:3.6'
print('Python', '3.6', sep=':')
```

#### Modifying the end of the line

By default, the `print()` function inserts a new line after the passed value(s). To override this behavior; pass the `end` parameter to the `print()` function: print('something', end='').

---

---

## Glossary

| Term   | Definition                                               | Example             |
| :----- | :------------------------------------------------------- | :------------------ |
| String | A sequence of characters surrounded by either `'` or `"` | 'abc', '123', "456" |

## Appendix

### Special Characters

Spcecial characters are a set of well-known characters preceeded by a backslash `\`.[^spec-chars]

- `\n`: new line.
- `\t`: horizontal tab.
- `\r`: go to the beginning of the current line.
- `\b`: backspace.

Note: to print a special character as it appears; prefix it with a backslash `\`: to print `\n` type `\\n`, and so on.

[^spec-chars]: https://en.wikipedia.org/wiki/List_of_Unicode_characters#Control_codes

<span style="text-align:center">

<hr style="width:70%">

[Top](#python-training)

</span>
