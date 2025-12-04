# 🤖 WhatsApp AI Agent

A minimalistic AI-powered WhatsApp message-sending agent that understands natural language commands using Google's Gemini API and automates WhatsApp Web using Selenium.

## ✨ Features

- 🧠 Natural language understanding with Gemini API
- 📱 Automated WhatsApp Web interaction via Selenium
- 🔄 Interactive command loop
- ✅ Message confirmation before sending
- 💾 Session persistence (stays logged in)

## 🛠️ Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically managed by Selenium)
- Gemini API Key ([Get it here](https://aistudio.google.com/))

## 📦 Installation & Setup

### 1. Clone the Repository
```powershell
git clone https://github.com/RiyanBhargava/acm-whatsapp-ai-agent.git
cd acm-whatsapp-ai-agent
```

### 2. Create Virtual Environment
```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```powershell
.venv\Scripts\Activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

> **Note:** You should see `(.venv)` at the start of your prompt

### 4. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 5. Configure API Key

**Copy the example file:**
```powershell
copy .env.example .env
```

**Edit `.env` and add your Gemini API key:**
```env
GEMINI_API_KEY=your_actual_api_key_here
```

Get your API key from: https://makersuite.google.com/app/apikey

## 🚀 How to Run

### Start the Agent
```powershell
python main.py
```

### First Time Use
1. Chrome will open with WhatsApp Web
2. Scan the QR code with your phone to login
3. Once logged in, the session is saved (no need to scan again)

### Using the Agent

Type natural language commands:

**Example 1:**
```
You: send message to mom saying hi i am out

Processing command...

→ Contact: mom
→ Message: hi i am out

Send this message? (y/n): y
Searching for contact: mom
Sending message: hi i am out
✓ Message sent successfully!
```

**Example 2:**
```
You: tell John I'll meet him at 6 near the metro station
```

**Example 3:**
```
You: message Sarah that the meeting is postponed to tomorrow
```

### Exit the Agent
Type any of these:
- `quit`
- `exit`
- `q`
- Press `Ctrl+C`

## 📝 How It Works

1. **User Input**: You type a natural language command
2. **Gemini Processing**: The command is sent to Gemini API which extracts:
   - Contact name
   - Message content
3. **Confirmation**: The agent shows what it understood and asks for confirmation
4. **Selenium Automation**: If confirmed, Selenium automates WhatsApp Web to send the message

## 🎯 Command Format

The agent understands various natural language patterns:
- "send message to [contact] saying [message]"
- "tell [contact] [message]"
- "message [contact] that [message]"
- "send to [contact] saying [message]"

## ⚙️ Configuration

### Chrome Profile
The agent saves Chrome session data in `./chrome_profile` to keep you logged in.

### Customizing Behavior
Edit `gemini_parser.py` to modify the system prompt and change how commands are interpreted.

## 🔧 Troubleshooting

**"GEMINI_API_KEY not found"**
- Make sure you created the `.env` file with your API key

**WhatsApp won't load**
- Ensure you have a stable internet connection
- Try clearing the `chrome_profile` folder and logging in again

**Contact not found**
- Make sure the contact name matches exactly as saved in WhatsApp
- The contact must exist in your WhatsApp contact list

**ChromeDriver issues**
- Selenium should automatically download the correct ChromeDriver
- Make sure Chrome browser is installed and up to date

## 📂 Project Structure

```
ai-agent-whatsapp/
├── main.py                  # Main application entry point
├── gemini_parser.py         # Gemini API integration for NLP
├── whatsapp_automation.py   # Selenium automation for WhatsApp
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your actual API key (create this)
└── README.md              # This file
```

## 🛡️ Security Notes

- Never commit your `.env` file with the API key
- The `.gitignore` file excludes sensitive files automatically
- Chrome profile data is stored locally and not shared

## 📜 License

This project is free to use for personal and educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

---

**Made with ❤️ using Gemini API and Selenium**
