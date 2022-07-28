#This function, sum_digits(), 
# produces the sum of all the digits in a positive number as if they were each a single number:

def sum_digits(n):
      if n < 0:
    ValueError("Inputs 0 or greater only!")
  if n <= 9: # if the number has just one digit 
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit


# test cases

print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

