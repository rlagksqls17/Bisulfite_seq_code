import sys

def get_ID_list(f):
    ID_list = []
    while(1):
        line = f.readline().strip()
        if line == "": break
        elif line[0] == "#":
            try: 
                ID_index = line.index("ID=")
                ID = line[ID_index:].split(",")[0][3:]
                ID_list.append(ID)
            except: continue
        else:
            break

    return ID_list


def find_ID_writed(f, ID):
    if ID == "PASS":
        PASS_count = 0

    while(1):
        line = f.readline().strip()
        if line == "": break
        elif line[0] == "#":
            continue
        else:
            if ID == "NC":
                if ID in line:
                    try:
                        if ID in line[line.index("GENEINFO"):].split(":")[0]:continue
                    except:
                        print(line)
                        print(line.index(ID))
            
            if ID == ";AF=":
                if ID in line:
                    print(line)

            if ID == "PASS":
                if ID in line:
                    PASS_count += 1

            if ID == "ASP":
                if ID in line:
                    print(line)

            if ID == "ASS":
                try:
                    if ID in line[line.index("PASS")+4:] and ID not in line[line.index("GENEINFO"):].split(":")[0]:
                        
                        print(line[line.index("GENEINFO"):].split(":")[0])
                        print(line)
                        print()
                except:
                    if ID in line[line.index("GENEINFO"):].split(":")[0]:
                        continue
                    print(line)
            
            if ID == "CDS":
                if ID in line:
                    print(line)
            
            if ID == "CFL":
                if ID in line:
                    print(line)

            if ID == "PM":
                if "TOPMED" in line:
                    continue
                elif "TOPMED" not in line and "PM" in line:
                    try:
                        if ID in line[line.index("GENEINFO"):].split(":")[0]:
                            continue
                        else: print(line)
                    except:
                        continue
            if ID in line: print(line)


    if ID == "PASS":
        return PASS_count


def get_ID_info_list(f, need_ID_list):
    while(1):
        line = f.readline().strip()
        if line == "": 
            break
        if "#" in line:
            try:
                ID = line[line.index("ID"):].split(",")[0][3:]
                if ID in need_ID_list:
                    print(line)
            except:
                continue
        if "PASS" in line:
            break




def main():
    # get vcf 4.1 ID
    vcf_old = "/home/bilab/khb/3_package/l_BisSNP/2_test/2_test_SNP_data/dbsnp_135.hg19.sort.vcf"
    # f = open(vcf_old, 'r')
    # ID_list = get_ID_list(f)[:56]
    # print(find_ID_writed(f, sys.argv[1]))
    need_ID_list = ['ASP', 'CFL', 'CLN', 'G5', 'G5A', 'GCF', 'GMAF', 'GNO', 'HD', 'KGPilot1', 'KGPilot123', 'LSD', 'MTP', 'NOV', 'OM','PH2', 'PM', 'PMC', 'RSPOS', 'RV', 'S3D', 'SAO', 'SCS', 'SLO', 'SSR', 'TPA', 'VC', 'VLD', 'VP', 'WGT', 'dbSNPBuildID']
    # get_ID_info_list(f, need_ID_list)
    
    # get vcf 4.2 ID
    vcf_new = "/home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/4_dbSNP/z2_extracted_Korea1K_from_dbSNP156_chraccession.vcf"
    # d = open(vcf_new, 'r')
    d_need_ID_list = ['RS', 'dbSNPBuildID', 'SSR', 'VC', 'NSF', 'NSM', 'NSN', 'SYN', 'U3', 'U5', 'DSS', 'INT', 'R3', 'R5', 'GNO', 'PUB', 'FREQ', 'COMMON', 'CLNHGVS', 'CLNVI', 'CLNORIGIN', 'CLNSIG', 'CLNDISDB', 'CLNDN', 'CLNREVSTAT', 'CLNACC']
    # print(find_ID_writed(d, sys.argv[1]))
    # d.close()

    print(set(need_ID_list) & set(d_need_ID_list))


main()
