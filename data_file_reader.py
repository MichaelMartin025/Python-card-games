#scan data.file

ace1 = 0
ace2 = 0
ace3 = 0
ace4 = 0

with open("data.txt", "r") as data_in:
    for e,line in enumerate(data_in):
        #print(f"Line: {e+1}: result: {line}")
        if "Aces=1" in line:
            ace1 += 1
        if "Aces=2" in line:
            ace2 += 1
        if "Aces=3" in line:
            print(e+1,line)
            ace3 += 1
        if "Aces=4" in line:
            ace4 += 1

print(e+1,ace1,ace2,ace3,ace4)