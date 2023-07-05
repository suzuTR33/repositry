import json
import tkinter as tk

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
    



def main():
    connection = [(1,2),(1,5)]
    path = 'kabeposter/kabeposter_000000000000_keypoints.json'
    persons = load_data(path)
    scale = 0.4
    

    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=500)
    canvas.pack()

    for p in persons:
        for c in connection:
            canvas.create_line(p[c[0]].x*scale, p[c[0]].y*scale, p[c[1]].x*scale, p[c[1]].y*scale)


    
    root.mainloop()


if __name__ == '__main__':
    main()