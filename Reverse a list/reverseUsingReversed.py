arr = [1, 2, 3, 4, 5, 6]
print(arr)
reversedArr = list(reversed(arr))
print(reversedArr)

"""
This code reverses a list using the `reversed()` function and then converts the reversed iterable into a new list. Here's a breakdown of the code:

1. `arr = [1, 2, 3, 4, 5, 6]`: This line defines a list `arr` containing a sequence of integers.

2. `print(arr)`: This line prints the original list `arr` to the console.

3. `reversedArr = list(reversed(arr))`: This line reverses the order of elements in the list `arr` using the `reversed()` function. The `reversed()` 
function returns a reverse iterator. To convert it back into a list, `list()` is used to create a new list, which is assigned to the variable `reversedArr`.

4. `print(reversedArr)`: This line prints the newly created list `reversedArr`, which contains the elements of the original list `arr` in reversed order.

The output of this code will be:

```
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
```

As you can see, the original list is printed, and then a new list `reversedArr` is created, containing the elements of the original list in reverse order, 
which is also printed.
"""