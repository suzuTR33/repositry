import json

class Point:
    def __init__(self,x,y,reliability) -> None:
        self.x = x
        self.y = y
        self.reliability = reliability

def load_data(path):
    with open(path) as f:
        data = json.load(f)
    
    points_raw = [d['pose_keypoints_2d'] for d in data['people']]
    persons = [[Point(pr[i],pr[i+1],pr[i+2]) for i in range(0,int(len(pr)/3),3)] for pr in points_raw]
    return persons
    

path = 'kabeposter/kabeposter_000000000000_keypoints.json'
persons = load_data(path)
parts = ['nose','neck']

for i,p in enumerate(persons):
    print(f'person {i}:')
    for j,part in enumerate(parts):
        print(f'\t{part}: x={p[j].x} y={p[j].y} r={p[j].reliability}')