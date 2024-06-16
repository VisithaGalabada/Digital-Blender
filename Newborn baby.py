import time
import random as rand

def initialize_game():
    global count, hs, stats, days_without_food, food
    count = 0
    try:
        with open("Stuff.txt", "r") as f:
            num = f.readline()
            if num == '':
                hs = 0
            else:
                hs = int(num)
    except FileNotFoundError:
        with open("Stuff.txt", "w") as f:
            hs = 0
    stats = rand.randint(2, 20)
    days_without_food = stats
    food = 0

def main():
    global count, hs, stats, days_without_food, food
    initialize_game()

    print("Hello! You are right now controlling a digital blender and you realize a newborn is in the blender. You are given the option to turn on the blender or let the baby live another day (your main objective is to let the baby live for as long as you can). Good Luck!")
    time.sleep(4)
    print(f"Here's how long the baby can go without food: {stats} days")
    time.sleep(2)

    while True:
        ans = input("Do you want to turn the blender on (y/n) or feed (f)? ")
        if ans == "no" or ans == "n":
            count += 1
            days_without_food -= 1
            food -= 1
            if food < 0:
                food += 1
            print(f"Baby lives another day. Day: {count}")
            if days_without_food <= 0:
                time.sleep(0.5)
                print("The baby starved to death.")
                if count > hs:
                    hs = count
                    print("You got higher than the High score!")
                break
            continue
        elif ans == "yes" or ans == "y":
            time.sleep(0.5)
            print("WAHH!!!")
            time.sleep(1)
            print("GOOGOO")
            time.sleep(1)
            print("GAAGAA")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("(dead)")
            time.sleep(0.5)
            break

        elif ans == "f" or ans == "feed":
            days_without_food = stats
            food += 1
            if food == 3:
                print("The baby was fed to death.")
                if count > hs:
                    hs = count
                    print("You got higher than the High score!")
                break
            continue

    with open("Stuff.txt", "w") as f:
        f.write(str(hs))

    print(f"High score: {hs}\nYour score: {count}")

    tryAgain = input("Do you want to try again (y/n)? ")
    if tryAgain == "no" or tryAgain == "n":
        pass
    else:
        count = 0
        main()

if __name__ == "__main__":
    main()