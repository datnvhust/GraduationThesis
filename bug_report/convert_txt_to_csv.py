import pandas as pd
df = pd.read_csv('Dataset\dataset\AspectJ.txt', sep="\t")
df.to_csv('Dataset\dataset\AspectJ.csv', index=False)