# Python Training - Appendix A: Arithmetic operators usage with different data types

- [Python Training - Appendix A: Arithmetic operators usage with different data types](#python-training---appendix-a-arithmetic-operators-usage-with-different-data-types)
  - [The + Operator (Summation)](#the--operator-summation)
  - [The - Operator (Subtraction)](#the---operator-subtraction)
  - [The \* Operator (Multiplication)](#the--operator-multiplication)
  - [The / Operator (Division)](#the--operator-division)
  - [The \*\* Operator (Exponent)](#the--operator-exponent)
  - [The % Operator (Modulo)](#the--operator-modulo)

## The + Operator (Summation)

| rhs \ lhs     | Integer (lhs)                                                   | Float (lhs)                                                       | String (lhs)                                  |
| ------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------- |
| Integer (rhs) | Integer (the summation of the two numbers)                      | Float (the summation of the two numbers)                          | *TypeError*: must be str, not int             |
| Float (rhs)   | Float (the summation of the two numbers)                        | Float (the summation of the two numbers)                          | *TypeError*: must be str, not float           |
| String (rhs)  | *TypeError*: unsupported operand type(s) for +: 'int' and 'str' | *TypeError*: unsupported operand type(s) for +: 'float' and 'str' | String (the concatination of the two strings) |

---

## The - Operator (Subtraction)

| rhs \ lhs     | Integer (lhs)                                                   | Float (lhs)                                                       | String (lhs)                                                    |
| ------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------- |
| Integer (rhs) | Integer (the difference between the two numbers)                | Float (the difference between the two numbers)                    | TypeError: unsupported operand type(s) for -: 'str' and 'int'   |
| Float (rhs)   | Float (the difference between the two numbers)                  | Float (the difference between the two numbers)                    | TypeError: unsupported operand type(s) for -: 'str' and 'float' |
| String (rhs)  | *TypeError*: unsupported operand type(s) for -: 'int' and 'str' | *TypeError*: unsupported operand type(s) for -: 'float' and 'str' | *TypeError*: unsupported operand type(s) for -: 'str' and 'str' |

---

## The * Operator (Multiplication)

| rhs \ lhs     | Integer (lhs)                        | Float (lhs)                                                     | String (lhs)                                                    |
| ------------- | ------------------------------------ | --------------------------------------------------------------- | --------------------------------------------------------------- |
| Integer (rhs) | Integer (The product of the numbers) | Float (The product of the numbers)                              | String (The string repeated n times)                            |
| Float (rhs)   | Float (The product of the numbers)   | Float (The product of the numbers)                              | *TypeError*: can't multiply sequence by non-int of type 'float' |
| String (rhs)  | String (The string repeated n times) | *TypeError*: can't multiply sequence by non-int of type 'float' | *TypeError*: can't multiply sequence by non-int of type 'str'   |

---

## The / Operator (Division)

| rhs \ lhs     | Integer (lhs)                                                   | Float (lhs)                                                       | String (lhs)                                                      |
| ------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| Integer (rhs) | Float (The division result)                                     | Float (The division result)                                       | *TypeError*: unsupported operand type(s) for /: 'str' and 'int'   |
| Float (rhs)   | Float (The division result)                                     | Float (The division result)                                       | *TypeError*: unsupported operand type(s) for /: 'str' and 'float' |
| String (rhs)  | *TypeError*: unsupported operand type(s) for /: 'int' and 'str' | *TypeError*: unsupported operand type(s) for /: 'float' and 'str' | *TypeError*: unsupported operand type(s) for /: 'str' and 'str'   |

---

## The ** Operator (Exponent)

| rhs \ lhs     | Integer (lhs)                                                             | Float (lhs)                                                                 | String (lhs)                                                                |
| ------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Integer (rhs) | Integer (The exponent result)                                             | Float (The exponent result)                                                 | *TypeError*: unsupported operand type(s) for ** or pow(): 'str' and 'int'   |
| Float (rhs)   | Float (The exponent result)                                               | Float (The exponent result)                                                 | *TypeError*: unsupported operand type(s) for ** or pow(): 'str' and 'float' |
| String (rhs)  | *TypeError*: unsupported operand type(s) for ** or pow(): 'int' and 'str' | *TypeError*: unsupported operand type(s) for ** or pow(): 'float' and 'str' | *TypeError*: unsupported operand type(s) for ** or pow(): 'str' and 'str'   |

---

## The % Operator (Modulo)

| rhs \ lhs     | Integer (lhs)                                                   | Float (lhs)                                                       | String (lhs)                                                      |
| ------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| Integer (rhs) | Integer (The division remainder)                                | Float (The division remainder)                                    | *TypeError*: not all arguments converted during string formatting |
| Float (rhs)   | Float (The division remainder)                                  | Float (The division remainder)                                    | *TypeError*: not all arguments converted during string formatting |
| String (rhs)  | *TypeError*: unsupported operand type(s) for %: 'int' and 'str' | *TypeError*: unsupported operand type(s) for %: 'float' and 'str' | *TypeError*: not all arguments converted during string formatting |

<span style="text-align:center">

<hr style="width:70%">

[Top](#python-training---appendix-a-arithmetic-operators-usage-with-different-data-types) &emsp; | &emsp; [Home](../README.md) &emsp; • &emsp; [Summary](../summary.md)

[Coming Next: Appendix B: Special Characters](appendix-b-special-characters.md)

</span>
