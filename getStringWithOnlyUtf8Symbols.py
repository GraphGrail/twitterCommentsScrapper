import re

def getStringWithOnlyUtf8Symbols(string):
    res = string.encode('utf-8', errors="replace").decode("utf-8")
    res = res.replace("\ufffd", " ")
    res = re.sub('\s+', ' ', res).strip()
    return res