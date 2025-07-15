def combine_speaker_entries(transcript):
    combined_transcript = []
    current_entry = None

    for entry in transcript:
        if current_entry is None:
            current_entry = entry
        elif current_entry['spk'] == entry['spk']:
            current_entry['text'] += entry['text']
        else:
            combined_transcript.append(current_entry)
            current_entry = entry
    
    # Append the last entry if it exists
    if current_entry is not None:
        combined_transcript.append(current_entry)

    return combined_transcript

def read_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    transcript = []
    for line in lines:
        line = line.strip()
        if line:
            entry = eval(line)
            transcript.append(entry)
    
    return transcript

def write_combined_transcript(file_path, combined_transcript):
    with open(file_path, 'w', encoding='utf-8') as file:
        for entry in combined_transcript:
            file.write(f"{entry}\n")

# 处理文件夹下所有txt文件
import os

input_dir = '/Users/lujiayi/parameter/spk_sorted_files'
output_dir = '/Users/lujiayi/parameter/spk_combined_files'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)
        transcript = read_transcript(input_file_path)
        combined_transcript = combine_speaker_entries(transcript)
        write_combined_transcript(output_file_path, combined_transcript)
        print(f"{filename} 处理完成，结果保存到 {output_file_path}")

print("所有文件处理完成。")
