from telegram import Update
from telegram.ext import  Updater, CommandHandler, MessageHandler, CallbackContext
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Send me a message in English, and I'll translate it to French.")

# Message handler for translation
def translate(update: Update, context: CallbackContext) -> None:
    text_to_translate = update.message.text
    translated_text = translator.translate(text_to_translate, src='en', dest='fr').text
    update.message.reply_text(translated_text)

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("8195298605:AAE4DdRZLhNJyCOAigpzOB5A0FAyEkPG74I") 

    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(None, translate))
    

    # Start the bot
    updater.start_polling()
    updater.idle()


