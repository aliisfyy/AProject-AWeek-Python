## 🚪 Week 1 : Unlock The Door
### 🎲 About :
A Python terminal game where you crack a 4-symbol code (L + N + N + L) to escape a locked room.
(Inspired by "Guess the Number"—but with a layered challenge!)

### 🔐 Password Format :</h3>
Guess a 4-part code
```
  -----
    A    (a letter)
  -----
    0    (a number)
  -----
    0    (a number)
  -----
    A    (a letter)
  -----
```
Example : ```A35D```

### 🎮 How to Play :
1. Enter your guess for each part (top to bottom).
2. Get instant hints after each attempt:
    - ```>``` : Your guess is too high.
    - ```<``` : Your guess is too low.
    - ```A/3``` : Correct symbol!
3. Escape when all 4 symbols match!

### 🛠️ Code Highlights :
- Random Code Generator:
```py
  password = [
    random.choice("ABCDEF"),  # Letter 1  
    str(random.randint(0, 9)),  # Number 1  
    str(random.randint(0, 9)),  # Number 2  
    random.choice("ABCDEF")     # Letter 2  
]
```

### 🖥️ Output Example :
1. Starting the Game
   ```
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
   
     Enter your guess:
     -----
   ```
2. Making Guesses (With Hints)
   ```
     Enter your guess:
     -----
       B
     -----
       5
     -----
       2
     -----
       F
     -----

     Hint:
     -----
       <  
     -----
       5  
     -----
       > 
     -----
       F 
     -----
   ```
3. Winning the Game
   ```
     !! Door Opens !!
     The passcode is C31E
   ```
