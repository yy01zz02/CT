from transformers import AutoModelForCausalLM, AutoTokenizer
import json

device = "cuda"

model_path = "D:/DataSet/Qwen2.5-Coder-0.5B-Instruct/"

model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_path)


messages = []


while True:
    prompt = input()

    messages.append({"role": "user", "content": prompt})

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    print(text)

    encoding = tokenizer(text, return_tensors="pt").to(device)

    # streamer = TextStreamer(tokenizer)
    # model.generate(**encoding, max_new_tokens=512, do_sample=True, streamer=streamer,
    #                pad_token_id=tokenizer.eos_token_id)

    generated_ids = model.generate(encoding.input_ids, max_new_tokens=512, temperature=0.0, do_sample=True)

    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in
                     zip(encoding .input_ids, generated_ids)]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print(response)
    # 将模型的回答添加到对话历史
    messages.append({"role": "assistant", "content": response})

