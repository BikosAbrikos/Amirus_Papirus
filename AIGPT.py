import g4f
# Считываем текст из файла
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Загрузка текста
text_content = load_text_from_file('правила _проживания_в_интернате.txt')
# Добавляем текст в правила для контекста
rules = [
    {"role": "system", "content": f"Вот информация, на основе которой ты будешь отвечать на вопросы: {text_content}"}
]
chat_history = []
limits = 'One message exceeds the 1000chars per message limit.'
def get_text(user_input):
    global chat_history
    if len(chat_history) > 5:
        chat_history.pop(0)

    # Добавляем новое сообщение от пользователя в историю
    chat_history.append({"role": "user", "content": user_input})

    # Отправляем запрос с полной историей диалога
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = rules + chat_history,  # Передаем всю историю
        stream=True,
    )

    # Собираем ответ в виде строки
    bot_response = ''
    for i in response:
        if isinstance(i, str):
            bot_response += i
    if limits in bot_response or bot_response == '' or type(bot_response) != str:
        get_text(user_input)
    else:
        chat_history.append({"role": "assistant", "content": bot_response})
        return bot_response