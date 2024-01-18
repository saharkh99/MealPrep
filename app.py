
import gradio as gr
import os
from generate_recepie import Meal

def create_meals(foods):
    output = Meal.create_meals(foods)
    titles = output.splitlines()[-3:]
    image_filename = Meal.create_and_save_image(titles[0], extra='white background')
    print(image_filename)
    return output, image_filename

with gr.Blocks() as demo:
    
    txt = gr.Textbox(label="enter ingredients", lines=2)
    foods = 'broccoli, chicken, fish, vegetables, cabbage, eggs, olive oil'
    # txt_3 = gr.Textbox(value="", label="Output")
    btn = gr.Button(value="Submit")
    outputs = [
    gr.Textbox(value="", label="recepie"),
    gr.Image(type="filepath", label="image of recepie"),
    ]
    btn.click(create_meals, inputs=[txt], outputs=outputs)


if __name__ == "__main__":
    demo.launch()