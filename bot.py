import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- 1. CONFIGURAÇÃO DO SERVIDOR WEB (Manter bot online 24/7) ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot $GRINCH está ativo e rodando 24/7! 🟢🎄"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# --- 2. CONFIGURAÇÃO DO BOT DO TELEGRAM ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Novo token atualizado do @BotFather
TOKEN_TELEGRAM = os.environ.get("TELEGRAM_TOKEN", "8806505554:AAEWyfPMDVSUjjSBUkAk7pTDYgqrgm05tew")
CONTRATO_SOLANA = "EM_BREVE"  # Atualiza quando lançar na Pump.fun
LINK_X = "https://x.com/GrinchCoin__"
LINK_TELEGRAM = "https://t.me/seu_grupo_aqui"

def get_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🌐 Twitter / X", url=LINK_X),
            InlineKeyboardButton("📢 Telegram", url=LINK_TELEGRAM)
        ],
        [
            InlineKeyboardButton("🚀 Comprar na Pump.fun", url="https://pump.fun")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    texto = (
        f"🎄 **Bem-vindo ao grupo oficial do $GRINCH, {user_name}!** 🟢\n\n"
        f"O Grinch chegou à rede Solana para dominar este Natal! 🎁💥\n\n"
        f"📌 **Lançamento Oficial:** 15 de Dezembro na Pump.fun\n"
        f"📝 **Contrato (CA):** `{CONTRATO_SOLANA}`\n\n"
        f"Usa os botões abaixo para acompanhar as novidades e participar dos raids!"
    )
    await update.message.reply_text(
        texto, 
        parse_mode="Markdown", 
        reply_markup=get_main_keyboard()
    )

async def contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        f"🟢 **CONTRATO OFICIAL ($GRINCH):**\n\n"
        f"`{CONTRATO_SOLANA}`\n\n"
        f"⚠️ *Confirma sempre o endereço oficial do contrato antes de realizar qualquer transação!*"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")

async def handle_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
        
    mensagem = update.message.text.lower()
    
    if any(p in mensagem for p in ["ca", "contrato", "contract"]):
        await contract(update, context)
        
    elif any(p in mensagem for p in ["quando lança", "lancamento", "lançamento", "launch"]):
        resposta = "🎄 O lançamento oficial do **$GRINCH** será no dia **15 de Dezembro** na Pump.fun! Fica atento às novidades no nosso X/Twitter! 🟢"
        await update.message.reply_text(resposta, parse_mode="Markdown")
        
    elif any(p in mensagem for p in ["site", "twitter", "x", "links", "social"]):
        await update.message.reply_text(
            "📌 **Links Oficiais do $GRINCH:**", 
            reply_markup=get_main_keyboard()
        )

def main():
    # Inicia o servidor Web em segundo plano
    keep_alive()
    
    # Inicia o Bot do Telegram
    bot_app = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("contract", contract))
    bot_app.add_handler(CommandHandler("ca", contract))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keywords))

    print("🤖 Bot $GRINCH em execução 24/7...")
    bot_app.run_polling()

if __name__ == "__main__":
    main()
