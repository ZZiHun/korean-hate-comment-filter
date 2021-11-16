import csv
with open("kocohub_labeled_data.csv") as file:
    new_file = open("kocohub_labeled_data.tsv", "w+")
    
    read_csv = csv.reader(file)
    for row in read_csv:
        if row[-1] == 'none':
            new_row = "".join([row[0],"\t","1"])
        else:
            new_row = "".join([row[0],"\t","0"])
        new_file.write(new_row)
        new_file.write("\n")
    new_file.close()

with open("hate_speech_refined.csv") as file:
    new_file = open("hate_speech_refined.tsv", "w+")

    read_csv = csv.reader(file)
    for row in read_csv:
        new_row = row[0].split(',')
        if new_row[-2] == "1":
            new_content = "".join([new_row[0],"\t","0"])
        else:
            new_content = "".join([new_row[0],"\t","1"])
        new_file.write(new_content)
        new_file.write("\n")
    new_file.close()