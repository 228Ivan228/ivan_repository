import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler
from math import asin, atan, acos, cos, sin, tan, radians, degrees
def start(update: Update, context: CallbackContext):
        update.message.reply_text(f"Привіт,{update.effective_user.first_name}.Цей Бот обчислює такі тригонометричні задачі,\n як:арктангенс, арксинус, арккосинус, синус, тангенс, косинус, а також переводить радіани в градуси, градуси в радіани.")

def help(update: Update, context:CallbackContext):
    update.message.reply_text(f"Обчислення(/do_operation)\nСпочатку вводите /do_operation,далі вводите операцію, далі вводите одиниці вимірювання, і число.\n"
                              f"Конвертування(/unit)\nКомандою /unit ви можете перевести радіани в градуси, та навпаки.\nДля цього спочатку введіть /unit потім число і одиниці вимірювання(rad - радіани, deg - градуси).\n"
                              f"Oplist(/oplist)\nУ цій команді вказано усі операції які цей бот спроможний виконати.\n"
                              f"Нюанси\n"
                              f"Коли ви в /unit вводите 30 deg, то 30 в данному випадку, це радіани, а 30 rad, то 30 це градуси.\n"
                              f"Одиниці вимірювання\nОдин радіан = 57,296 градусів.\nОдин градус = 0.017453 радіан.  ")


def oplist(update: Update, context: CallbackContext):
    update.message.reply_text("as_in - арксинус; at_an - арктангенс; ac_os - арккосинус;\n"
                              "si_n - синус; ta_n - тангенс; co_s - косинус;\n/unit - конвертування радіан у градуси, та градуси у радіани")


def do_operation(uptade: Update, context: CallbackContext):
    if len(context.args) != 3:
        uptade.message.reply_text("Помилка, не правильна кількість аргументів")
        return
    operation, units ,number = context.args
    try:
        if units == "deg":
            number = radian(number)
        if operation == "as_in":
            result = as_in(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
        elif operation == "at_an":
            result = at_an(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
        elif operation == "ac_os":
            result = ac_os(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
        elif operation == "si_n":
            result = si_n(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
        elif operation == "ta_n":
            result = ta_n(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
        elif operation == "co_s":
            result = co_s(number)
            uptade.message.reply_text(f"Ось ваш результат:{result}")
    except(ValueError):
        return uptade.message.reply_text("Виникла помилка")




def as_in(number):
    number = float(number)
    result = asin(number)
    return result


def at_an(number):
    number = float(number)
    result = atan(number)
    return result

def ac_os(number):
    number = float(number)
    result = acos(number)
    return result

def si_n(number):
    number = float(number)
    result = sin(number)
    return result


def ta_n(number):
    number = float(number)
    result = tan(number)
    return result

def co_s(number):
    number = float(number)
    result = cos(number)
    return result

def radian(number):
    number = float(number)
    result = radians(number)
    return result

def degree(number):
    number = float(number)
    result = degrees(number)
    return result

def unit(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        update.message.reply_text("Помилка переводу, не достатньо аргументів")
        return
    number, unit = context.args
    try:
        if unit == "rad":
            unit = radian(number)
            update.message.reply_text(f"Результат:{unit}")
        elif unit == "deg":
            unit = degree(number)
            update.message.reply_text(f"Результат:{unit}")
    except(ValueError):
        update.message.reply_text(f"Помилка значеннь")


def main() -> None:
        """Run bot."""
        # Create the Updater and pass it your bot's token.
        updater = Updater("5609418659:AAGKlJJfPsO-g7UkpJyAZKcq3mvKls7pQhU")

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        # on different commands - answer in Telegram
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help))
        dispatcher.add_handler(CommandHandler("do_operation", do_operation))
        dispatcher.add_handler(CommandHandler("oplist", oplist))
        dispatcher.add_handler(CommandHandler("unit", unit))
        # Start the Bot
        updater.start_polling()

        # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
        # SIGABRT. This should be used most of the time, since start_polling() is
        # non-blocking and will stop the bot gracefully.
        updater.idle()


if __name__ == "main":
    main()