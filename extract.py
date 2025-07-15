import ast
import os

# 要处理的文件夹
input_dir = "/Users/lujiayi/parameter/recognizd_wav_to_txt"
output_dir = "/Users/lujiayi/parameter/spk_sorted_files"
os.makedirs(output_dir, exist_ok=True)

# 遍历文件夹下所有txt文件
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        try:
            data = ast.literal_eval(file_content)
        except Exception as e:
            print(f"文件 {filename} 解析失败: {e}")
            continue
        # 兼容单条或多条数据
        if isinstance(data, dict):
            data = [data]
        spk_ordered_texts = []
        for entry in data:
            spk = entry.get('spk')
            text = entry.get('text')
            spk_ordered_texts.append({'spk': spk, 'text': text})
        # 保存每个文件的结果到单独的输出文件夹
        output_file_path = os.path.join(output_dir, filename)
        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            for item in spk_ordered_texts:
                out_file.write(f"{item}\n")
        print(f"{filename} 已处理，结果保存到 {output_file_path}")
