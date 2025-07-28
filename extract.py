import json
import os

# 设置输入和输出目录
input_dir = "/Users/lujiayi/parameter/recognizd_wav_to_txt"
output_dir = "/Users/lujiayi/parameter/extracted_txt"
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

# 遍历输入文件夹下的所有txt文件
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        # 生成输出文件名：原文件名 + "_整理输出"
        output_filename = os.path.splitext(filename)[0] + "_整理输出.txt"
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"正在处理文件: {filename}")
        
        try:
            # 读取 txt 文件
            with open(input_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 解析数据
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                data = eval(content)  # fallback，如果是 Python dict 格式

            # 访问第一项字典的 sentence_info 字段
            sentence_info = data[0]["sentence_info"]

            # 按 start 时间排序
            sentences = sorted(sentence_info, key=lambda x: x['start'])

            # 写入整理后的输出
            with open(output_path, "w", encoding="utf-8") as out:
                for sentence in sentences:
                    spk = f"spk{sentence['spk']}"
                    text = sentence['text']
                    out.write(f"{spk}: {text}\n")

            print(f"✅ {filename} 整理完成，输出已保存到：{output_filename}")
            
        except Exception as e:
            print(f"❌ 处理文件 {filename} 时出错: {e}")
            continue

print("🎉 所有文件处理完成！")