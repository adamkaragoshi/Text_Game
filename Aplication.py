from Game.Game import game_state

print("Welcome to my first game!")

health = 10
is_alive = True

name = input("What is your name? ")
print("Hello " + name + "!")

age = input("How old are you, " + name + "? ")
if int(age) < 18:
    print("You cannot play if you are not 18 or over.")
    quit("Player is too young.")
else:
    print("Welcome to my game, let's get started")

    # Situation1
i = 0
while i < 1:
    situation1_input = input("you can turn 'left' or 'right'. ")
    if "left" in situation1_input:
        print("you fall in a pitfall...")
        is_alive = False
        game_state(health, is_alive)
    elif "right" in situation1_input:
        print("Good job! You made through the first question. Stay on your toes.")
        i += 1
    else:
        print("You need to enter a valid value")

# Intermission
print("you have " + str(health) + " hp left")

# Situation2
i = 0
while i < 1:
    situation2_input = input("You arrive at a water crossing where a boat appears. You either take the 'boat' or\
 'go around'. Which will it be? ")
    if "go around" in situation2_input:
        print("you fall in a pitfall...")
        is_alive = False
        game_state(health, is_alive)
    elif "boat" in situation2_input:
        print("You made it through but lost 3 hp because of hungry fish.")
        health -= 3
        i += 1
    else:
        print("You need to enter a valid value")

# Intermission
print("you have " + str(health) + " hp left")

# Situation3
i = 0
while i < 1:
    situation3_input = input("Your last challenge will be to get out of the forest as fast as possible. There are\
 three choices, a 'car', a 'horse', or you can 'run' ")
    if "horse" in situation3_input:
        print("you fall in a pitfall with the horse...")
        is_alive = False
        game_state(health, is_alive)
    elif "run" in situation3_input:
        print("you lose 7 health from wolf bites.")
        health -= 7
        game_state(health, is_alive)
    elif "car" in situation3_input:
        print("You made it through unscathed. Welcome Back!")
        i += 1
    else:
        print("You need to enter a valid value")

print("YOU WIN THE GAME")
