import io
import os
import openai
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)
os.environ['OPENAI_API_KEY'] = "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"
class Meal :
    def create_meals(ingredients, kcal=2000):
        from openai import OpenAI
        
        client = OpenAI()
        prompt = f'''Create a healthy daily meal plan for breakfast, lunch and dinner based on
        the following ingredients {ingredients}.
        Explain each recipe.
        The total daily intake of kcal should be below {kcal}.
        Assign a suggestive and concise title to each meal.
        Your answer should end with 'Titles: ' and the title of each recipe.'''
        foods = ingredients.split()
        #     print(prompt)
        messages = [
            {'role': 'system', 'content': 'You are a talented cook.'},
            {'role': 'user', 'content': prompt}
        ]
        response =  client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=1,
            max_tokens = 1024,
            n=1
        )
        return response.choices[0].message.content

    def create_and_save_image(title, model='dall-e-3', extra=''):
        from openai import OpenAI
        client = OpenAI()

        import requests
        import shutil

        image_prompt = f'{title}, {extra}, high quality food photography'
    #     print(image_prompt)

        # making the API call
        response = client.images.generate(
            model=model,
            prompt=image_prompt,
            n=1,
            size='1024x1024'
        )

        image_url = response.data[0].url
        print()
        print(image_url)

        image_resource = requests.get(image_url, stream=True)
        print(image_resource.status_code)

        image_filename = f'{title}.png'
        if image_resource.status_code == 200:
            with open(image_filename, 'wb') as f:
                shutil.copyfileobj(image_resource.raw, f)
                return image_filename
        else:
            print('Error accessing the image!')
            return False
      


