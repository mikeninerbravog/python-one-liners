list1 = [12, 345, 123, 34, 23, 37]
list2 = ['m', 'a', 'k', 'e', 'u', 's', 'e', 'o', 'f']
list3 = [5, 4, 3, 2, 1]
print("Before Sorting:")
print(list1)
print(list2)
print(list3)
list1.sort()
list2.sort()
list3.sort()
print("After Sorting:")
print(list1)
print(list2)
print(list3)

"""
This code demonstrates how to sort lists in Python using the `sort()` method. Here's a breakdown of the code:

1. `list1 = [12, 345, 123, 34, 23, 37]`: This line defines a list called `list1` containing a sequence of integers.

2. `list2 = ['m', 'a', 'k', 'e', 'u', 's', 'e', 'o', 'f']`: This line defines another list called `list2` containing a sequence of characters (letters).

3. `list3 = [5, 4, 3, 2, 1]`: This line defines a third list called `list3` containing a sequence of integers.

4. `print("Before Sorting:")`: This line prints the message "Before Sorting:" to indicate that the original lists will be printed.

5. `print(list1)`: This line prints the original contents of `list1`.

6. `print(list2)`: This line prints the original contents of `list2`.

7. `print(list3)`: This line prints the original contents of `list3`.

8. `list1.sort()`: This line sorts `list1` in ascending order using the `sort()` method, which modifies the list in place.

9. `list2.sort()`: This line sorts `list2` in lexicographic (alphabetical) order.

10. `list3.sort()`: This line sorts `list3` in ascending order.

11. `print("After Sorting:")`: This line prints the message "After Sorting:" to indicate that the sorted lists will be printed.

12. `print(list1)`: This line prints the sorted contents of `list1`.

13. `print(list2)`: This line prints the sorted contents of `list2`.

14. `print(list3)`: This line prints the sorted contents of `list3`.

The output of this code will show the original lists and the lists after sorting:

```
Before Sorting:
[12, 345, 123, 34, 23, 37]
['m', 'a', 'k', 'e', 'u', 's', 'e', 'o', 'f']
[5, 4, 3, 2, 1]
After Sorting:
[12, 23, 34, 37, 123, 345]
['a', 'e', 'e', 'f', 'k', 'm', 'o', 's', 'u']
[1, 2, 3, 4, 5]
```

As you can see, the lists are sorted according to their respective data types and the sorting order.
"""