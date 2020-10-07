import random
while True:
    user_inp = int(input("Give a input. Press '1' for stone, '2' for paper and '3' for scissor.\n"))
    comp_inp = random.randrange(1, 4)
    if user_inp == 1:
        if comp_inp == 1:
            print(f"You: Stone\nComputer: Stone.\nIts a draw")
        elif comp_inp == 2:
            print(f"You: Stone\nComputer: Paper.\nComputer won")
        elif comp_inp == 3:
            print(f"You: Stone\nComputer: Scissor.\nYou won.")
    elif user_inp == 2:
        if comp_inp == 1:
            print(f"You: Paper\nComputer: Stone.\nYou won")
        elif comp_inp == 2:
            print(f"You: Paper\nComputer: Paper.\nIts a draw")
        elif comp_inp == 3:
            print(f"You: Paper\nComputer: Scissor.\nComputer won")
    elif user_inp == 3:
        if comp_inp == 1:
            print(f"You: Scissor\nComputer: Stone.\nComputer won")
        elif comp_inp == 2:
            print(f"You: Scissor\nComputer: Paper.\nYou won")
        elif comp_inp == 3:
            print(f"You: Scissor\nComputer: Scissor.\nIts a draw")
    else:
        print(f"Please input a correct number")