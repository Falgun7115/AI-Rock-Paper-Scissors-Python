import random
import json
import os

choices = ["rock", "paper", "scissors"]
DATA_FILE = "game_data.json"


def load_data() -> dict:
    """Load saved scores and history from file."""
    if not os.path.exists(DATA_FILE):
        return {"user_score": 0, "computer_score": 0, "user_history": []}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # Validate expected keys exist
            for key in ("user_score", "computer_score", "user_history"):
                if key not in data:
                    raise KeyError(f"Missing key: {key}")
            return data
    except (json.JSONDecodeError, KeyError) as e:
        print(f"⚠️  Corrupted save file ({e}). Starting fresh.\n")
        return {"user_score": 0, "computer_score": 0, "user_history": []}


def save_data(user_score: int, computer_score: int, user_history: list) -> None:
    """Persist scores and history to file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(
                {"user_score": user_score, "computer_score": computer_score, "user_history": user_history},
                f,
                indent=2
            )
    except OSError as e:
        print(f"⚠️  Could not save data: {e}")


def get_probabilities(history: list) -> dict:
    total = len(history)
    return {choice: history.count(choice) / total for choice in choices}


def get_computer_choice(user_history: list) -> str:
    if len(user_history) < 3:
        return random.choice(choices)

    probs = get_probabilities(user_history)
    predicted = random.choices(
        population=choices,
        weights=[probs["rock"], probs["paper"], probs["scissors"]]
    )[0]

    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[predicted]


def get_winner(user: str, computer: str) -> str:
    if user == computer:
        return "draw"
    winning_combos = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    return "user" if (user, computer) in winning_combos else "computer"


def display_result(result: str, user_score: int, computer_score: int) -> None:
    """Use match/case to display round result."""
    match result:
        case "draw":
            print("🤝 Draw!")
        case "user":
            print("🎉 You win!")
        case "computer":
            print("💻 Computer wins!")
        case _:
            print("❓ Unknown result.")

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}\n")


def play() -> None:
    data = load_data()
    user_score: int = data["user_score"]
    computer_score: int = data["computer_score"]
    user_history: list = data["user_history"]

    print("🎮 Rock Paper Scissors (Smart AI)")
    print(f"📂 Loaded → You: {user_score} | Computer: {computer_score}")
    print("Type 'exit' to quit or 'reset' to clear scores.\n")

    while True:
        try:
            user = input("Enter rock, paper, or scissors: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Game interrupted.")
            break

        match user:
            case "exit":
                print("\n🏁 Final Score:")
                print(f"You: {user_score} | Computer: {computer_score}")
                save_data(user_score, computer_score, user_history)
                print("💾 Progress saved.")
                break

            case "reset":
                user_score, computer_score, user_history = 0, 0, []
                save_data(user_score, computer_score, user_history)
                print("🔄 Scores reset.\n")

            case "rock" | "paper" | "scissors":
                computer = get_computer_choice(user_history)
                user_history.append(user)

                print(f"Computer chose: {computer}")
                result = get_winner(user, computer)

                match result:
                    case "user":
                        user_score += 1
                    case "computer":
                        computer_score += 1

                display_result(result, user_score, computer_score)
                save_data(user_score, computer_score, user_history)

            case _:
                print("❌ Invalid input. Try 'rock', 'paper', or 'scissors'.\n")


if __name__ == "__main__":
    play()
