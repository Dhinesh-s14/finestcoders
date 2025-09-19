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
        
        
