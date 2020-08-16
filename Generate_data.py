import pandas as pd
import source_file.file as f
import source_file.data_processing as d_p
import pandas as pd
import numpy as np
import parse_ast as pa
import javalang
import csv
import re
from bug_report.data_preprocessing import *
from pair_bugrp_source_v2 import *
data=pd.read_csv(r'D:\20192\project2\bug_localization\Eclipse_csv.csv')
get_data(file_name="dataset.csv",type="w",data=data,path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_eclipseUI\eclipse.platform.ui')
# save(data[:1656],name_file="eclipse_evaluate.csv",path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_eclipseUI\eclipse.platform.ui')
data=pd.read_csv(r'D:\20192\project2\bug_localization\JDT_csv.csv')
get_data(file_name="dataset.csv",type="a",data=data,path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_jdt\eclipse.jdt.ui')
# save(data[:632],name_file="JDT_evaluate.csv",path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_jdt\eclipse.jdt.ui')
data=pd.read_csv(r'D:\20192\project2\bug_localization\SWT_csv.csv')
get_data(file_name="dataset.csv",type="a",data=data,path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_swt\eclipse.platform.swt')
# save(data[:817],name_file="SWT_evaluate.csv",path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_swt\eclipse.platform.swt')
# get_data(file_name="dataset.csv",type="a",data=data[-2000:-1500],path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_eclipseUI\eclipse.platform.ui')
# get_data(file_name="dataset.csv",type="a",data=data[-2000:-1500],path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_jdt\eclipse.jdt.ui')
# get_data(file_name="dataset.csv",type="a",data=data[-2000:-1500],path_root=r'D:\20192\project2\bug_localization\data\SourceFile\sourceFile_swt\eclipse.platform.swt')