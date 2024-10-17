import os 


in_path = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/3_main_pipeline_1000_genome/4_GATK_header"

command = ""

count = 0
index = 0

# 25 thread
for i in os.listdir(in_path):
    if "bam" in i:
        f = open(f"{index}_HET.sh", 'a')
        command = f"java -Xmx10g -jar ~/3_package/l_BisSNP/1_tool/BisSNP-0.82.2.jar -R ../../3_main_pipeline_1000_genome/a_database/2_genome/test.fa -T BisulfiteGenotyper -I ../4_GATK_header/{i} -D ../../3_main_pipeline_1000_genome/a_database/1_SNPdata/GRCH38_150_dbSNP.vcf -vfn1 {i.split('_')[0][:-2]}.snp.HET.vcf --num_threads 5 --output_modes EMIT_HET_SNPS_ONLY"
        f.write(f"{command}\n")
        
        print(command)
        count += 1
        if count == 5:
            index += 1
            count = 0
