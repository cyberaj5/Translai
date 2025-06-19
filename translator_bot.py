from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Initialize translator
translator = Translator()

# Bot token from BotFather
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    welcome_text = """
    Welcome to the French-English Translator Bot!
    
    Simply send me text in either English or French and I'll translate it to the other language.
    
    Commands:
    /start - Show this welcome message
    /help - Show help information
    """
    update.message.reply_text(welcome_text)

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a help message when the command /help is issued."""
    help_text = """
    How to use this bot:
    
    • Send text in English to get French translation
    • Send text in French to get English translation
    
    The bot automatically detects the input language.
    """
    update.message.reply_text(help_text)

def translate_text(update: Update, context: CallbackContext) -> None:
    """Translate the user's message."""
    text = update.message.text
    
    try:
        # Detect language
        detected = translator.detect(text)
        
        # Determine target language
        if detected.lang == 'fr':
            target = 'en'
            target_name = 'English'
        else:
            target = 'fr'
            target_name = 'French'
        
        # Translate text
        translation = translator.translate(text, dest=target)
        
        # Send translation back to user
        response = f"Translation to {target_name}:\n\n{translation.text}"
        update.message.reply_text(response)
        
    except Exception as e:
        update.message.reply_text(f"Sorry, I couldn't translate that. Error: {str(e)}")

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non-command messages - translate the message
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()