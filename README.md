Problem Statement
You are given an integer n and a maximum iteration limit k.
Define the process:

1. Reverse the digits of n.
2. Add this reversed number to n.
3. Check if the result is a palindrome.
4. If not, repeat the process with the new number.

If a palindrome appears within k iterations, return the number of iterations and the
palindrome.


 Reverse and Add until Palindrome

This program takes an integer input from the user, reverses its digits, adds it to the original number, and repeats the process until a **palindrome number** is found (or until the given limit is reached).  


📌 How It Works
1. User enters a number (`a`) and a maximum iteration limit (`limit`).
2. The program reverses the number and adds it to the original.
3. After each addition, the result is checked:
   - If the number is a palindrome → process stops.
   - Otherwise → process repeats until the limit is reached.









        
        
