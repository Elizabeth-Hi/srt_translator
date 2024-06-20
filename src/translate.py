
def translate_text(text, translator, src='en', dest='zh-CN'):
    """
    使用 translator 将文本从源语言翻译为目标语言。

    Args:
        text (str): 要翻译的文本。
        translator(class): 翻译器。
        src (str): 源语言代码。
        dest (str): 目标语言代码。

    Returns:
        str: 翻译后的文本。
    """
    translated = translator(source=src, target=dest).translate(text=text)
    return translated