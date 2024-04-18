from openai import OpenAI

client = OpenAI()


def ask_chatgpt(context, user_answer):
    yes_answer = ["Да", "ДА"]
    no_answer = ["Нет", "НЕТ"]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": f"{context}"},
            {"role": "user", "content": f"{user_answer}"}
        ]
    )
    gpt_answer = completion.choices[0].message.content
    print(gpt_answer)
    for word in yes_answer:
        if word in gpt_answer:
            return True

    for word in no_answer:
        if word in gpt_answer:
            return False

    return False
