import math
import json

path = 'catalog.json'

jcnt = 0
jmax = -math.inf
jmin = math.inf


with open(path,'r') as f:
    dl = json.load(f)

for d in dl:
    if(d['name'] == 'jacket'):
        jcnt += 1
        jmax = max(jmax,d['price'])
        jmin = min(jmin,d['price'])

print(f'個数 = {jcnt}\n最高価格 = {jmax}\n最低価格 = {jmin}')