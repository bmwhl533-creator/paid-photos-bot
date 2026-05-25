import telebot
from telebot.types import LabeledPrice
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "أهلا! ابعتلي صورة باش نخليها مدفوعة بالـ Stars ⭐")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    prices = [LabeledPrice(label="الصورة", amount=50)]
    bot.send_invoice(
        chat_id=message.chat.id,
        title="صورة مدفوعة",
        description="ادفع بالـ Stars باش تشوف الصورة",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="paid_photo",
        payload="photo123"
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def pre_checkout(query):
    bot.answer_pre_checkout_query(query.id, ok=True)

print("Bot is running...")
bot.polling()
