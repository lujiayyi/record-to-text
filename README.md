# 参数项目说明文档

本项目用于音频识别、说话人分离、文本整理与合并，适用于批量处理语音转文本的场景。项目包含多个 Python 脚本和若干数据文件夹，整体流程如下：

## 目录结构

- `record_wav/`：原始录音（wav 文件）存放目录
- `recognizd_wav_to_txt/`：音频识别后生成的原始文本（txt 文件）
- `spk_sorted_files/`：说话人分离与排序后的文本
- `spk_combined_files/`：同一说话人连续发言合并后的文本
- `combine.py`：合并同一说话人连续发言的脚本
- `extract.py`：从原始识别文本中提取说话人文本并排序的脚本
- `recognition.py`：批量音频识别脚本（依赖 FunASR）
- `second.py`：提取文本内容并拼接输出的脚本

---

## 各脚本功能说明

### 1. recognition.py
- 功能：批量将 `record_wav/` 下的 wav 文件转为文本，输出到 `recognizd_wav_to_txt/`。
- 依赖：FunASR
- 主要流程：
  1. 遍历 `record_wav/` 下所有 wav 文件
  2. 使用 FunASR 进行语音识别，结果保存为 txt 文件

### 2. extract.py
- 功能：将 `recognizd_wav_to_txt/` 下的 txt 文件，提取出 spk（说话人）和 text 字段，按顺序输出到 `spk_sorted_files/`。
- 主要流程：
  1. 遍历所有 txt 文件
  2. 解析为 Python 对象，提取 spk 和 text 字段
  3. 仅保留 spk=1 或 2 的内容，按顺序写入新文件

### 3. combine.py
- 功能：将 `spk_sorted_files/` 下的 txt 文件，同一说话人连续发言合并，输出到 `spk_combined_files/`。
- 主要流程：
  1. 读取每行（每条发言）
  2. 如果说话人相同则合并 text，否则换行
  3. 合并后写入新文件

### 4. second.py
- 功能：将单个 txt 文件中所有 text 字段内容拼接为一段文本，输出到 `output.txt`。
- 主要流程：
  1. 读取 txt 文件内容，解析为 list of dicts
  2. 提取所有 text 字段并拼接
  3. 写入 output.txt

---

## 运行流程建议

1. 将待识别的 wav 文件放入 `record_wav/`
2. 运行 `recognition.py`，生成原始识别文本到 `recognizd_wav_to_txt/`
3. 运行 `extract.py`，提取并排序说话人文本到 `spk_sorted_files/`
4. 运行 `combine.py`，合并同一说话人连续发言到 `spk_combined_files/`
5. 如需拼接文本，可用 `second.py` 对单个 txt 文件处理

---

## 依赖环境

- Python 3.7+
- FunASR（仅 recognition.py 需要）

安装 FunASR：
```bash
pip install funasr
```

---

## 注意事项
- 路径请根据实际情况修改为绝对路径或相对路径。
- 处理大批量文件时建议分步检查每一步输出。
- 识别模型需提前下载，详见 FunASR 官方文档。

---

## 联系方式
如有问题请联系项目维护者。
