# 语音识别与文本提取项目

本项目用于音频识别和文本内容提取，适用于批量处理语音转文本的场景。项目包含两个核心Python脚本，实现从音频文件到结构化文本的完整处理流程。

## 项目结构

```
parameter/
├── record_wav/                    # 原始录音文件目录（wav格式）
├── recognizd_wav_to_txt/          # 语音识别结果目录（txt格式）
├── extracted_txt/                 # 提取整理后的文本目录
├── recognition.py                 # 语音识别脚本
├── extract.py                     # 文本提取整理脚本
├── requirements.txt               # 项目依赖
└── README.md                      # 项目说明文档
```

## 核心功能

### 1. 语音识别 (recognition.py)
**功能**：将音频文件转换为文本，支持说话人识别和标点符号

**主要特性**：
- 使用 FunASR 的 paraformer-zh 模型进行中文语音识别
- 支持说话人分离 (speaker diarization)
- 自动标点符号识别
- 批量处理 wav 格式音频文件
- 支持热词识别（当前设置为"魔搭"）

**输入**：`record_wav/` 目录下的 wav 文件
**输出**：`recognizd_wav_to_txt/` 目录下的 txt 文件

**处理流程**：
1. 遍历 `record_wav/` 目录下的所有 wav 文件
2. 使用 FunASR 模型进行语音识别
3. 将识别结果保存为对应的 txt 文件
4. 输出文件包含说话人信息、时间戳和文本内容

### 2. 文本提取整理 (extract.py)
**功能**：从识别结果中提取并整理说话人对话内容

**主要特性**：
- 批量处理识别结果文件
- 按时间顺序排序对话内容
- 提取说话人标识和文本内容
- 错误处理和容错机制
- 自动生成整理后的输出文件

**输入**：`recognizd_wav_to_txt/` 目录下的 txt 文件
**输出**：`extracted_txt/` 目录下的整理后文件

**处理流程**：
1. 遍历 `recognizd_wav_to_txt/` 目录下的所有 txt 文件
2. 解析 JSON 格式的识别结果
3. 提取 `sentence_info` 中的对话信息
4. 按 `start` 时间字段排序
5. 格式化输出为 "spk{说话人ID}: {文本内容}" 格式
6. 保存到对应的输出文件

## 安装与配置

### 环境要求
- Python 3.7+
- 足够的磁盘空间用于模型下载和文件处理

### 安装依赖
```bash
pip install -r requirements.txt
```

### 目录准备
确保以下目录存在（脚本会自动创建）：
- `record_wav/` - 存放待识别的音频文件
- `recognizd_wav_to_txt/` - 存放识别结果
- `extracted_txt/` - 存放整理后的文本

## 使用流程

### 1. 准备音频文件
将需要识别的 wav 格式音频文件放入 `record_wav/` 目录

### 2. 执行语音识别
```bash
python recognition.py
```
- 脚本会自动处理所有 wav 文件
- 识别结果保存到 `recognizd_wav_to_txt/` 目录
- 每个音频文件对应一个 txt 结果文件

### 3. 提取整理文本
```bash
python extract.py
```
- 脚本会处理所有识别结果文件
- 整理后的文本保存到 `extracted_txt/` 目录
- 输出文件命名格式：`原文件名_整理输出.txt`

## 输出格式说明

### 识别结果格式 (recognizd_wav_to_txt/*.txt)
```json
[{
  "sentence_info": [
    {
      "spk": 1,
      "text": "说话内容",
      "start": 0.0,
      "end": 2.5
    }
  ]
}]
```

### 整理后格式 (extracted_txt/*_整理输出.txt)
```
spk1: 第一段对话内容
spk2: 第二段对话内容
spk1: 第三段对话内容
...
```

## 注意事项

1. **模型下载**：首次运行 `recognition.py` 时会自动下载 FunASR 模型，需要网络连接
2. **文件格式**：音频文件必须是 wav 格式
3. **编码格式**：所有文本文件使用 UTF-8 编码
4. **错误处理**：脚本包含错误处理机制，单个文件处理失败不会影响其他文件
5. **路径配置**：如需修改文件路径，请编辑脚本中的 `wav_dir`、`input_dir`、`output_dir` 变量

## 常见问题

**Q: 识别结果为空或错误？**
A: 检查音频文件质量，确保是清晰的 wav 格式文件

**Q: 处理速度慢？**
A: 语音识别需要时间，特别是首次运行时需要下载模型

**Q: 输出文件乱码？**
A: 确保系统支持 UTF-8 编码，检查文件编码设置

## 技术栈

- **语音识别**：FunASR (paraformer-zh)
- **说话人分离**：CAM++ 模型
- **标点符号**：CT-PUNC-C 模型
- **语音活动检测**：FSMN-VAD 模型
- **编程语言**：Python 3.7+

## 许可证

本项目仅供学习和研究使用。
