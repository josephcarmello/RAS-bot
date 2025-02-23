# 📢 RAS Bot

An informative Discord bot that listens for `!` commands and responds dynamically based on a separate `responses.py` file. Supports both plain text and embedded responses.

## 🚀 Features

- Dynamically registers commands from `responses.py`
- Supports both text and rich embeds
- Helps with repetitive questions that are frequently reanswered in support and general channels.

---

## 📥 Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/josephcarmello/RAS-bot.git
cd YOUR_REPO
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project directory and add your bot token:

```ini
DISCORD_BOT_TOKEN=your_token
```

---

## ▶️ Running the Bot

```sh
python bot.py
```

If everything is set up correctly, you should see:

```sh
Logged in as YourBotName
```

---

## 🛠 Adding New Commands

To add a new command, simply update `responses.py`. No need to modify `bot.py`!

Example:

```python
RESPONSE_MAP["newcommand"] = "This is a new command response!"
```

Now, the bot will automatically respond to `!newcommand`.

---

## 📝 Requirements

- Python 3.8+
- `discord.py`
- `python-dotenv`

To install all dependencies:

```sh
pip install -r requirements.txt
```

---

## 🏗 Project Structure

```
📁 /
 ├── bot.py
 ├── responses.py
 ├── .env
 ├── requirements.txt
 ├── README.md
```

---

## 📜 License

This project is licensed under MIT License.

---
