import telebot

bot = telebot.TeleBot('6601677282:AAHW_VdZfziYFlmtqAXY1WiO_E7fMLJs56E')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет это Крипто бот, чем могу помочь?', parse_mode='Markdown')


@bot.message_handler(commands=['com1'])
def main(message):
    bot.send_message(message.chat.id,'*Держи*[Видео](https:// www.youtube.com / watch?v = VibTITVSHIw)', parse_mode='Markdown')

@bot.message_handler(commands=['com2'])
def main(message):
    bot.send_message(message.chat.id,
                     '_Криптовалюта — средство платежа, которое существует только в интернете. У нее нет бумажного выражения, и ее ценность не зависит от государства.Обычно, чтобы перевести деньги от одного человека другому, нужен посредник — банк. С криптовалютой по-другому: в обмене банк не участвует. Криптовалюта построена на системе блокчейн — цепочке информационных блоков. Их используют для перевода цифровых денег от человека к человеку без посредника.В 2009 году появилась первая цифровая монета — биткоин, с тех пор количество криптовалют растет.Рассказываем, что такое криптовалюта, как она устроена, от чего зависит ее цена, как ее получить и использовать_',
                     parse_mode='Markdown')


bot.infinity_polling()