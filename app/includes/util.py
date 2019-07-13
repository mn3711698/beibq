#coding: utf-8

def strdecode(text):
    if not isinstance(text, str):
        try:
            text = text.decode('utf-8')
        except UnicodeDecodeError:
            text = text.decode('gbk', 'ignore')
        return text
    return text


