def isValid(s):
    l = ['{','}','[',']','(',')']
    res = []
    for i in s:
        if i in l:
            res.append(i)
    resStr  = ''.join(res)
    while '()' in resStr or '{}' in resStr or '[]' in resStr:
        resStr = resStr.replace('()','').replace('{}','').replace('[]','')
    if resStr == '':
        return True
    return False

