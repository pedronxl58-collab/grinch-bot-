import logging
import random
from datetime import datetime, timezone, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações Oficiais do Bot $GRINCH
TOKEN_TELEGRAM = "8806505554:AAH1coxKkLHgXChDyaggmETslL1Tf"
CHAT_ID_GRUPO = "@GrinchSolanaPortal"

# Data oficial de lançamento: 15 de Dezembro de 2026
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
            f"🎄 **$GRINCH STATUS UPDATE** 🟢\n\n"
            f"⏳ Faltam **{dias} dias** para o lançamento oficial na Pump.fun!\n"
            "• O nosso portal no Telegram não para de crescer.\n"
            "• O Grinch já está a tramar as melhores surpresas para o dia do lançamento.\n"
            "💬 *Convidem os vossos amigos para a caverna antes que o Grinch feche a porta!*"
        ),
        (
            f"🎁 **$GRINCH COMMUNITY INTEL** 🚀\n\n"
            f"Contagem decrescente: **{dias} dias** restantes!\n"
            "• Os perfis oficiais no X (Twitter) e Instagram estão ativos com os preparativos.\n"
            "• Preparem as vossas carteiras Solana (Phantom) para o maior choque natalício da rede.\n"
            "🟢 *Ninguém vai roubar este pump de vocês!*"
        ),
        (
            f"🚨 **AVISO DO GRINCH** 🟢\n\n"
            f"Faltam apenas **{dias} dias** para o grande dia (15 de Dezembro)!\n"
            "• O contrato oficial (CA) só será revelado no momento exato do lançamento para garantir justiça para todos.\n"
            "• Fiquem atentos a este canal para não perderem nenhuma novidade exclusiva do $GRINCH."
        )
    ]
    
    mensagem_escolhida = random.choice(atualizacoes_grinch)
    
    try:
        await context.bot.send_message(chat_id=CHAT_ID_GRUPO, text=mensagem_escolhida, parse_mode="Markdown")
        logger.info("Update exclusivo do Grinch enviado com sucesso para o grupo!")
    except Exception as e:
        logger.error(f"Erro ao enviar update automático do Grinch: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    dias = calcular_dias_faltantes()
    await update.message.reply_text(
        f"🎄 **Welcome to the Grinch Cave, {user.first_name}!** 🟢\n\n"
        f"Faltam **{dias} dias** para o lançamento do **$GRINCH**! 🚀\n\n"
        "• /countdown - Dias restantes para o lançamento\n"
        "• /news - Últimas novidades do $GRINCH\n"
        "• /contract - Ver Contrato\n"
        "• /links - Redes sociais oficiais",
        parse_mode="Markdown"
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dias = calcular_dias_faltantes()
    await update.message.reply_text(
        f"📰 **Últimas Notícias do $GRINCH:**\n\n"
        f"1️⃣ **Lançamento:** Marcado para 15 de Dezembro de 2026 na Pump.fun (Faltam {dias} dias).\n"
        "2️⃣ **Redes Sociais:** X e canais ativos com branding oficial e focado no público global.\n"
        "3️⃣ **Comunidade:** O portal do Telegram está aberto 24/7 com este bot de monitorização ativo.\n\n"
        "🟢 *O Grinch está pronto para dominar a Solana!*",
        parse_mode="Markdown"
    )

async def countdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dias = calcular_dias_faltantes()
    await update.message.reply_text(f"⏳ Faltam **{dias} dias** para o lançamento oficial do $GRINCH na Pump.fun! 🟢🎄", parse_mode="Markdown")

async def contract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 **CA:** `O contrato oficial será fixado aqui no dia 15 de Dezembro!`", parse_mode="Markdown")

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌐 **X (Twitter):** @GrinchSolana \n💬 **Telegram Portal:** t.me/GrinchSolanaPortal", parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN_TELEGRAM).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("countdown", countdown))
    app.add_handler(CommandHandler("contract", contract))
    app.add_handler(CommandHandler("links", links))

    if app.job_queue:
        app.job_queue.run_repeating(envio_automatico_grinch, interval=21600, first=15)

    logger.info("🤖 Bot exclusivo do Grinch a rodar perfeitamente...")
    app.run_polling()

if __name__ == '__main__':
    main()
