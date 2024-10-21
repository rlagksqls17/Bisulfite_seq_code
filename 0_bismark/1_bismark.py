import os
import subprocess
import pandas as pd

RNA_path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/z_code/1_deduplication/RNA_seq_meta_data.csv"
RNA_df = pd.read_csv(RNA_path, sep = "\t")
RNA_sample_list = list(set([i.split("-")[0] for i in list(RNA_df['Unnamed: 0'])]))


in_path1 = "/home/bilab/gdy/methylation/col_cancer_data/2.Trim"
in_path2 = "/home/bilab/gdy/methylation/set2_col_cancer_data/2.Trim"

count = 0
for i in RNA_sample_list:
    TT_1 = f"{i}-TT-D_1_val_1.fq.gz"
    TT_2 = f"{i}-TT-D_2_val_2.fq.gz"
    TN_1 = f"{i}-TN-D_1_val_1.fq.gz"
    TN_2 = f"{i}-TN-D_2_val_2.fq.gz"
    
    in_path1_list = os.listdir(in_path1)
    in_path2_list = os.listdir(in_path2)

    log = open("log.txt", 'a')
    if TT_1 in in_path1_list and TT_2 in in_path1_list and TN_1 in in_path1_list and TN_2 in in_path1_list:
        log.write(subprocess.check_output("date", shell=True, text=True))
        log.write(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path1}/{TT_1} -2 {in_path1}/{TT_2}\n")
        log.write(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path1}/{TN_1} -2 {in_path1}/{TN_2}\n")

        
        os.system(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path1}/{TT_1} -2 {in_path1}/{TT_2}")
        os.system(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path1}/{TN_1} -2 {in_path1}/{TN_2}")
    

    elif TT_1 in in_path2_list and TT_2 in in_path2_list and TN_1 in in_path2_list and TN_2 in in_path2_list:
        log.write(subprocess.check_output("date", shell=True, text=True))
        log.write(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path2}/{TT_1} -2 {in_path2}/{TT_2}\n")
        log.write(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path2}/{TN_1} -2 {in_path2}/{TN_2}\n")
        
        os.system(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path2}/{TT_1} -2 {in_path2}/{TT_2}")
        os.system(f"bismark -N 1 -p 4 --multicore 4 /home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/5_genome -1 {in_path2}/{TN_1} -2 {in_path2}/{TN_2}")

        count += 1
