from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Приветствие
def start(update, context):
    update.message.reply_text("Привет! Я бот проекта BLAGO. Чтобы начать, пожалуйста, зарегистрируйтесь командой /register.")

# Регистрация
def register(update, context):
    update.message.reply_text("Спасибо за регистрацию! Теперь вы можете присоединиться к сообществу командой /join_community.")

# Вступить в сообщество
def join_community(update, context):
    update.message.reply_text("Вы успешно присоединились к сообществу BLAGO!")

# Создание потребностей
def create_need(update, context):
    update.message.reply_text("Опишите свою потребность.")

# Создание благ
def create_benefit(update, context):
    update.message.reply_text("Опишите предлагаемое благо.")

# Обработка текстовых сообщений пользователя
def echo(update, context):
    update.message.reply_text(update.message.text)

# Обработка неизвестных команд
def unknown(update, context):
    update.message.reply_text("Извините, я не понимаю эту команду.")

def main():
    # Инициализация токена вашего бота
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Добавление обработчиков команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("join_community", join_community))
    dp.add_handler(CommandHandler("create_need", create_need))
    dp.add_handler(CommandHandler("create_benefit", create_benefit))

    # Добавление обработчика для текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Добавление обработчика для неизвестных команд
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
