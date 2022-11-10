str1 = "MUO"
str2 = "madam"
str3 = "MAKEUSEOF"
str4 = "mom"
print('Yes') if str1 == str1[::-1] else print('No')
print('Yes') if str2 == str2[::-1] else print('No')
print('Yes') if str3 == str3[::-1] else print('No')
print('Yes') if str4 == str4[::-1] else print('No')

"""
In this code, you are checking whether each of the given strings is a palindrome or not. A palindrome is a word or phrase that reads the same forwards and backward. Here's a breakdown of your code:

1. `str1 = "MUO"`: Defines a string variable `str1` with the value "MUO".

2. `str2 = "madam"`: Defines another string variable `str2` with the value "madam".

3. `str3 = "MAKEUSEOF"`: Defines a third string variable `str3` with the value "MAKEUSEOF".

4. `str4 = "mom"`: Defines a fourth string variable `str4` with the value "mom".

5. `print('Yes') if str1 == str1[::-1] else print('No')`: This line checks if `str1` is a palindrome. It does this by comparing `str1` with its reverse, which is obtained by using slicing with `[::-1]`. If they are equal, it prints 'Yes', indicating that `str1` is a palindrome. Otherwise, it prints 'No'. In this case, "MUO" is not a palindrome, so it will print 'No'.

6. Similarly, the code checks `str2`, `str3`, and `str4` for palindromes using the same logic:
   - `str2` is a palindrome ("madam"), so it will print 'Yes'.
   - `str3` is not a palindrome ("MAKEUSEOF"), so it will print 'No'.
   - `str4` is a palindrome ("mom"), so it will print 'Yes'.

The code prints 'Yes' or 'No' based on whether each string is a palindrome.
"""