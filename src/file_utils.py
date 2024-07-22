import os
import zipfile
import re

def extract_zip_files(path, keyword=''):
    """
    解压路径中所有包含指定关键词的 ZIP 文件。

    Args:
        path (str): 包含 ZIP 文件的目录路径。
        keyword (str): 用于筛选 ZIP 文件的关键词。

    Returns:
        list: 解压后的文件夹路径列表。
    """
    if keyword == '':
        zip_files = [f for f in os.listdir(path) if f.endswith('.zip')]
    else:
        zip_files = [f for f in os.listdir(path) if f.endswith('.zip') and keyword in f]
    extracted_paths = []
    
    for zip_file in zip_files:
        with zipfile.ZipFile(os.path.join(path, zip_file), 'r') as zip_ref:
            extract_path = os.path.join(path, os.path.splitext(zip_file)[0])
            zip_ref.extractall(extract_path)
            extracted_paths.append(extract_path)
    
    return extracted_paths


def count_files_and_check_odd(path):
    """
    检查指定路径下每个文件夹中的文件个数是否为偶数，并打印出包含奇数个文件的文件夹名称。
    适用于字幕文件和视频文件在同一文件夹下的情况，正常情况下文件夹中视频和字幕的个数相同。

    Args:
        path (str): 要处理的根目录路径。
    """
    # 获取 path 目录下的所有文件夹
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    
    for folder in folders:
        folder_path = os.path.join(path, folder)
        # 统计文件夹中的文件个数
        num_files = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])
        
        # 检查文件个数是否为奇数
        if num_files % 2 != 0:
            print(f"Folder '{folder}' contains an odd number of files: {num_files}")


def process_files(path):
    """
    只适用于本项目。
    处理路径中的字幕文件夹：
    1. 查找包含 'Subtitles' 的文件夹。
    2. 对文件夹中包含“zh-CN”的文件进行重命名，处理为与视频名称相同的文件。因为部分视频播放器只能自动识别与视频同名的字幕文件。
    3. 对其他语言的字幕进行删除操作。

    Args:
        path (str): 要处理的根目录路径。
    """
    # 找到名称包含 Subtitles 的文件夹
    subtitle_dirs = [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and 'Subtitles' in d]
    
    for subtitle_dir in subtitle_dirs:
        for root, _, files in os.walk(subtitle_dir):
            for file in files:
                file_path = os.path.join(root, file)
                
                if '_zh-CN_' in file:
                    # 替换文件名
                    new_file_name = re.sub(r' - lang_zh-CN_.*?\.srt$', '.srt', file)
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} to {new_file_path}")
                else:
                    # 删除文件
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")


