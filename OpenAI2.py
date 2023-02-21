import openai
import time
import sys, time  # Agregamos los módulos sys y time.
import config

openai.api_key = config.davinci

prompt = input("\n\n * Que quieres crear hoy? \n = ")

response = None

while not response:                 # Mientras no hayamos obtenido respuesta...  
    response = openai.Image.create( # ...intentamos obtenerla.  
        prompt=prompt,  
        n=1,  
        size='1024x1024'  
    )    

image_url = response['data'][0]['url']  # Obtenemos la URL de la imagen generada.    

print(f'\nURL de la imagen generada: {image_url}')