import random

tic = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

dic = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

choice = input("Choose symbol from 'X' and 'O': ").upper()
while choice not in ['X', 'O']:
    choice = input("Invalid choice. Please choose either 'X' or 'O': ").upper()

placed = []


def computer(in_list):
    # Generate random number for computer's move
    while True:
        computer_guess = random.randint(1, 9)
        if computer_guess not in in_list:
            return computer_guess


def check_winner():
    for i in range(3):
        if tic[i][0] == tic[i][1] == tic[i][2] != "_":
            return tic[i][0]
        if tic[0][i] == tic[1][i] == tic[2][i] != "_":
            return tic[0][i]
    if tic[0][0] == tic[1][1] == tic[2][2] != "_":
        return tic[0][0]
    if tic[0][2] == tic[1][1] == tic[2][0] != "_":
        return tic[0][2]
    return None


def print_board():
    # Print the board after each move
    j = 0
    for i in tic:
        a = ' | '.join(map(str, i))
        print(a)
        if j < 2:
            print("-------")
        j += 1


game_is_on = True
while game_is_on:
    if len(placed) == 9:
        print("It's a draw!")
        game_is_on = False
        break

    user = int(input("Enter a number between 1-9 to make your move: "))
    while user not in range(1, 10) or user in placed:
        user = int(input("Invalid move. Enter a number between 1-9 to make your move: "))

    placed.append(user)
    value = dic[user]
    tic[value[0]][value[1]] = choice

    winner = check_winner()
    if winner:
        print_board()
        if choice==winner:
            print(f"computer wins!")
        else:
            print("You win")
        game_is_on = False
        break

    if len(placed) != 9:
        computer_ = computer(placed)
        placed.append(computer_)
        computer_choice = "O" if choice == "X" else "X"
        value1 = dic[computer_]
        tic[value1[0]][value1[1]] = computer_choice

        winner = check_winner()
        if winner:
            print_board()
            print(f"{winner} wins!")
            game_is_on = False
            break

    print_board()
