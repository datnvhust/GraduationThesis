import pandas as pd
import source_file.file as f
import source_file.data_processing as d_p
import numpy as np
import parse_ast as pa
import javalang
import csv
import random
import re
from bug_report.data_preprocessing import *
def save(data,name_file,path_root):
    print(len(data))
    data_link=data["files"]
    data_link=np.array(data_link)
    data_commit=data["commit"]
    data_commit=np.array(data_commit)
    data_summary=data["summary"]
    data_description=data["description"]
    nature_language=[]
    cnt=0
    files=[]
    all_files = f.listAllJavaFiles(path_root)
    with open(name_file, mode='w') as csv_file:
        fieldnames = ['nature_language', 'code_token', 'label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for n_l,link,id in zip(data_description,data_link,data_commit):
            if not n_l or pd.isnull(n_l):
                continue
            try:
                random.shuffle(all_files)
                n_l=processing(n_l)
                n_l=''.join(n_l)
                list_path=f.listFileInBug(link,id,path_root)  

                # 
                # duyệt tất cả files thay vì chỉ file trong list path
                # 

                for path in list_path:
                    # đặt mặc định label = 0
                    label = 1
                    # nếu file nằm trong list path thì label = 1
                    
                    # 
                    # phần này giữ nguyên
                    # 
                    files.append(path)
                    with open(files[-1],'r') as file:
                        file_jv=file.read()
                    tree = javalang.parse.parse(file_jv)
                    class_n_method = []
                    for path, node in tree:
                        node_str = str(node)
                        node_name = node_str.split('(')[0]
                        if node_name == 'ClassDeclaration' or node_name == 'MethodDeclaration':
                            class_n_method.append(str(node.name))
                    code_str=""
                    set_class=set(class_n_method)
                    list_word=[]
                    for c in set_class:
                        arr_word=d_p.split_word(c)
                        for w in arr_word:
                            w=w.lower()
                            list_word.append(w)
                    set_word=set(list_word)
                    for w in set_word:
                        code_str+=w
                        code_str+=" "
                    if code_str=='' or n_l=='':
                        continue
                    # 
                    # thêm path và label
                    #
                    writer.writerow({'nature_language':n_l,'code_token':code_str, 'label': label})
                cnt = 0
                for path in all_files:
                    if path in list_path:
                        continue
                    # đặt mặc định label = 0
                    label = 0
                    # nếu file nằm trong list path thì label = 1
                    if cnt==100:
                        break
                    cnt+=1
                    # 
                    # phần này giữ nguyên
                    # 
                    files.append(path)
                    with open(files[-1],'r') as file:
                        file_jv=file.read()
                    tree = javalang.parse.parse(file_jv)
                    class_n_method = []
                    for path, node in tree:
                        node_str = str(node)
                        node_name = node_str.split('(')[0]
                        if node_name == 'ClassDeclaration' or node_name == 'MethodDeclaration':
                            class_n_method.append(str(node.name))
                    code_str=""
                    set_class=set(class_n_method)
                    list_word=[]
                    for c in set_class:
                        arr_word=d_p.split_word(c)
                        for w in arr_word:
                            w=w.lower()
                            list_word.append(w)
                    set_word=set(list_word)
                    for w in set_word:
                        code_str+=w
                        code_str+=" "
                    if code_str=='' or n_l=='':
                        continue
                    # 
                    # thêm path và label
                    #
                    writer.writerow({'nature_language':n_l,'code_token':code_str,  'label': label})
            except:
                continue
def get_data(file_name, type,data, path_root):
    data_link=data["files"]
    data_link=np.array(data_link)
    data_commit=data["commit"]
    data_commit=np.array(data_commit)
    data_summary=data["summary"]
    data_description=data["description"]
    data_description=np.array(data_description)
    files=[]
    cnt=0
    fieldnames = ['nature_language', 'code_token']
    with open(file_name, type) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if type=="w":
            writer.writeheader()
        for n_l,link,id in zip(data_description,data_link,data_commit):
            if not n_l or pd.isnull(n_l):
                continue
            try:
                cnt+=1
                n_l=processing(n_l)
                # if type(link)!=str or type(n_l)!=list:
                    # continue
                n_l=''.join(n_l)
                list_path=f.listFileInBug(link,id,path_root)
                for path in list_path:
                    files.append(path)
                    with open(files[-1],'r') as file:
                        file_jv=file.read()
                    tree = javalang.parse.parse(file_jv)
                    class_n_method = []
                    for path, node in tree:
                        node_str = str(node)
                        node_name = node_str.split('(')[0]
                        if node_name == 'ClassDeclaration' or node_name == 'MethodDeclaration':
                            class_n_method.append(str(node.name))
                    code_str=""
                    set_class=set(class_n_method)
                    list_word=[]
                    for c in set_class:
                        arr_word=d_p.split_word(c)
                        for w in arr_word:
                            w=w.lower()
                            list_word.append(w)
                    set_word=set(list_word)
                    for w in set_word:
                        code_str+=w
                        code_str+=" "
                    if code_str=='' or n_l=='':
                        continue
                    writer.writerow({'nature_language':n_l,'code_token':code_str})
            except:
                continue
