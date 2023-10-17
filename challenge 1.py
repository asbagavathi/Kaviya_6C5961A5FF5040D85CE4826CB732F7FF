def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number =int(input("Enter the value : "))
res=factorial(number)
print("factorial of {} is {}".format(number,res)) 
