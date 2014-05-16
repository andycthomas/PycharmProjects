__author__ = 'andythomas'
digit_numbers = list(range(100, 1000))
digit_numbers_reversed = list(reversed(digit_numbers))
multiplying = (x*y for x in digit_numbers for y in digit_numbers_reversed)
dirty_palindromes = map(lambda pol: pol if str(pol) == str(pol)[::-1] else 0, list(multiplying))
print(max(dirty_palindromes))