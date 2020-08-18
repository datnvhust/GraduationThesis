import pandas as pd
from glob import glob
import re
path = '..\Dataset\dataset\*.txt'
files = glob(path)
print(files)
for file in files:
  df = pd.read_csv(file, sep="\t")
  df.to_csv(re.sub(".txt", ".csv", file), index=False) 