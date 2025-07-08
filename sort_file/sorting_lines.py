fname = input("Enter the filename whose contents are to be sorted: ")

with open(fname, "r") as infile:
    lineList = [line.strip() for line in infile.readlines()]

lineList.sort()

with open("sorted.txt", "w") as outfile:
    for line in lineList:
        outfile.write(line + "\n")

print("Sorted content saved to 'sorted.txt'")
