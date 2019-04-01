# Auther:Hook
# Date:2019.4.1
# Content:a game

import random

while True:
    l = ['Rock', 'Scissors', 'Paper ']
    gz = [["Rock", "Scissors"], ["Paper ", "Rock"], ["Scissors", "Paper "]]
    s = random.choice(l)
    print(s)
    n = input("play finger-guessing game:")
    if n == 'q':
        break
    if n in l:
        if n == s:
            print("draw")
        elif [n, s] in gz:
            print("win")
        else:
            print("lose")
    else:
        print("!")
