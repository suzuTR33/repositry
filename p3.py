result = 0

for i in range(1,1000,2):
    path = 'sample/kitamura_'+str(i).zfill(5)+'_kgu.txt'
    with open(path,'r') as f:
        txt = f.readlines()
    try:
        result += int(txt[0])
    except ValueError:
        pass

print(result)