import re
import os
import shutil
import pysrt

from translate import translate_text


def read_srt(file_path):
    """
    读取并解析 .srt 文件。

    Args:
        file_path (str): .srt 文件的路径。

    Returns:
        list: 包含字幕条目的列表，每个条目是一个字典，包含索引、时间戳和文本。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 分割成块，每个块表示一个字幕条目
    blocks = content.strip().split('\n\n')
    
    subtitles = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            index = lines[0]
            timestamps = lines[1]
            text = '\n'.join(lines[2:])
            
            start_time, end_time = re.match(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})", timestamps).groups()
            
            subtitles.append({
                'index': int(index),
                'start_time': start_time,
                'end_time': end_time,
                'text': text
            })
    
    return subtitles


def write_srt(subtitles, file_path):
    """
    将字幕条目写入 .srt 文件。

    Args:
        subtitles (list): 包含字幕条目的列表，每个条目是一个字典，包含索引、时间戳和文本。
        file_path (str): 输出 .srt 文件的路径。
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for subtitle in subtitles:
            file.write(f"{subtitle['index']}\n")
            file.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            file.write(f"{subtitle['text']}\n\n")


def translate_srt(translator, input_file, output_file, src='en', dest='zh-CN'):
    """
    读取、翻译并写入 .srt 文件。

    Args:
        translator(class): 翻译器。
        input_file (str): 输入 .srt 文件的路径。
        output_file (str): 输出 .srt 文件的路径。
        src (str): 源语言代码。
        dest (str): 目标语言代码。
    """
    # 读取srt文件
    subtitles = read_srt(input_file)
    
    # 翻译字幕文本
    for subtitle in subtitles:
        subtitle['text'] = translate_text(subtitle['text'], translator=translator, src=src, dest=dest)
    
    # 写入新的srt文件
    write_srt(subtitles, output_file)


def move_srt_files(path):
    """
    适用于本项目数据。
    将包含 'Subtitles' 的文件夹中的 .srt 文件移动到对应包含 'Videos' 的文件夹中，方便播放器自动识别字幕文件。

    Args:
        path (str): 包含 'Subtitles' 和 'Videos' 文件夹的根目录路径。
    """
    # 获取包含 Subtitles 的文件夹和包含 Videos 的文件夹
    subtitle_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and 'Subtitles' in d]
    video_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and 'Videos' in d]
    
    for subtitle_dir in subtitle_dirs:
        base_name = subtitle_dir.replace(' Subtitles', '')
        corresponding_video_dir = base_name + ' Videos'
        
        if corresponding_video_dir in video_dirs:
            subtitle_dir_path = os.path.join(path, subtitle_dir)
            video_dir_path = os.path.join(path, corresponding_video_dir)
            
            for root, _, files in os.walk(subtitle_dir_path):
                for file in files:
                    if file.endswith('.srt'):
                        src_file_path = os.path.join(root, file)
                        dest_file_path = os.path.join(video_dir_path, file)
                        shutil.move(src_file_path, dest_file_path)
                        print(f"Moved: {src_file_path} to {dest_file_path}")


def extract_subtitles(file_path):
    """
    用pysrt提取字幕文件中的内容

    Args:
        file_path (str): 字幕文件路径
    """
    subs = pysrt.open(file_path)
    return [{'start': sub.start.to_time(), 'end': sub.end.to_time(), 'text': sub.text} for sub in subs]