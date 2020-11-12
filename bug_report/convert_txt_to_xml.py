import pandas as pd
from glob import glob
import numpy as np
import cgi
import html
import re
import xml.etree.ElementTree as ET
import datetime

#AspectJ 7-2002 to 10-2006
#Eclipse_Platform_UI
#JDT
#SWT
#Tomcat

a = ['28919', '39436', '40380', '43709', '29769', '29934', '29959', '30168', '30439', '28974', '29186', '44117', '45489', '44191', '44272', '47318', '47754', '46280', '46298', '48990', '47910', '49250', '47952', '48080', '48091', '31460', '32463', '31423', '34858', '34925', '34951', '33635', '36430', '36803', '36234', '37576', '37739', '38131', '39993', '40257', '40192', '39626', '41952', '41123', '43033', '42993', '43194', '42539', '42573', '72671', '50200', '49457', '50570', '50776', '49638', '49657', '49743', '76096', '76055', '76798', '77163', '77799', '80916', '81863', '81846', '80249', '51929', '52394', '53012', '51320', '51322', '54421', '54625', '54965', '55341', '53981', '53999', '58520', '58681', '59208', '59596', '59895', '60015', '59909', '57430', '57436', '57666', '62227', '62642', '64069', '64331', '61411', '61536', '67592', '67774', '65319', '68494', '69011', '68991', '70008', '70241', '70619', '70773', '69459', '71723', '71811', '71878', '72150', '72154', '72157', '72528', '72531', '72699', '71377', '74238', '74952', '73433', '82062', '82570', '82752', '83303', '83563', '83565', '82171', '82134', '82218', '112243', '112736', '113257', '113510', '113511', '114343', '116626', '116949', '117189', '117209', '117296', '117681', '117882', '118192', '114875', '118715', '118599', '115251', '115252', '115275', '115607', '118781', '120401', '120474', '120351', '120356', '120363', '120739', '120543', '120909', '121395', '121616', '122370', '119353', '119210', '119451', '119539', '119543', '119749', '86789', '88652', '87376', '92880', '95517', '95529', '96371', '100195', '100227', '101047', '98320', '99168', '102459', '103741', '104218', '107299', '108118', '109614', '109173', '128744', '123212', '123423', '123612', '123695', '124105', '124654', '124808', '125101', '124999', '125405', '125475', '125480', '122580', '125699', '125810', '122728', '122742', '161217', '159896', '128128', '128237', '128699', '128618', '128655', '129525', '129566', '126328', '131505', '131932', '131933', 
'132130', '132349', '132591', '132926', '133117', '133307', '130300', '130837', '130869', '136665', '136707', '138143', '138171', '138215', '138219', '138223', '138286', '138540', '134541', '135068', '135001', '135780', '141956', '142165', '146546', '147801', '147701', '145086', '148409', '148388', '148536', '148537', '148545', '148693', '148727', '148737', '148908', '148786', '149071', '148972', '149305', '149289', '145693', '145950', '150271', '150671', '151182', '151673', '151938', '151845', '152257', '152366', '152388', '153490', '153535', '153845', '154332', '152631', '152589', '155148', '155238', '152848', '152871', '152873', '155972', '156904', '156962', '158412', '158573', '158624', '173602']
print(len(a))
min_date = datetime.datetime(2002, 7, 1).timestamp()
max_date = datetime.datetime(2006, 10, 1).timestamp()

bugrepository = ET.Element('bugrepository')
bugrepository.set('name', 'AspectJ')


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

data = pd.read_csv("..\Dataset\dataset\AspectJ.txt", sep="\t")
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
z = []
for files, summ, desc, i, o, f, commit, status in zip(data_link, data_summary, data_description, data_id, data_opendate, data_fixdate, data_commit, data_status):
    # if(not desc or pd.isnull(desc)):
    #     continue
    # if status not in ['resolved fixed', 'verified fixed', 'closed fixed']:
    #     continue
    # if o < min_date or o > max_date:
    #     continue
    # array_file = divide_link(files)
    # length = len(array_file)
    # for file_ in array_file:
    #     if file_.find('tests/') != -1 or file_.find('testsrc/') != -1 or file_.find('testing/') != -1 or file_.find('testdata/') != -1:
    #         length = length - 1
    # if length < 1:
    #     continue
    z.append(str(i))
    if str(i) not in a:
        continue
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
    summary.text = summ[4:]
    description.text = '' if (not desc or pd.isnull(desc)) else unescape(desc)
    # source
    fixedFiles = ET.SubElement(bug, 'fixedFiles')

    # print(divide_link(files))
    array_file = divide_link(files)
    if(len(array_file) > max_file):
        max_file = len(array_file)
        bug_id = i
    for file_ in array_file:
        # if file_.find('tests/') == -1 and file_.find('testsrc/') == -1 and file_.find('testing/') == -1 and file_.find('testdata/') == -1:
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
myfile = open("AspectJ.xml", "wb")
myfile.write(mydata)

print((z))
for i in a:
    if i not in z:
        print(i)