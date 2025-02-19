from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_id = "D:/DataSet/Qwen2.5-Coder-0.5B-Instruct/"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)
message = [{"role": "user", "content": "沈阳一共有几条地铁？"}]
conversion = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)
print(conversion)
encoding = tokenizer(conversion, return_tensors="pt").to("cuda")
streamer = TextStreamer(tokenizer)
model.generate(**encoding, max_new_tokens=500, temperature=0.2, do_sample=True, streamer=streamer, pad_token_id=tokenizer.eos_token_id)


