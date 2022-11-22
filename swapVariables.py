a = 100
b = 12
print("Value of a before swapping:", a)
print("Value of b before swapping:", b)
a, b = b, a
print("Value of a after swapping:", a)
print("Value of b after swapping:", b)

"""
This code swaps the values of two variables `a` and `b` without using a temporary variable. Here's a breakdown of the code:

1. `a = 100`: This line defines a variable `a` and assigns it the value `100`.

2. `b = 12`: This line defines a variable `b` and assigns it the value `12`.

3. `print("Value of a before swapping:", a)`: This line prints the value of `a` before the swap. It will display "Value of a before swapping: 100".

4. `print("Value of b before swapping:", b)`: This line prints the value of `b` before the swap. It will display "Value of b before swapping: 12".

5. `a, b = b, a`: This line swaps the values of `a` and `b` without using a temporary variable. 
It does so by creating a tuple `(b, a)` on the right side and then unpacking it into the variables `a` and `b`.

6. `print("Value of a after swapping:", a)`: This line prints the value of `a` after the swap. 
It will display "Value of a after swapping: 12", which is the value of `b` before the swap.

7. `print("Value of b after swapping:", b)`: This line prints the value of `b` after the swap. 
It will display "Value of b after swapping: 100", which is the value of `a` before the swap.

As a result, after running this code, the values of `a` and `b` will be swapped, and you'll see the values displayed 
before and after the swap as described above.
"""