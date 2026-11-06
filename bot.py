import os
import telebot
from flask import Flask
from threading import Thread

# आपका बॉट टोकन यहाँ ऑटोमैटिक सेट है
TOKEN = "9089114527:AAEfiWh03aIxTWqToBOHzUCesa5VIrmBjQM"
bot = telebot.TeleBot(TOKEN)

# जब भी कोई आपके बॉट को मैसेज करेगा, यह ऑटो-रिप्लाई जाएगा
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    auto_reply_text = (
        "नमस्ते! 👋\n\n"
        "आपका मैसेज मिल गया है। फ़िलहाल मैं किसी काम में व्यस्त हूँ। "
        "जैसे ही मैं फ्री होता हूँ, आपसे खुद संपर्क करूँगा। तब तक हमारे साथ जुड़े रहने के लिए धन्यवाद! 🙏"
    )
    bot.reply_to(message, auto_reply_text)

# 24/7 चालू रखने के लिए सर्वर
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
