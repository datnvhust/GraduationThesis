import javalang
def parse(link):
    with open(link,'r') as f:
        file_jv=f.read()
    tree = javalang.parse.parse(file_jv)
    return tree