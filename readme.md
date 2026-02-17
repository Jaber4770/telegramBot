```markdown
# 🤖 Telegram Bot using Python

A simple Telegram bot built with Python for practice and learning purposes.  
This project helps beginners understand how Telegram bots work and how to build automation using Python.
```
<img src="https://raw.githubusercontent.com/Jaber4770/telegramBot/refs/heads/main/images/bot-img.png" width="450">
```


---

## 🚀 Features

- `/start` – Start the bot and get a welcome message  
- `/help` – Show available commands  
- `/python` – Get Python learning resources  
- `/ip <ip_address>` – Get basic IP information (country, city, ISP)

---

## 🛠️ Technologies Used

- Python 3  
- python-telegram-bot  
- Requests (for API calls)  
- Telegram Bot API  

---

## 📂 Project Structure

```

telegram-bot/
│
├── bot.py          # Main bot file
├── .gitignore      # Git ignore file
├── README.md       # Project documentation
└── .venv/          # Virtual environment (ignored)

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/telegram-bot-python.git
cd telegram-bot-python
````

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install python-telegram-bot requests
```

---

### 4️⃣ Add Your Bot Token

Open `bot.py` and replace:

```python
TOKEN = "YOUR_BOT_TOKEN"
```

Get your token from **@BotFather** on Telegram.

⚠️ Never share your bot token publicly.

---

### 5️⃣ Run the Bot

```bash
python bot.py
```

You should see:

```
Bot is running...
```

---

## 🧪 Test Commands on Telegram

```
/start
/help
/python
/ip 8.8.8.8
```

---

## 📚 What I Learned from This Project

* Creating Telegram bots with Python
* Handling commands and user input
* Working with external APIs
* Using virtual environments
* Managing a project with Git and GitHub

---

## 🌱 Future Improvements

* Inline keyboard buttons
* Password generator command
* Cyber security tools (whois, hash)
* Database integration
* Deploy the bot for 24/7 uptime

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## ✨ Author

**Jaber Ahmed**
Learning Python & Automation 🚀

```
