Smart Daily Digest

A Python-based automation script that fetches the latest tech news from RSS feeds, summarizes it using an AI model (Claude Sonnet via OpenRouter), and emails the summary to you every day.

🚀 Features

Fetches top 5 articles from TechCrunch.

Summarizes long content using Claude Sonnet 4 (Anthropic) via OpenRouter.

Sends a clean summary to your email using Gmail SMTP.

Easy to configure and deploy.

🔧 Setup

Clone the Repository

git clone https://github.com/HuzaifaaIqbal/smart-daily-digest.git
cd smart-daily-digest

Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate  # Windows

Install Dependencies

pip install -r requirements.txt

Add Environment Variables
Create a .env file in the root directory:

OPENAI_API_KEY=your_openrouter_key
OPENAI_BASE_URL=https://openrouter.ai/api
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_TO=receiver_email@gmail.com

▶️ Run the Script

python summarizer_test.py

☁️ Deploy on PythonAnywhere

Create a new scheduled task.

Point it to summarizer_test.py using the full path.

Set it to run daily (or however often you'd like).

📧 Sample Email Output

Subject: 🧠 Daily Tech Summary

Here is your smart daily digest:

- OpenAI releases GPT-4.5 with better reasoning capabilities...
- Apple announces major updates to iOS 19...
- ...

🧠 Tech Stack

Python 3

OpenRouter API (Claude Sonnet 4)

feedparser

smtplib

Gmail SMTP

dotenv

💡 Future Ideas

Add multi-feed support.

Toggle between daily and weekly digests.

Add HTML email formatting.

Add web dashboard to manage preferences.

📄 License

This project is open-source and available under the MIT License.
