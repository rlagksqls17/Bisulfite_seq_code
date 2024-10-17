import os
import pandas as pd


def main():
    dedup_path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/3_deduplication_sam"
    dedup_sample_list = []

    for f in os.listdir(dedup_path):
        dedup_sample = "-".join(f.split("-")[0:1])
        dedup_sample_list.append(dedup_sample)

    #print(len(set(dedup_sample_list))) # 63 sample

    RNA_csv_path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/z_code/RNA_seq_meta_data.csv"
    df = pd.read_csv(RNA_csv_path, sep = "\t")
    RNA_sample_list = [i.split("-")[0] for i in list(df["Unnamed: 0"])]
    #print(len(set(RNA_sample_list))) # 80

    #print(len(set(dedup_sample_list) & set(RNA_sample_list))) # 63
    target_list = list(set(RNA_sample_list) - set(dedup_sample_list))
    
    for i in target_list:
        print(i)
    
    print("==========")
    print(len(target_list))
    return 0


main()
