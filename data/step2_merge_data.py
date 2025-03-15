import json

names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]

for name in names:
    si_path = f'dataset/simplify_{name}.json'
    bl_path = f'{name}/block_{name}.json'
    fix_path = f'{name}/fixed_{name}.json'
    save_path = f'{name}/{name}.json'

    # 读取 simplify_.json 文件
    with open(si_path, 'r', encoding='utf-8') as f:
        simplify_data = json.load(f)

    # 读取 block_.json 文件
    with open(bl_path, 'r', encoding='utf-8') as f:
        block_data = json.load(f)

    # 读取 fix_.json 文件
    with open(fix_path, 'r', encoding='utf-8') as f:
        fix_data = json.load(f)

    block_data_dict = {item['id']: item for item in block_data}
    fix_data_dict = {item['id']: item for item in fix_data}

    for item in simplify_data:
        item_id = item.get('id')

        # 查找是否有匹配的 block 数据
        if item_id in block_data_dict:
            block_item = block_data_dict[item_id]
            item.update({
                'bug': block_item.get('bug'),
                'bug_before': block_item.get('bug_before'),
                'bug_after': block_item.get('bug_after'),
                'cwe': block_item.get('cwe'),
                'issue': block_item.get('issue')
            })
        else:
            print(f'Block data not found for item {item_id}')

        if item_id in fix_data_dict:
            fix_item = fix_data_dict[item_id]
            item.update({
                'fixed_code': fix_item.get('fix_code')
            })
        else:
            print(f'Fixed data not found for item {item_id}')

    # 保存合并后的数据到一个新的 JSON 文件
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(simplify_data, f, ensure_ascii=False, indent=4)
