import os
import sys

path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline/2_deduplication"

count = 0

for i in os.listdir(path):
    if "bam" in i:
        command = f"samtools view -h -o {i[:-4]}.sam {path}/{i}"
        os.system(command)
