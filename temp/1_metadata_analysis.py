import os 
import pandas as pd


trim_path1 = "/home/bilab/gdy/methylation/col_cancer_data/2.Trim"
trim_path2 = "/home/bilab/gdy/methylation/set2_col_cancer_data/2.Trim"
dedup_path1 = "/home/bilab/gdy/methylation/col_cancer_data/5.deduplicate"
dedup_path2 = "/home/bilab/gdy/methylation/set2_col_cancer_data/5.deduplicate"

trim_list1 = []
trim_list2 = []
dedup_list1 = []
dedup_list2 = []

for f in os.listdir(trim_path1):
    if "report" in f:
        ID = f.split(".")[0].split("_")[0]
        trim_list1.append(ID)


for f2 in os.listdir(trim_path2):
    if "report" in f2:
        ID = f2.split(".")[0].split("_")[0]
        trim_list2.append(ID)

for f3 in os.listdir(dedup_path1):
    if "report" in f3:
        ID = "_".join(f3.split("_")[:2]).split("_")[0]
        dedup_list1.append(ID)

for f4 in os.listdir(dedup_path2):
    if "report" in f4: 
        ID = "_".join(f4.split("_")[:2]).split("_")[0]
        dedup_list2.append(ID)


set1 = set(trim_list1 + trim_list2)
set2 = set(dedup_list1 + dedup_list2)

print("set1len", len(set1)) # set1len 230 => 115 sample
print("set2len", len(set2)) # set2len 130 => 65 sample
print(len(set1&set2)) # 130
print(set1-set2) # len = 100 => 50 sample
print(set2-set1) # set()


df = pd.read_csv("/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline/z_code/RNA_seq_meta_data.csv", sep = "\t")
df_columns = set([f"{i}-D" for i in list(df['Unnamed: 0'])])
print(len(df_columns))
print(len(set2&df_columns))
print(set2 - (set2&df_columns)) # 안겹치는 애들임

"""
result

trimming sample은 총 230개, 따라서 115 human
tirmming sample 중 deduplicated sample은 총 130개, 따라서 65 human
42번째 줄에서 set1 - set2 검산해보니 맞았음

df_columns는 총 160개, 따라서 80 human
현재 (24.09.30), df_columns에 없는 애들도 존재
=> {'10001691-TT-D', '11000311-TT-D', '11000311-TN-D', '10001691-TN-D'} 이 애들임

=> deduplication은 얼마 안걸리므로, 일단 80 human에 대해서 해보자.
"""
