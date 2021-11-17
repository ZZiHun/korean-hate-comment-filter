import csv
with open("labeled.csv") as file:
    new_file = open("labeled.tsv", "w+")

    read_csv = csv.reader(file)
    for row in read_csv:
        new_row = row[0].split(',')
        if new_row[-1] == '0':
            new_content = "".join([new_row[0],"\t","1"])    # 0이면 사람
        else:
            new_content = "".join([new_row[0],"\t","0"])    # 1, 2 면 욕 및 차별성 발언
        new_file.write(new_content)
        new_file.write("\n")
    
    new_file.close()


