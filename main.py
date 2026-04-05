import random

choices = ["rock", "paper", "scissors"]

user_history = []
user_score = 0
computer_score = 0


def get_probabilities(history):
    total = len(history)

    return {
        "rock": history.count("rock") / total,
        "paper": history.count("paper") / total,
        "scissors": history.count("scissors") / total
    }


def get_computer_choice():
    # If not enough data → random
    if len(user_history) < 3:
        return random.choice(choices)

    probs = get_probabilities(user_history)

    # Predict using weighted probability
    predicted = random.choices(
        population=choices,
        weights=[probs["rock"], probs["paper"], probs["scissors"]]
    )[0]

    # Counter strategy
    counter = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    return counter[predicted]


def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"


def play():
    global user_score, computer_score

    print("🎮 Rock Paper Scissors (Smart AI)")
    print("Type 'exit' to quit\n")

    while True:
        user = input("Enter rock, paper, or scissors: ").lower()

        if user == "exit":
            print("\n🏁 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        if user not in choices:
            print("❌ Invalid input. Try again.\n")
            continue

        computer = get_computer_choice()
        user_history.append(user)

        print("Computer chose:", computer)

        result = get_winner(user, computer)

        if result == "draw":
            print("🤝 Draw!")
        elif result == "user":
            print("🎉 You win!")
            user_score += 1
        else:
            print("💻 Computer wins!")
            computer_score += 1

        print(f"📊 Score → You: {user_score} | Computer: {computer_score}\n")


if __name__ == "__main__":
    play()