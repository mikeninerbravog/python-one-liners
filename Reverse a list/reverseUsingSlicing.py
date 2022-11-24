arr = [1, 2, 3, 4, 5, 6]
print(arr)
reversedArr = arr[::-1]
print(reversedArr)

"""
This code snippet also reverses a list, but it uses slicing to create a reversed copy of the original list. Here's a breakdown of the code:

1. `arr = [1, 2, 3, 4, 5, 6]`: This line defines a list `arr` containing a sequence of integers.

2. `print(arr)`: This line prints the original list `arr` to the console.

3. `reversedArr = arr[::-1]`: This line uses slicing to create a reversed copy of the original list `arr`. The slice notation `[::-1]` 
means "start from the end and go backward with a step of -1." It effectively creates a reversed copy of the list, 
which is assigned to the variable `reversedArr`.

4. `print(reversedArr)`: This line prints the newly created list `reversedArr`, which contains the elements of the original list `arr` in reversed order.

The output of this code will be:

```
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
```

As you can see, the original list is printed, and then a new list `reversedArr` is created, which contains the elements of the 
original list in reverse order, and it's also printed.
"""