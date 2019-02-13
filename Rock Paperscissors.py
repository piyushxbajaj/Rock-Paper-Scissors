import random
ch=1
while True:
    print("Choose any one of the following (1)Rock, (2)Paper and (3)Scissors ")
    choo = int(input("Enter the number=="))
    a = random.randint(1,3)
    if choo == a:
        print("It is a draw")
    if choo==1:
        if a == 3:
            print("You win")
        elif a == 2:
            print("You lose")
    if choo==2:
        if a == 1:
            print("You win")
        elif a == 3:
            print("You lose")
    if choo==3:
        if a == 2:
            print("You win")
        elif a == 1:
            print("You lose")
    print("\n")
    ch = input("Do you want to play more? (1) YES (2) NO")
    print("\n \n")
    if ch ==2:
        break
    
