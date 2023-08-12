def convert(filename):
    file = open(filename, 'r',encoding='utf8')
    text = file.read()
    return text