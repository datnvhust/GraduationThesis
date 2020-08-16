import os
import glob
import datetime
import ntpath

# function read folder
def divide_link(input):
    output = []
    link = ''
    for i in range(len(input)):
        if (input[i]==' ' and input[i-5:i]=='.java'):
            output.append(link)
            link = ''
        else:
            link += input[i]
    if link[-5:]=='.java':
        output.append(link)
    return output

def clean(link, id):  # add id , return then id+name file java
    path = os.path.normpath(link)
    token = path.split(os.sep)
    token[len(token) - 1]=id + ' ' + token[len(token) - 1]
    link_n=''
    cnt=0
    for i in token:
        link_n+=i
        if cnt!=len(token)-1:
            link_n+="\\"
        cnt+=1
    return link_n

def listFileInBug(link,id,path_root):
    s=[]
    list_link = divide_link(link)
    for i in list_link:
        s.append(os.path.join(path_root,clean(i,id)))

    return s

# 
# hàm lấy ra tất cả files java trong thư mục
#
def listAllJavaFiles(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.java' in file:
                files.append(os.path.join(r, file))

    return files