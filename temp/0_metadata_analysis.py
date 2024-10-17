import os

GATK = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/4_GATK_header"
GATK_list = []

for i in os.listdir(GATK):
    GATK_list.append(i.split("_")[0][:-2])

RNA = "/nas_shared/Data/jdw_SMC_CRC"
RNA_list = []

for i in os.listdir(RNA):
    RNA_list.append(i.split("_")[0])

print(len(RNA_list))
print(len(set(GATK_list) & set(RNA_list)))
