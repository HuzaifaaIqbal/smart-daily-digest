# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(
    # api_key=os.getenv("OPENAI_API_KEY"),
    # base_url=os.getenv("OPENAI_BASE_URL")
# )

# def summarize_text(text):
    # response = client.chat.completions.create(
        # model="anthropic/claude-sonnet-4",  # ✅ OpenRouter format
        # messages=[
            # {"role": "user", "content": f"Summarize the following:\n\n{text}"}
        # ],
        # temperature=0.7,
        # max_tokens=300,
    # )
    # return response.choices[0].message.content.strip()

# if __name__ == "__main__":
    # sample_text = """
    # Artificial intelligence (AI) is intelligence demonstrated by machines,
    # unlike the natural intelligence displayed by humans and animals.
    # Leading AI textbooks define the field as the study of "intelligent agents":
    # any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
    # """
    # print("Original Text:\n", sample_text)
    # print("\nSummary:\n", summarize_text(sample_text))
    
    
    
import feedparser
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def send_email(summary):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = os.getenv("EMAIL_TO")  # can be same as sender
    app_password = os.getenv("EMAIL_PASSWORD")

    subject = "🧠 Daily Tech Summary"
    body = f"Here is your smart daily digest:\n\n{summary}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
        

def fetch_top_tech_news(feed_url, limit=5):
    feed = feedparser.parse(feed_url)
    top_entries = feed.entries[:limit]
    
    news_items = []
    for entry in top_entries:
        title = entry.title
        summary = entry.summary if hasattr(entry, 'summary') else ''
        news_items.append(f"Title: {title}\nSummary: {summary}\n")

    return "\n".join(news_items)

def summarize_text(text):
    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes tech news in a concise, clear, and professional format."},
            {"role": "user", "content": f"Summarize the following tech news:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=500
    )
    # return response.choices[0].message.content.strip()
    
    if isinstance(response, str):
        return response.strip()

    # Otherwise, fallback to normal structure
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Fetching latest tech news...")
    tech_news = fetch_top_tech_news("https://techcrunch.com/feed/")
    print("\nOriginal News:\n", tech_news)

    print("\nGenerating Summary...")
    summary = summarize_text(tech_news)
    print("\n✅ Daily Tech Summary:\n", summary)
    
    send_email(summary)


    # Schedule the task
    schedule.every().day.at("09:00").do(run_daily_summary)

    print("⏰ Scheduler started. Waiting to run the task daily at 09:00 AM...")

    while True:
        schedule.run_pending()
        time.sleep(60)