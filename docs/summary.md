# Python Training - Summary

- [Python Training - Summary](#python-training---summary)
  - [How do arithmetic operators operate on different data types](#how-do-arithmetic-operators-operate-on-different-data-types)
    - [The + operator](#the--operator)

## How do arithmetic operators operate on different data types

### The + operator

|        Data types | Effect                                                                                                                        |
| ----------------: | :---------------------------------------------------------------------------------------------------------------------------- |
| Integer + Integer | Adds the two numbers, result will be an integer                                                                               |
|     Float + Float | Adds the two numbers, result will be a float                                                                                  |
|   Integer + Float | Adds the two numbers, result will be a float                                                                                  |
|   String + String | Concatenates the two strings, the result will be a string                                                                     |
|  String + Integer | ***ERROR***: must be str, not int                                                                                             |
|    String + Float | ***ERROR***: must be str, not float                                                                                           |
|       List + List | Creates a new list with the items from the left-hand-side list followed by the items from the right-hand-side list (in order) |
|    List + Integer | ***ERROR***: can only concatenate list (not "int") to list                                                                    |
|      List + Float | ***ERROR***: can only concatenate list (not "float") to list                                                                  |
|     List + String | ***ERROR***: can only concatenate list (not "str") to list                                                                    |

<span style="text-align:center">

<hr style="width:70%">

[Top](#python-training---summary) &emsp; | &emsp; [Home](README.md)

</span>
