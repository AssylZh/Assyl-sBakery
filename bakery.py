import telebot
from telebot import types

token = '6245767547:AAGapGsWx-dE-TUXZNHsMky5w2OUcJCGiZo'
bot = telebot.TeleBot(token)


def handle_bakery_questions(message):
    question = message.text.lower()
    if 'what are your hours of operation?' in question:
        bot.reply_to(message, 'We are open from 7am to 9pm, seven days a week.')
    elif 'do you have gluten-free options?' in question:
        bot.reply_to(message, 'Yes, we offer a variety of gluten-free options. Please inquire at the front desk for more information.')
    elif 'what kinds of pastries do you have?' in question:
        bot.reply_to(message, 'We offer a variety of pastries including croissants, muffins, and danishes. Please check our website for the full selection.')
    elif 'what is the price of a cake?' in question:
        bot.reply_to(message, 'Our cake prices vary depending on the size and design. Please check our website or contact us for more information.')
    elif 'do you offer delivery?' in question:
        bot.reply_to(message, 'Yes, we offer delivery within the city limits for a small fee. Please inquire at the front desk for more information.')
    elif 'what is the cost of a membership?' in question:
        bot.reply_to(message,
                     'Our membership rates vary depending on the length of the membership and services included. Please check our website or contact us for more information.')
    else:
        bot.reply_to(message,
                     'I am sorry, I do not understand your question. Please try again with a different question.')


@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    keyboard.add(types.KeyboardButton('Manager`s contacts'), types.KeyboardButton('Ask a question'))
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}! Welcome to Assyl`s bakery', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
    question = message.text.lower()
    if message.text == 'Ask a question':
        bot.send_message(message.chat.id, 'What would you like to know about our bakery?')
        bot.register_next_step_handler(message, handle_bakery_questions)
    elif 'manager`s contacts' in question:
        bot.reply_to(message,'Here are the contacts of our manager: 77777777777(number)')
    elif 'what are your hours of operation?' in question:
        bot.reply_to(message, 'We are open from 7am to 9pm, seven days a week.')
    elif 'do you have gluten-free options?' in question:
        bot.reply_to(message, 'Yes, we offer a variety of gluten-free options. Please inquire at the front desk for more information.')
    elif 'what kinds of pastries do you have?' in question:
        bot.reply_to(message, 'We offer a variety of pastries including croissants, muffins, and danishes. Please check our website for the full selection.')
    elif 'what is the price of a cake?' in question:
        bot.reply_to(message, 'Our cake prices vary depending on the size and design. Please check our website or contact us for more information.')
    elif 'do you offer delivery?' in question:
        bot.reply_to(message, 'Yes, we offer delivery within the city limits for a small fee. Please inquire at the front desk for more information.')
    elif 'what is the cost of a membership?' in question:
        bot.reply_to(message,
                     'Our membership rates vary depending on the length of the membership and services included. Please check our website or contact us for more information.')
    else:
        bot.reply_to(message,
                     'I am sorry, I do not understand your question. Please try again with a different question.')

bot.polling(none_stop=True)
