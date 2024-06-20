import os
from deep_translator import GoogleTranslator
import traceback

from file_utils import extract_zip_files
from subtitle_utils import translate_srt


def process_subtitle_files(paths_list, translator=GoogleTranslator, src='el', dest='zh-CN' ):
    """
    处理paths_list路径中的字幕文件：
 
    1. 将目录中的源语言(srouce)为src的.srt 文件翻译解压为目标语言dest(destination)（文件名包含 '_源语言_'）。
    2. 输出翻译后的字幕文件，命名方式为将原字幕文件名称中代表源语言的部分替换为目标语言

    Args:
        paths_list (list): 包含字幕文件的目录路径集合。
        translator(class): 翻译器，默认使用谷歌，可换为百度
        keyword (str): 用于筛选目标文件夹的关键词。
        src (str): 源语言代码。
        dest (str): 目标语言代码。
    """
    if not paths_list:
        return
    
    for extract_path in paths_list:
        for root, _, files in os.walk(extract_path):
            for file in files:
                try:
                    # 通过"_源语言_"的格式识别需翻译的字幕文件，可根据需求修改
                    if file.endswith('.srt') and '_' + src + '_' in file:
                        input_file = os.path.join(root, file)
                        # 生成新的字幕文件名称，可根据需求修改
                        output_file = os.path.join(root, file.replace('_' + src + '_', '_' + dest + '_'))
                        # 翻译目标文件
                        translate_srt(translator, input_file, output_file, src, dest)
                        print(f"Translated {input_file} to {output_file}")
                except Exception as e:
                    print('-----------Error----------')
                    print(file)
                    traceback.print_exc()
                    print('')


if __name__ == "__main__":
    # 翻译path路径下的zip文件夹
    path = "./test_data"  # 请将此路径修改为你的实际路径
    # 对包含Subtitles的文件夹进行解压
    extracted_paths = extract_zip_files(path, keyword='Subtitles')
    # 翻译extracted_paths中的所有srt文件
    process_subtitle_files(extracted_paths, translator=GoogleTranslator, src='en', dest='zh-CN')


    # 翻译单个srt文件
    input_file = "./test_data/1 - Introduction - lang_en_vs2.srt"
    output_file = './test_data/1 - Introduction - lang_zh-CN_vs2.srt'
    translate_srt(input_file, output_file)
