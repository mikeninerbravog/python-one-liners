from functools import reduce; fibSequence = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

print(fibSequence(10))
print(fibSequence(5))
print(fibSequence(6))

"""
This code defines a lambda function called `fibSequence` that generates a Fibonacci sequence and then applies this function to different values of `n`. 
It uses the `reduce` function from the `functools` module to build the sequence iteratively. Here's a breakdown of the code:

1. `from functools import reduce`: This line imports the `reduce` function from the `functools` module. The `reduce` function is 
used to accumulate values iteratively.

2. `fibSequence = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])`: 
This line defines a lambda function `fibSequence` that generates a Fibonacci sequence of length `n`. 

It uses the `reduce` function to iteratively build the sequence. Here's how it works:
   - `range(n-2)`: It generates a range of values from 0 to `n-3`. 
   
   This is used as the iterable to control how many Fibonacci numbers are generated (n-2 because we already have the first two numbers [0, 1]).
   - `[0, 1]`: This is the initial sequence with the first two Fibonacci numbers.

   The `reduce` function iterates over the range and, for each step, appends the sum of the last two elements of the sequence to the sequence itself.

3. `print(fibSequence(10))`: This line calls the `fibSequence` lambda function with `n` set to 10, which will generate the first 10 Fibonacci numbers. 
It prints the resulting list.

4. `print(fibSequence(5))`: This line calls the `fibSequence` lambda function with `n` set to 5, which will generate the first 5 Fibonacci numbers. 
It prints the resulting list.

5. `print(fibSequence(6))`: Similarly, this line calls the `fibSequence` lambda function with `n` set to 6, generating the first 6 Fibonacci 
numbers and printing the resulting list.

The output of this code will be:

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[0, 1, 1, 2, 3]
[0, 1, 1, 2, 3, 5]
```

These are the Fibonacci sequences for the given values of `n`.
"""