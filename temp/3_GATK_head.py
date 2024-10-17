import os
import sys

path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/2_deduplication"

list1 = []

count = 0
index = 0

for i in os.listdir(path):
    if "bam" in i:
        f = open(f"{index}.sh", 'a')
        f.write(f"java -Xmx4g -jar ~/3_package/m_picard/AddOrReplaceReadGroups.jar I={path}/{i} O=./{i[:-4]}_withRG.bam ID=TT LB=TT PL=illumina PU=run SM={i[:8]} CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate\n")
        count += 1
        if count == 4:
            index += 1
            count = 0
