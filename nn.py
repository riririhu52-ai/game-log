import random
import time

print("=====================================")
print("   WELCOME TO THE MULTIPLICATION GAME")
print("=====================================\n")

# Teacher hosting
teacher = input("Teacher hosting the game: ")

# Player setup
players = []
num_players = int(input("Number of players: "))

for i in range(num_players):
    name = input(f"Enter player {i+1} name: ")
    players.append({"name": name, "score": 0, "streak": 0})

rounds = 5

# Countdown timer function
def countdown(t):
    for i in range(t, 0, -1):
        print(f"Time left: {i} seconds", end="\r")
        time.sleep(1)

# Game rounds
for r in range(1, rounds + 1):

    print("\n======================")
    print(f"ROUND {r}")
    print("======================")

    # Random special events
    event = random.choice(["normal", "double", "speed", "bonus"])

    if event == "double":
        print("🔥 DOUBLE POINT ROUND")
        points = 2
        time_limit = 10
    elif event == "speed":
        print("⚡ SPEED ROUND")
        points = 1
        time_limit = 5
    elif event == "bonus":
        print("🎁 BONUS ROUND")
        points = 3
        time_limit = 10
    else:
        print("Normal Round")
        points = 1
        time_limit = 10

    # Questions for each player
    for player in players:

        a = random.randint(2, 12)
        b = random.randint(2, 12)

        print(f"\n{player['name']}, your question:")
        # Show × for presentation
        print(f"What is {a} × {b}?")

        countdown(time_limit)

        start = time.time()
        answer = input("\nAnswer: ")
        end = time.time()

        # Time check
        if end - start > time_limit:
            print("⏳ Too slow!")
            player["streak"] = 0
            continue

        # Correct answer calculation uses *
        correct_answer = a * b

        # Answer check
        try:
            if int(answer) == correct_answer:
                print("✅ Correct!")
                player["score"] += points
                player["streak"] += 1

                # Streak bonus
                if player["streak"] == 3:
                    print("🎯 STREAK BONUS! +2 points")
                    player["score"] += 2
                    player["streak"] = 0

            else:
                print("❌ Wrong!")
                player["streak"] = 0

        except:
            print("Invalid input!")
            player["streak"] = 0

    # Scores after each round
    print("\nCurrent Scores:")
    for p in players:
        print(f"{p['name']}: {p['score']}")

# Sudden death round
print("\n======================")
print("💀 SUDDEN DEATH ROUND")
print("======================")

a = random.randint(10, 15)
b = random.randint(10, 15)

for player in players:

    print(f"\n{player['name']} sudden death question!")
    print(f"What is {a} × {b}?")

    answer = input("Answer: ")

    try:
        correct_answer = a * b
        if int(answer) == correct_answer:
            print("🔥 Correct! +4 points")
            player["score"] += 4
        else:
            print("❌ Wrong!")
    except:
        print("Invalid input!")

# Final boss question
print("\n======================")
print("👑 FINAL BOSS QUESTION")
print("======================")

a = random.randint(15, 20)
b = random.randint(15, 20)

for player in players:

    print(f"\n{player['name']} BOSS QUESTION!")
    print(f"What is {a} × {b}?")

    answer = input("Answer: ")

    try:
        correct_answer = a * b
        if int(answer) == correct_answer:
            print("🏆 AMAZING! +5 points")
            player["score"] += 5
        else:
            print("❌ Wrong!")
    except:
        print("Invalid input!")

# Final scoreboard
print("\n======================")
print("🏆 FINAL SCOREBOARD")
print("======================")

winner = None
high_score = -1

for p in players:
    print(f"{p['name']}: {p['score']}")
    if p["score"] > high_score:
        high_score = p["score"]
        winner = p["name"]

print(f"\n🎉 WINNER: {winner}")
print(f"Game hosted by {teacher}")
