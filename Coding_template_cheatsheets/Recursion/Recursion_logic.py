
# Mental Model of recursion in python 

def sum_to_one(n):
    result = 1
    call_stack = []
  
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)

    print("BASE CASE REACHED")

    while len(call_stack) != 0:
        return_value = call_stack.pop()
        print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
        result += return_value['n_value']


    return result, call_stack

sum_to_one(4)


#We want a function that takes an integer as an input and returns the sum of all numbers from the input down to 1.

#Here’s how this function would look if we were to write it iteratively:

def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result
 
sum_to_one(4)
# num is set to 4, 3, 2, and 1
# 10

#we want a recursive function that will produce the following function calls:

#recursive_sum_to_one(4)
#recursive_sum_to_one(3)
#recursive_sum_to_one(2)
#recursive_sum_to_one(1)


#Every recursive function needs a base case when the function does not recurse,
#  and a recursive step, when the recursing function moves towards the base case.

#Base case:

#The integer given as input is 1.
#Recursive step:

#The recursive function call is passed an argument 1 less than the last function call.

# How actually we will write it: 

def sum_to_one(n): 
  if n == 1: 
    return n 
  else:
    print("Recursing with input: {0}".format(n))
    return n + sum_to_one(n-1)


print(sum_to_one(7))


#Other example 
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(12))

# IF I INPUT A TOO LARGE NUMBER > ERROR > STACK OVERFLOW 

# SO WHY RECURSION?? 

#Even when there is room for any reasonable input, recursive functions tend to be at least a little 
# less efficient than comparable iterative solutions because of the call stack.

#The beauty of recursion is how it can reduce complex problems into an elegant solution of only a few lines of code.
#  Recursion forces us to distill a task into its smallest piece, the base case, and the smallest step to get there, 
# the recursive step.








