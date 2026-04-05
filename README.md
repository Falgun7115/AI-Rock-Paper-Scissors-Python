# 🎮 AI Rock Paper Scissors (Python)

## 📌 Overview

This project is an intelligent implementation of the classic **Rock-Paper-Scissors** game using Python.
Unlike traditional versions, this game includes a simple **AI-based prediction system** that learns from the player's past moves and adapts its strategy accordingly.

---

## 🧠 Features

* 🎯 AI-based move prediction using probability
* 📊 Learns from user history
* ⚖️ Weighted decision-making using past data
* 💾 Persistent score and history storage (JSON file)
* 🔁 Continuous gameplay loop
* 🧩 Error handling for corrupted data files
* 🆕 Reset and Exit functionality
* 🧵 Clean and modular code structure

---

## ⚙️ How It Works

1. The game stores user choices in a history list.
2. It calculates the probability of each move:

   * Rock
   * Paper
   * Scissors
3. Based on past behavior, the AI predicts the user's next move.
4. The computer plays the **counter move** to increase its chances of winning.

---

## 📂 Project Structure

```
📁 AI-RockPaperScissors/
│── game.py
│── game_data.json   # Auto-created to store scores & history
│── README.md
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-RockPaperScissors.git
cd AI-RockPaperScissors
```

### 2. Run the Game

```bash
python game.py
```

---

## 🎮 Gameplay Instructions

* Enter:

  * `rock`
  * `paper`
  * `scissors`
* Special commands:

  * `reset` → Reset scores and history
  * `exit` → Save progress and quit

---

## 💾 Data Storage

* Game data is stored in:

  ```
  game_data.json
  ```
* Stores:

  * User score
  * Computer score
  * User move history

---

## 📊 Example Output

```
🎮 Rock Paper Scissors (Smart AI)
📂 Loaded → You: 2 | Computer: 3

Enter rock, paper, or scissors: rock
Computer chose: paper
💻 Computer wins!
📊 Score → You: 2 | Computer: 4
```

---

## 🚀 Future Improvements

* 🔥 GUI using Tkinter or PyQt
* 📈 Advanced AI using Markov Chains
* 🌐 Web-based version (Flask/Streamlit)
* 🧠 Machine Learning model for prediction

---

## 🛠️ Tech Stack

* Python 3
* JSON (for storage)
* Standard Libraries:

  * `random`
  * `json`
  * `os`

---

## 📌 Key Concepts Used

* Probability & Statistics
* File Handling (Persistent Storage)
* Exception Handling
* Pattern Matching (`match-case`)
* Basic AI Logic

---

## 🤝 Contributing

Feel free to fork this repository and improve the project!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Your Name**

---

⭐ If you like this project, don't forget to give it a star!
