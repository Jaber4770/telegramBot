from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = "your bot token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি তোমার Practice Bot")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Bot শুরু\n"
        "/python - Python resource\n"
        "/jack - make by jack sargey\n"
        "/help - Help menu"
    )

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐍 Python শেখার জন্য:\nhttps://docs.python.org/3/"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("python", python))

print("🤖 Bot is running...")
app.run_polling()
