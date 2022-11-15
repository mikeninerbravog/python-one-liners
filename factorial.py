num1 = 5
num2 = 0
num3 = 10
num4 = 12
factorial = lambda num : 1 if num <= 1 else num*factorial(num-1)
print("Factorial of", num1, ":", factorial(num1))
print("Factorial of", num2, ":", factorial(num2))
print("Factorial of", num3, ":", factorial(num3))
print("Factorial of", num4, ":", factorial(num4))

"""
This code defines a lambda function `factorial` to calculate the factorial of a given number and then applies this function to four different numbers. 

Here's a breakdown of the code:

1. `num1 = 5`: This line defines a variable `num1` and assigns it the value 5.

2. `num2 = 0`: This line defines a variable `num2` and assigns it the value 0.

3. `num3 = 10`: This line defines a variable `num3` and assigns it the value 10.

4. `num4 = 12`: This line defines a variable `num4` and assigns it the value 12.

5. `factorial = lambda num : 1 if num <= 1 else num*factorial(num-1)`: This line defines a lambda function named `factorial` 
that calculates the factorial of a given number `num`. The lambda function is a recursive function. 
It returns 1 if `num` is less than or equal to 1 (base case) and otherwise calculates the factorial by 
multiplying `num` by the factorial of `num - 1`.

6. `print("Factorial of", num1, ":", factorial(num1))`: This line prints the factorial of `num1` by calling the `factorial` 
lambda function with `num1` as an argument. It will print "Factorial of 5 :", followed by the result of the calculation.

7. Similarly, the code prints the factorials of `num2`, `num3`, and `num4` using the `factorial` lambda function. 
However, it's important to note that the factorial of 0 is defined as 1 by convention, so it will return 1 for `num2`.

The output of this code will be:

```
Factorial of 5 : 120
Factorial of 0 : 1
Factorial of 10 : 3628800
Factorial of 12 : 479001600
```

It calculates and prints the factorials of the four numbers you provided.
"""