import pandas as pd
import source_file.file as f
import source_file.data_processing as d_p
import numpy as np
import parse_ast as pa
import javalang
import csv
import random
import re
import bug_report.data_preprocessing as pre

def get_data(file_name, type, data, path_root):
    data_link = data["files"]
    # data_link = np.array(data_link)
    data_commit = data["commit"]
    data_commit = np.array(data_commit)
    data_summary = data["summary"]
    data_description = data["description"]
    data_description = np.array(data_description)
    files = []
    cnt = 0
    fieldnames = ['nature_language', 'code_token']
    with open(file_name, type) as csv_file: # viết file csv
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if type == "w":
            writer.writeheader()
        for n_l, link, id, summary in zip(data_description, data_link, data_commit, data_summary):
            # nếu không có desc thì bỏ qua hàng đó
            if not n_l or pd.isnull(n_l):
                continue
            try:
                cnt += 1
                # tiền xử lí bugs
                summary = pre.processing(summary)
                n_l = pre.processing(n_l)
                n_l = np.append(summary, n_l)
                # concat summary + desc
                # if type(link)!=str or type(n_l)!=list:
                # continue
                n_l = ''.join(n_l)
                # list_path là danh sách đường linh dẫn đến source file tương ứng
                list_path = f.listFileInBug(link, id, path_root)
                # print(list_path)
                for path in list_path:
                    files.append(path)
                    with open(files[-1], 'r') as file:
                        # print("file", files[-1])
                        file_jv = file.read()
                    # tree là cây AST
                    tree = javalang.parse.parse(file_jv)
                    # print(tree)
                    class_n_method = []
                    # chưa rõ path có tác dụng gì
                    for path, node in tree:
                        # print(node)
                        node_str = str(node)
                        node_name = node_str.split('(')[0]
                        # nếu là định nghĩa lớp hoặc định nghĩa phương thức thì giữ lại
                        if node_name == 'ClassDeclaration' or node_name == 'MethodDeclaration':
                            class_n_method.append(str(node.name))
                    # print(class_n_method)
                    code_str = ""
                    # set array để tạo ra Set
                    set_class = set(class_n_method)
                    print(set_class)
                    list_word = []
                    for c in set_class:
                        print(c)
                        arr_word = d_p.split_word(c)
                        print(arr_word)
                        for w in arr_word:
                            w = w.lower()
                            list_word.append(w)
                    set_word = set(list_word)
                    for w in set_word:
                        code_str += w
                        code_str += " "
                    # print("desc", n_l)
                    # print("summary", summary)
                    # print("code_token", code_str)
                    if code_str == '' or n_l == '':
                        continue
                    writer.writerow(
                        {'nature_language': n_l, 'code_token': code_str})
            except:
                continue

# with open(r"Dataset/SourceFile/sourceFile_eclipseUI/eclipse.platform.ui/weaver/src/org/aspectj/weaver/99a873c AjcMemberMaker.java", 'r') as file:
#     print(file.read())
data=pd.read_csv('./Dataset/dataset/AspectJ.csv')
get_data(file_name="dataset1.csv",type="w",data=data,path_root=r'..\Dataset\SourceFile\sourceFile_aspectj\org.aspectj')
