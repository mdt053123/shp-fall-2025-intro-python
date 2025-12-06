with open("file.txt", "w") as f:
    f.write("line1\n")
    f.write("line2\n")
    f.write("line3\n")
    
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())