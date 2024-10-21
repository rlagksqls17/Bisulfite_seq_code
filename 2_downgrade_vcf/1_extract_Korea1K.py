f = open("/home/bilab/khb/8_TF_Methylation_Colon_Cancer/1_database/4_dbSNP/dbSNP_156.vcf", 'r')


Korea1K_count = 0 
case1_count = 0
case2_count = 0
case3_count = 0
case4_count = 0
case5_count = 0
case6_count = 0
case7_count = 0
case8_count = 0
case9_count = 0
case10_count = 0
case11_count = 0

a_count = 0
b_count = 0
c_count = 0
d_count = 0

while (1):
    line = f.readline().strip()
    if line == "": break

    if "#" in line[0]:
        print(line.strip())
    elif "Korea1K" in line:
        Korea1K_count += 1
        line = line.strip()
        MAF = -0.99999
        Korea1K_line = line[line.index("Korea1K"):]
        if "|" in Korea1K_line:
            case1_count += 1

            MAF_pre1 = ",".join(Korea1K_line.split("|")[0].split(",")[1:])
            MAF_pre2 = ""
            try: 
                MAF_pre2 = MAF_pre1[MAF_pre1.index('0.'):]
                case3_count += 1
            except:
                if Korea1K_line.split("|")[0].split(",")[0] == "Korea1K:1":
                    MAF_pre2 = '0'
                    case4_count += 1
                else:
                    MAF_pre2 = '1'
                    case5_count += 1
            
            MAF_pre3 = ""
            try: 
                MAF_pre3 = float(MAF_pre2.split(",")[0])
                case6_count += 1
            except:
                if ";" in MAF_pre2: 
                    MAF_pre3 = float(MAF_pre2.split(";")[0])
                    case7_count += 1

            """
            if MAF_pre3 >= 0.01:
                print(line)
            """
        else:
            case2_count += 1

            MAF_pre1 = ""
            split_list = Korea1K_line.split(",")
            if split_list[0] != "Korea1K:.":
                MAF_pre1 = ",".join(split_list[1:])
                case8_count += 1
            elif split_list[0] == "Korea1K:.":
                MAF_pre1 = ",".join(split_list[2:])
                print(Korea1K_line)
                case9_count += 1
            MAF_pre2 = ""
            
            try:
                MAF_pre2 = MAF_pre1[MAF_pre1.index("0"):]
                case10_count += 1
            except: 
                MAF_pre2 = MAF_pre1[MAF_pre1.index("1"):]
                case11_count += 1
            MAF_pre3 = ""

            if ",." in MAF_pre2:
                try:
                    MAF_pre3 = float(MAF_pre2.split(",.")[0])
                    a_count += 1
                except: 
                    MAF_pre3 = float(MAF_pre2.split(",.")[0].split(";")[0])
                    b_count += 1
                if MAF_pre3 >= 0.01:
                    a=0
                    #print(line)
            elif ";" in MAF_pre2:
                MAF_pre3 = float(MAF_pre2.split(";")[0])
                c_count += 1
                if MAF_pre3 >= 0.01:
                    a=0
                    #print(line)
            else:
                MAF_pre3 = float(MAF_pre2)
                d_count += 1
                if MAF_pre3 >= 0.01:
                    a=0
                    #print(line)
    if line == "": break
   


print(a_count)
print(b_count)
print(c_count)
print(d_count)
