# -*- coding: utf-8 -*-
import gradio as gr
from threading import Thread
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

device = "cuda"
model_id = "D:/DataSet/Qwen2.5-Coder-1.5B-Instruct/"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)


def question_answer(query):
    message = [{"role": "user", "content": query}]
    conversion = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)
    encoding = tokenizer(conversion, return_tensors="pt").to(device)
    streamer = TextIteratorStreamer(tokenizer)
    generation_kwargs = dict(encoding, streamer=streamer, max_new_tokens=1000, do_sample=True, temperature=0.2)
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    generate_text = ''
    for new_text in streamer:
        output = new_text.replace(conversion, '')
        if output:
            generate_text += output
            yield generate_text


demo = gr.Interface(
    fn=question_answer,
    inputs=gr.Textbox(lines=3, placeholder="your question...", label="Question"),
    outputs="text",
)

demo.launch(server_name="127.0.0.1", server_port=50079, share=True)
