from funasr import AutoModel
import os

# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model = AutoModel(model="paraformer-zh", model_revision="v2.0.4",
                  vad_model="fsmn-vad", vad_model_revision="v2.0.4",
                  punc_model="ct-punc-c", punc_model_revision="v2.0.4",
                  spk_model="cam++", spk_model_revision="v2.0.2",
                  )

wav_dir = "/Users/lujiayi/parameter/record_wav"
output_dir = "/Users/lujiayi/parameter/recognizd_wav_to_txt"
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

wav_files = [f for f in os.listdir(wav_dir) if f.endswith('.wav')]
for wav_file in wav_files:
    wav_path = os.path.join(wav_dir, wav_file)
    res = model.generate(input=wav_path, batch_size_s=300, hotword='魔搭')
    print(f"{wav_file}: {res}")
    # 保存每个识别结果到单独的txt文件
    txt_filename = os.path.splitext(wav_file)[0] + ".txt"
    txt_path = os.path.join(output_dir, txt_filename)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(str(res))

# 确认保存成功
print("所有识别结果已分别保存为单独的txt文件")


