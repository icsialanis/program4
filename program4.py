names = []
codes = []

def read_csv(kll):
    with open(kll, "r") as data_csv:
        lines = data_csv.readlines()
        return lines

def parse_csv(yuu):
    for i in yuu:
        new_list = i.split(",")
        names.append(new_list[0])
        codes.append(new_list[1])

def print_data():
    for i in range(len(names)):
        print("---------")
        print("names: " + names[i])
        print("codes: " + codes[i])


kll = read_csv("data.csv")
parse_csv(kll)
print_data()