import random

draw = 0
you_win = 0
computer_win = 0

while True:

    print("""
    r for rock ✊
    p for paper ✋
    s for scissors ✌
    """)


    computer = random.choice([1,2,3])
    youstr = input("Enter your choice : ")
    youdict = {"r":1,"p":2,"s":3}
    you = youdict[youstr]
    reversedict = {1:"Rock✊",2:"Paper✋",3:"scissors✌"}


    print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}\n")


    if computer == you :
        draw += 1
        print("It's a draw.")

    if youstr not in youdict :
        print("Please choose between (r/p/s)")

    else:
        if computer == 1 and you == 3 :
            computer_win += 1
            print("""Rock crushes Scissors.✊
    Computer win.🥳""")
        elif computer == 2 and you == 1 :
            computer_win += 1
            print("""Paper wraps Rock.✋
    Computer win.🥳""")
        elif computer == 3 and you == 2 :
            computer_win += 1
            print("""Scissors cuts Paper.✌
    Computer win.🥳""")
        elif you == 1 and computer == 3 :
            you_win += 1
            print("""Rock crushes Scissors.✊
    You win.🥳""")
        elif you == 2 and computer == 1 :
            you_win += 1
            print("""Paper wraps Rock.✋
    You win.🥳""")
        elif you == 3 and computer == 2 :
            you_win += 1
            print("""Scissors cuts Paper.✌
    You win.🥳""")
        else:
            print("Something went wrong!!")


    
    print("~~~~💯Scoreboard💯~~~~")
    print(f"Draw : {draw}")
    print(f"You wins : {you_win}")
    print(f"Computer wins : {computer_win}")

    user = input("If you want to exit the game then click (E) : ")

    if user.lower() == "e":
        print("Game over!!")
        break
    else:
        continue