from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model_id = "D:/DataSet/Qwen2.5-Coder-1.5B-Instruct/"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)
message = [{"role": "user", "content": "介绍一下Python"}]
conversion = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)
print(conversion)
encoding = tokenizer(conversion, return_tensors="pt").to("cuda")
streamer = TextIteratorStreamer(tokenizer)
# Run the generation in a separate thread, so that we can fetch the generated text in a non-blocking way.
generation_kwargs = dict(encoding, streamer=streamer, max_new_tokens=2048, do_sample=True, temperature=0.2)
thread = Thread(target=model.generate, kwargs=generation_kwargs)
thread.start()

generated_text = ""
for new_text in streamer:
    output = new_text.replace(conversion, '')
    if output:
        print(output.replace("<|im_end|>", ""), end='')
