import screen
import random
import pyautogui
import time

def slowClick(coord):
    # move to x y
    pyautogui.moveTo(coord)
    # wait 0.2 seconds
    time.sleep(0.2)
    # click
    pyautogui.click()
    # wait 0.2 seconds
    time.sleep(0.2)

def oldAI():
    # Get all the moves
    moves = screen.getMultithreadMoves()
    ok = False

    weight = [0, 0, 0, 0]

    # Loop through the moves
    # Assign a weight to a move based on the effectiveness of the move
    # If the move is effective, assign a weight of 1
    # If the move is not effective, assign a weight of 0
    # If the move is super effective, assign a weight of 5
    # If the move is status, assign a weight of -1
    for i in range(len(moves)):
        if "not very effective" in moves[i].lower() or "notvery effective" in moves[i].lower():
            weight[i] = 2
        elif "super effective" in moves[i].lower() or "supereffective" in moves[i].lower():
            weight[i] = 10
        elif "status" in moves[i].lower():
            weight[i] = 0
        elif "effective" in moves[i].lower():
            weight[i] = 3
        else:
            weight[i] = 0

    print(moves)
    print(weight)

    # Randomly choose a move based on the weight
    # use the random.choices function to choose a move based on the weight
    result = random.choices([1,2,3,4], weight)
    print(result)

    # based off the result and the coordinates in the screen class, press the move
    if result[0] == 1:
        pyautogui.click(screen.move1[0:2])
    elif result[0] == 2:
        pyautogui.click(screen.move2[0:2])
    elif result[0] == 3:
        pyautogui.click(screen.move3[0:2])
    elif result[0] == 4:
        pyautogui.click(screen.move4[0:2])

def newAI():
    super = []
    effective = []
    noteff = []
    choice = 0
    # Get all the moves
    moves = screen.getMultithreadMoves()
    ok = False

    # Loop through the moves
    for i in range(0, len(moves)):
        if "super effective" in moves[i].lower() or "supereffective" in moves[i].lower():
                super.append(i + 1)
        # If the move is not effective, put the index in a list
        elif "not very effective" in moves[i].lower() or "notvery effective" in moves[i].lower():
            noteff.append(i + 1)
        # If the move is effective, put the index in a list
        elif "effective" in moves[i].lower():
            effective.append(i + 1)

    print(super)
    print(effective)
    print(noteff)

    # Check if the super list has something
    if len(super) > 0:
        # Randomly choose a move
        choice = random.choice(super)
    # Check if the effective list has something
    elif len(effective) > 0:
        # Randomly choose a move
        choice = random.choice(effective)
    # Check if the noteff list has something
    elif len(noteff) > 0:
        # Randomly choose a move
        choice = random.choice(noteff)
    else:
        # something went wrong
        choice = random.choice([1,2,3,4])

    print(choice)

    # based off the result and the coordinates in the screen class, press the move
    if choice == 1:
        slowClick(screen.move1[0:2])
    elif choice == 2:
        slowClick(screen.move2[0:2])
    elif choice == 3:
        slowClick(screen.move3[0:2])
    elif choice == 4:
        slowClick(screen.move4[0:2])


if __name__ == "__main__":
    newAI()