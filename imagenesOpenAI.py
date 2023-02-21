import openai
from halo import Halo
import config

openai.api_key = config.davinci

prompt = input("\n\n * Que quieres crear hoy? \n = ")

spinner = Halo(text='Generando tu imagen, dame un momento  ', spinner='squareCorners')
spinner.start() 

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024'
)
image_url = response['data'][0]['url']

spinner.stop() 

print(f'\nURL de la imagen generada: \n {image_url}')