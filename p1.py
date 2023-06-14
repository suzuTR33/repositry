path = 'data.txt'
result = 0

with open(path) as f:
    txt = f.readlines()

for l in txt:
    try:
        
        result += int(l)
    except ValueError:
        pass


print(result)