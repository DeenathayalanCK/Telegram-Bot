import Constants as keys
import Responses as R
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

print("Bot started...")

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Sollu da ipo unaku enna venum 😒...!!")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Help ella panna mudiyathu 💀 :)")

async def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    await update.message.reply_text(response)

async def error(update: object, context: CallbackContext):
    print(f"Update {update} caused error {context.error}")

def main():
    app = Application.builder().token(keys.API_KEY).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()



# import Constants as keys 
# from telegram.ext import *
# import Responses as R

# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters

# print("Bot started.....")

# def start_command(update, context ):
# 	update.message.reply_text("Type something to get started")
	
# def help_command(update, context ):
# 	update.message.reply_text("Still i am not trained for that so you may go and ask Google...!!:)")
# def handle_message(update, context):
# 	text = str(update.message.text).lower()
# 	response= R.sample_responses(text)
	
# 	update.message.reply_text(response)

# def error(update, context):
# 	print(f"update {update} caused error {context.error}")
	
# def main():
# 	updater = Updater(keys.API_KEY, use_context= True)
# 	dp = updater.dispatcher
# 	dp.add_handler(CommandHandler("start", start_command))
# 	dp.add_handler(CommandHandler("help", help_command))
# 	dp.add_handler(MessageHandler(Filters.text, handle_message))
# 	dp.add_error_handler(error)
# 	updater.start_polling()
# 	updater.idle()
	
# main()
	
	
