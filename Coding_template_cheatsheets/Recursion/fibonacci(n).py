def fibonacci(n):
      # base cases
  if n <= 1:
    return n
  return (fibonacci(n - 1) + fibonacci(n - 2))


nterms = int(input("Insert the number of element of the sequence that you want to display:"))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i))