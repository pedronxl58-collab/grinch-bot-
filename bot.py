import asyncio
import logging
import random
from datetime import datetime, timezone, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações Oficiais
TOKEN_TELEGRAM = "8806505554:AAGgHL-K5MG4N3K0wuATRSG8CaN6qWJZp6Y"
CHAT_ID_GRUPO = "@GrinchSolanaPortal"
X_USERNAME = "GrinchCoin__"

DATA_LANCAMENTO = datetime(2026, 12, 15, 0, 0, 0, tzinfo=timezone(timedelta(hours=-3)))

def calcular_dias_faltantes():
    agora = datetime.now(timezone(timedelta(hours=-3)))
    diferenca = DATA_LANCAMENTO - agora
    dias = diferenca.days
    if dias < 0:
        return 0
    return dias

async def envio_automatico_grinch(context: ContextTypes.DEFAULT_TYPE):
    dias = calcular_dias_faltantes()
    
    atualizacoes_grinch = [
        (
            f"🎄 **$GRINCH STATUS & MARKETING UPDATE** 🟢\n\n"
            f"⏳ Only **{dias} days left** until the official launch on Pump.fun!\n"
            f"• Follow our X profile: [X (Twitter)](https://x.com/{X_USERNAME})\n"
            "• Social media campaigns are expanding globally.\n"
            "💬 *Join the portal and invite your friends!*\n\n"
            "-----------------------------------\n"
            f"🎄 **STATUS E MARKETING DO $GRINCH** 🟢\n\n"
            f"⏳ Faltam apenas **{dias} dias** para o lançamento oficial na Pump.fun!\n"
            f"• Segue o nosso perfil no X: [X (Twitter)](https://x.com/{X_USERNAME})\n"
            "• As campanhas nas redes sociais estão a expandir-se globalmente.\n"
            "💬 *Junta-te ao portal e convida os teus amigos!*"
        ),
        (
            f"🎁 **$GRINCH COMMUNITY INTEL & SOCIALS** 🚀\n\n"
            f"Countdown: **{dias} days** remaining!\n"
            f"• Check out our latest posts on [X (Twitter)](https://x.com/{X_USERNAME}) and drop a like/retweet!\n"
            "• Get your Solana (Phantom) wallets ready for the ultimate holiday pump.\n"
            "🟢 *Let's take over Solana together!*\n\n"
            "-----------------------------------\n"
            f"🎁 **INFORMAÇÕES E REDES SOCIAIS $GRINCH** 🚀\n\n"
            f"Contagem decrescente: **{dias} dias** restantes!\n"
            f"• Confere os nossos novos posts no [X (Twitter)](https://x.com/{X_USERNAME}) e deixa o teu like/retweet!\n"
            "• Preparem as vossas carteiras Solana (Phantom) para o pump de Natal.\n"
            "🟢 *Vamos dominar a Solana juntos!*"
        )
    ]
    
    mensagem_escolhida = random.choice(atualizacoes_grinch)
    
    try:
        await context.bot.send_message(chat_id=CHAT_ID_GRUPO, text=mensagem_escolhida, parse_mode="Markdown")
        logger.info("Update completo do Grinch enviado com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao enviar update automático: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    dias = calcular_dias_faltantes()
    await update.message.reply_text(
        f"🎄 **Welcome to the Grinch Cave, {user.first_name}!** 🟢\n\n"
        f"⏳ **{dias} days left** until the **$GRINCH** launch! 🚀\n\n"
        "• /countdown - Days left until launch\n"
        "• /news - Latest project news & socials\n"
        "• /contract - View Contract Address\n"
        "• /links - Official socials\n\n"
        "-----------------------------------\n"
        f"🎄 **Bem-vindo à Caverna do Grinch, {user.first_name}!** 🟢\n\n"
        f"⏳ **{dias} dias restantes** para o lançamento do **$GRINCH**! 🚀\n\n"
        "• /countdown - Dias para o lançamento\n"
        "• /news - Últimas notícias e redes sociais\n"
        "• /contract - Ver Contrato\n"
        "• /links - Redes sociais",
        parse_mode="Markdown"
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dias = calcular_dias_faltantes()
    await update.message.reply_text(
        f"📰 **Latest $GRINCH News & Updates:**\n\n"
        f"1️⃣ **Launch:** December 15th, 2026 on Pump.fun ({dias} days left).\n"
        f"2️⃣ **Socials:** Active campaigns on [X (Twitter)](https://x.com/{X_USERNAME}).\n"
        "3️⃣ **Community:** 24/7 portal monitoring and automated updates.\n\n"
        "-----------------------------------\n"
        f"📰 **Últimas Notícias e Atualizações do $GRINCH:**\n\n"
        f"1️⃣ **Lançamento:** 15 de Dezembro de 2026 na Pump.fun (Faltam {dias} dias).\n"
        f"2️⃣ **Redes Sociais:** Campanhas ativas no [X (Twitter)](https://x.com/{X_USERNAME}).\n"
        "3️⃣ **Comunidade:** Monitorização 24/7 e atualizações automáticas no portal.",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

async def countdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dias = calcular_dias_faltantes()
    await update.message.reply_text(
        f"⏳ Only **{dias} days left** until the official $GRINCH launch on Pump.fun! 🟢🎄\n\n"
        f"⏳ Faltam apenas **{dias} dias** para o lançamento oficial do $GRINCH na Pump.fun! 🟢🎄",
        parse_mode="Markdown"
    )

async def contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 **CA:** `The official contract address will be pinned here on December 15th!`\n\n"
        "📋 **CA:** `O contrato oficial será fixado aqui no dia 15 de Dezembro!`",
        parse_mode="Markdown"
    )

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 **Official Links / Links Oficiais:**\n\n"
        f"• 🕊️ **X (Twitter):** https://x.com/{X_USERNAME}\n"
        "• 💬 **Telegram Portal:** https://t.me/GrinchSolanaPortal\n"
        "• 📍 **Pump.fun:** (Coming soon / Brevemente)",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

async def main_async():
    app = Application.builder().token(TOKEN_TELEGRAM).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("countdown", countdown))
    app.add_handler(CommandHandler("contract", contract))
    app.add_handler(CommandHandler("links", links))

    if app.job_queue:
        app.job_queue.run_repeating(envio_automatico_grinch, interval=21600, first=15)

    logger.info("🤖 Bot do Grinch com links clicáveis do X atualizados...")
    
    async with app:
        await app.start()
        await app.updater.start_polling()
        await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main_async())
    except (KeyboardInterrupt, SystemExit):
        pass
