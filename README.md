# SRT Translator Project

## 项目简介

这个项目用于处理和翻译字幕文件，包括解压 ZIP 文件、翻译和移动 SRT 文件、翻译字幕内容以及统计文件夹中的文件个数等，
能够实现将Subtitles路径中的外文字幕翻译并生成中文字幕文件，经过一些文件名称处理后，移动到对应的Videos路径中，
使得在播放Videos路径下的视频时，播放器能够自动识别字幕文件。
部分脚本只适用于示例数据test_data中的数据格式。

## 目录结构

```plaintext
srt_translator/
│
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── file_utiles.py
│   ├── subtitle_utils.py
│   └── translate.py
└── test_data/
```

## 安装
1.克隆此仓库：
```
git clone https://github.com/Elizabeth-Hi/srt_translator.git
cd srt_translator
```

2. 创建并激活虚拟环境（可选）：
```
python -m venv venv
source venv/bin/activate  # 对于 Windows，使用 `venv\Scripts\activate`
```

3. 安装依赖项：
```
pip install -r requirements.txt
```

## 使用说明
### 处理文件
file_utile.py可以解压包含特定关键字的 ZIP 文件、处理字幕文件名称等。

### 处理字幕
subtitle_utils.py可以用于读取、解析、翻译、写入.srt字幕文件。

### 翻译
translate.py可用于使用指定翻译器将指定文字从源语言翻译为目标语言。

### 主函数
main.py能够批量翻译指定路径下的字幕文件。
默认使用Google Translator，可更换为其他翻译器，例如Baidu Translator。

### test_data
该文件夹下存放测试用的字幕和视频文件，内容为UDACITY的免费统计学入门课程。




