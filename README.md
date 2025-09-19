Problem Statement
You are given an integer n and a maximum iteration limit k.
Define the process:

1. Reverse the digits of n.
2. Add this reversed number to n.
3. Check if the result is a palindrome.
4. If not, repeat the process with the new number.

If a palindrome appears within k iterations, return the number of iterations and the
palindrome.

PYTHON CODE FOR THE ABOVE PROBLEM STATEMENT:
a = int(input("enter your value: "))
limit = int(input("Enter your limit: "))
for i in range(limit):
    b = str(a)[::-1]
    c = int(b)
    a = a+c
    print(f"step{i+1} = {a}")
    if str(a) == str(a)[::-1]:
        print("palindrome found = ",a)
        break
        
        
