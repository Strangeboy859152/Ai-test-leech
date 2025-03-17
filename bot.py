touch bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# बॉट टोकन
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('नमस्ते! मैं एक लीक बॉट हूँ। टेक्स्ट फ़ाइल भेजें।')

def handle_text(update: Update, context: CallbackContext) -> None:
    # यहाँ पर आप टेक्स्ट फ़ाइल को प्रोसेस कर सकते हैं
    text_file = update.message.document.get_file()
    text_file.download('downloaded_file.txt')
    update.message.reply_text('फ़ाइल डाउनलोड हो गई है!')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("text/plain"), handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
