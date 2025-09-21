from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv(8205237649:)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"Привет, {user.first_name}! Я твой диспетчерский бот 🚜")

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Пока отчётов нет, но скоро будут 😉")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report))
    print("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
