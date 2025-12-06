with open("output.txt", "r") as f:
    content = f.read()
    lines = content.split("\n")
    lines = lines[0:len(lines)-1]
    print(lines)
    print(content)
    
    for line in lines:
        print(line)