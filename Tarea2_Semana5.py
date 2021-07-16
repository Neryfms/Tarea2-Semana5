import logging
from typing import Text

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, message
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [

            InlineKeyboardButton("Consultar la tasa de cambio de el dolar.",
            callback_data='el dolar en HN es 1USD=23HNL. Mas en: g.co/finance/USD-HNL'),
        ],
        [
            InlineKeyboardButton("Consultar la tasa de cambio de el euro.", 
            callback_data='el euro en HN es 1EUR=28HNL. Mas en: g.co/finance/EUR-HNL'),
            
        ],
        [   
            InlineKeyboardButton("Consultar el precio de el oro.", 
            callback_data='el oro en HN es 1KG=1,409,987.60HNL Mas en: goldprice.org/es')
        ],
        [   
            InlineKeyboardButton("Consultar el precio de el café.", 
            callback_data='el café en HN es 1KG=3,37USD. Mas en: cutt.ly/zmJZgsu')
        ],
         [   
            InlineKeyboardButton("Consultar el precio de la plata.", 
            callback_data='la plata en HN es 1KG=20,274.70HNL. Mas en: silverprice.org/es')
        ],
         [   
            InlineKeyboardButton("Consultar el precio de la gasolina.", 
            callback_data='la gasolina en HN es 1 Litro=26.81HNL Mas en: cutt.ly/LmJX829')
        ],
         [   
            InlineKeyboardButton("Consultar el precio de el diesel.", 
            callback_data='el diesel en HN es 1 Litro=21.83HNL Mas en: cutt.ly/CmJCpVe ')
        ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    user = update.effective_user
    update.message.reply_markdown_v2(
    fr'¡Hola {user.mention_markdown_v2()}\!, ¿Deseas realizar una consulta?',
        
    reply_markup=reply_markup)
    
    


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer("¡Estoy procesando la opcion seleccionada!. Por favor, espere...")
    query.edit_message_text(text=f"El valor de {query.data}")
    
 

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start para realizar otra consulta")
    
    


def main() -> None:
    updater = Updater("1780488021:AAHOzUQopOX_GzqrKeTMdLY75s_n69zNlxM")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
    