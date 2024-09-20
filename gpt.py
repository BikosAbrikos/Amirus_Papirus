import openai
API_key = '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'
# Установите ваш API ключ
openai.api_key = API_key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3",  # Можно использовать "gpt-3.5-turbo" для другой версии
        messages=[{"role": "system", "content": "Ты - помощник."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7,  # Контролирует уровень креативности ответов
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Привет! Чем могу помочь?")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "выход":
            print("До свидания!")
            break
        response = chat_with_gpt(user_input)
        print("Бот:", response)
