s = "Welcome"
print(s)
reversedString = s[::-1]
print(reversedString)

"""
This code snippet demonstrates how to reverse a string in Python. Here's a breakdown of the code:

1. `s = "Welcome"`: This line defines a string variable `s` with the value "Welcome".

2. `print(s)`: This line prints the original string `s` to the console. So, it will print "Welcome".

3. `reversedString = s[::-1]`: This line creates a new string `reversedString` by using slicing (`[::-1]`) on the original string `s`. 
The `[::-1]` slicing notation is a way to reverse the string. It starts from the end of the string and goes backward with a step of -1.

4. `print(reversedString)`: This line prints the reversed string `reversedString` to the console.

The output of this code will be:

```
Welcome
emocleW
```

The first `print` statement displays the original string, and the second `print` statement shows the reversed version of the string.
"""