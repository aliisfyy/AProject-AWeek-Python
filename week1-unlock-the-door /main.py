import random #random library

letter = [ "A", "B", "C", "D", "E", "F"]    #you can also import string and use string.ascii_letters to make it harder
password = [
    random.choice(letter),
    str(random.randint(0,9)),
    str(random.randint(0,9)),
    random.choice(letter)
]

print(
"""
You're trapped in a dark room!
The only exit is a locked door with a coded keypad.
Crack the password to escape!
-----
  A    (a letter)
-----
  0    (a number)
-----
  0    (a number)
-----
  A    (a letter)
-----
"""
)

while True :
    print("""
Enter your guess :
-----"""
    )
    ans = []
    hint = []

    for i in range (4) :
        if i == 0 or i==3 :
            ans.append((input("  ")).upper())
        else :
            ans.append(input("  "))
        print("-----")

        if ans[i] == password[i] :
            hint.insert(i, f"{ans[i]}")
        elif ans[i] > password[i] :
            hint.insert(i, "<")
        else :
            hint.insert(i, ">")

    if ans == password :
        print("!! Door Opens !!")
        print(f"The passcode is {''.join(password)}")
        break
    
    print("""
Hint :
-----""")
    for i in hint :
        print(f"  {i}")
        print("""-----""")
