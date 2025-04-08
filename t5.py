prompt = f"<s>[INST] {prompt} [/INST]"
# 或包含系统提示
# prompt = f"<s>[INST] <<SYS>>\\n{system_prompt}\\n<</SYS>>\\n\\n{user_prompt} [/INST]"
text = prompt  # 直接使用手动构造的 prompt
encoding = tokenizer(text, return_tensors="pt").to(device)
generated_ids = model.generate(
    encoding.input_ids,
    max_new_tokens=256,
    do_sample=True,
    eos_token_id=tokenizer.eos_token_id,  # 显式指定 EOS
)# 直接取生成的后 max_new_tokens 部分
response = tokenizer.decode(generated_ids[0][-256:], skip_special_tokens=True)

