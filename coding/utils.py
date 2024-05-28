from openai import OpenAI
import pyflakes.api
import pyflakes.reporter
import sys
import io

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
    for word in yes_answer:
        if word in gpt_answer:
            return True

    for word in no_answer:
        if word in gpt_answer:
            return False

    return False


def check_python_code(code):
    error_stream = io.StringIO()
    original_stderr = sys.stderr
    sys.stderr = error_stream

    try:
        pyflakes.api.check(code, filename='input_code')
    finally:
        sys.stderr = original_stderr

    return error_stream.getvalue()


def gpt_help(user_answer):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": f"Explain in one paragraph about the vulnerabilities in the transmitted code"},
            {"role": "user", "content": f"{user_answer}"}
        ]
    )

    return completion.choices[0].message.content