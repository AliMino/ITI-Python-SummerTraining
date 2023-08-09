# Python Training

- [Python Training](#python-training)
  - [Installing Python](#installing-python)
  - [Tutorial](#tutorial)
    - [Printing values to the terminal](#printing-values-to-the-terminal)
      - [Modifying values separator](#modifying-values-separator)
      - [Modifying the end of the line](#modifying-the-end-of-the-line)
    - [Read values from the user](#read-values-from-the-user)
    - [Data types](#data-types)
      - [Type Casting](#type-casting)
    - [Basic Arithmetic](#basic-arithmetic)
      - [Operators' Precedence](#operators-precedence)
    - [Working with variables](#working-with-variables)
      - [Examples for valid variable names](#examples-for-valid-variable-names)
      - [Examples for invalid variable names](#examples-for-invalid-variable-names)
    - [Manipulating strings](#manipulating-strings)
      - [String indexing](#string-indexing)
      - [String Slicing](#string-slicing)
        - [Using stride](#using-stride)
      - [Querying string length](#querying-string-length)
      - [Usefull string methods](#usefull-string-methods)
      - [Formatting strings](#formatting-strings)
      - [Here document](#here-document)
  - [Glossary](#glossary)
  - [Appendix](#appendix)
    - [Special Characters](#special-characters)
    - [Static vs. Dynamic Typing](#static-vs-dynamic-typing)

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

### Read values from the user

[Go to code](tutorial/2-prompt-the-user.py)

The `input()` function prompts the user to enter a value.

```python
print('Hello', input('What is your name?'))
```

---

### Data types

[Go to code](tutorial/3-querying-for-types.py)

|             Data Type | Name in Python | Description                                              | Examples            |
| --------------------: | :------------: | :------------------------------------------------------- | :------------------ |
|                String |      str       | A sequence of characters surrounded by either `'` or `"` | 'abc', '123', "456" |
|               Integer |      int       | A whole number                                           | -3, 0, 100, 1e-3    |
| Floating-point Number |     float      | A real number; has a decimal point `.`                   | 3.1, -6.4, 0.0      |

`... more are coming soon`

To query for a type of an arbitrary value, use `type(value)`:

```python
print(type(''))
print(type(1))
print(type(1.0))
```

#### Type Casting

Type casting is a builtin function in most programming languages that offers an implicit conversion of types.

To cast something to a string

```python
str(1)
str(1.5)
```

To cast something to an integer

```python
int('123') + 5
int('-7')
```

Note: You could add numbers using the `+` sign, however, the `+` sign concatenates (join) strings. You cannot add numbers to strings, you will have to cast either of them.

```python
'1' + '2' # will result in '12'
1 + 2     # will result in 3
```

---

### Basic Arithmetic

Basic arithmetic is done in python using operators

- Summation: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Power: `**`
- Modulo: `%`

#### Operators' Precedence

The arithemtic operators are evaluated in the following order

- `()`.
- `**`.
- `*`, `/` & `%`, from left to right.
- `+` & `-`, from left to right.

---

### Working with variables

The name of a variable consists of one or more english character (a-z, A-Z) or an underscore `_` followed by zero or more english characters, underscores `_`, or numbers.

#### Examples for valid variable names

- name
- age
- python_version
- now
- value1
- value2
- value_2
- \_val_
- _
- _1
- _2

#### Examples for invalid variable names

- python version
- 1value
- va!lue
- vaيlue
- va💡lue

---

### Manipulating strings

#### String indexing

Retrieving a single character from a string.

```python
print('Hello'[0])
print('Hello'[1])
print('Hello'[-1])
print('Hello'[-2])
```

#### String Slicing

Retrieving a substring from a string.

```python
print('Hello'[0:])
print('Hello'[1:])
print('Hello'[:-2])
```

##### Using stride

```python
print('123456789'[::2])
print('123456789'[1::2])
```

#### Querying string length

```python
print(len('Hello'))
```

#### Usefull string methods

- lower()
- upper()
- split()

#### Formatting strings

- format()
- f-strings.

#### Here document

---

---

## Glossary

| Term | Definition | Example |
| :--- | :--------- | :------ |

## Appendix

### Special Characters

Spcecial characters are a set of well-known characters preceeded by a backslash `\`.[^spec-chars]

- `\n`: new line.
- `\t`: horizontal tab.
- `\r`: go to the beginning of the current line.
- `\b`: backspace.

Note: to print a special character as it appears; prefix it with a backslash `\`: to print `\n` type `\\n`, and so on.

---

### Static vs. Dynamic Typing

Static typing means that the type of a variable can't be changed after declaration, while in dynamic typed laguages you can change the type of a variable after declaration. Python is dynamically typed language.

```python
value = 5

value = 'Five'
```

[^spec-chars]: https://en.wikipedia.org/wiki/List_of_Unicode_characters#Control_codes

<span style="text-align:center">

<hr style="width:70%">

[Top](#python-training)

</span>
