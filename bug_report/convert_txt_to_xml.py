import pandas as pd
from glob import glob
import numpy as np
import cgi
import html
import re
import xml.etree.ElementTree as ET

#AspectJ
#Eclipse_Platform_UI
#JDT
#SWT
#Tomcat

bugrepository = ET.Element('bugrepository')
bugrepository.set('name', 'SWT')


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    return s

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

path = '..\Dataset\dataset\*.txt'
files = glob(path)
# print(files)
# for file in files:
#     df = pd.read_csv(file, sep="\t")
#     print(file)
#     print(df)

data = pd.read_csv("..\Dataset\dataset\SWT.txt", sep="\t")
data_link = data["files"]
# data_link = np.array(data_link)
# data_commit = data["commit"]
data_summary = data["summary"]
data_description = data["description"]
data_id = data["bug_id"]
data_opendate = data["report_timestamp"]
data_fixdate = data["commit_timestamp"]
data_commit = data["commit"]
data_status = data["status"]
count = 0
max_file = 0
bug_id = 0
for files, summ, desc, i, o, f, commit, status in zip(data_link, data_summary, data_description, data_id, data_opendate, data_fixdate, data_commit, data_status):
    # if(not desc or pd.isnull(desc)):
    #     continue
    if status not in ['resolved fixed', 'verified fixed', 'closed fixed']:
        continue
    # array_file = divide_link(files)
    # length = len(array_file)
    # for file_ in array_file:
    #     if file_.find('tests/') == 0:
    #         length = length - 1
    # if length < 1:
    #     continue
    count += 1
    # bug
    # print(i, o, f)
    bug = ET.SubElement(bugrepository, 'bug')
    bug.set('id', str(i))
    bug.set('opendate', str(o))
    bug.set('fixdate', str(f))
    bug.set('status', status)
    bug.set('commit', commit)

    buginformation = ET.SubElement(bug, 'buginformation')
    summary = ET.SubElement(buginformation, 'summary')
    description = ET.SubElement(buginformation, 'description')
    summary.text = summ
    description.text = '' if (not desc or pd.isnull(desc)) else unescape(desc)
    # source
    fixedFiles = ET.SubElement(bug, 'fixedFiles')

    # print(divide_link(files))
    array_file = divide_link(files)
    if(len(array_file) > max_file):
        max_file = len(array_file)
        bug_id = i
    for file_ in array_file:
        file_name = ET.SubElement(fixedFiles, 'file')
        file_name.text = file_

    # print(files)
    # print(summary)
    # print(desc)

print("count", count)
print("max_length", max_file)
print("bug_id", bug_id)
mydata = ET.tostring(bugrepository)

# print(mydata)
myfile = open("SWT.xml", "wb")
myfile.write(mydata)