# singleExpressionPython

This is a code challange I enjoy playing with - solve some puzzle as a single expression in Python. There are a few tricks that make this possible

# Array as If

## Basic
Because of coersion, Python will interpret bools as ints when used as an indicie. This can be leveraged in an array as:
```python
x = ['ifFalse', 'ifTrue'][condition]
```

## With Methods
The problems with this approach is that Python is not lazy so it doesn't work for methods
```python
x = [ifFalse(), ifTrue()][conditional]
```

There is one easy way around this. If both methods have the same signature (or we can make them have the same signature) we can call it like this
```python
x = [ifFalse, ifTrue][conditional]()
```

But if they don't we can force Python to be lazy with logical operators
```python
x = [conditional or ifFalse(),conditional and ifTrue()][conditional]
```
