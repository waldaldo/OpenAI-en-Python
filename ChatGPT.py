import openai
import config

openai.api_key = config.chatgpt

while True:

    pregunta = input('\nCual es tu pregunta?: ')

    if pregunta == exit:
        break

    consulta = openai.Completion.create(engine = "text-davinci-003",
                                    prompt = pregunta,
                                    max_tokens = 2048 )

    print(consulta.choices[0].text)

    