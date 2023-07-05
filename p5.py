import tkinter as tk

class Human:
    def __init__(self,canvas:tk.Canvas,center_x,center_y,width, height, tag) -> None:
        self.canvas = canvas
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.speed = 3
        self.tag = tag


    def draw_human(self):
        # head
        head_r = self.height//6.5
        head_x1 = self.center_x - head_r
        head_y1 = self.center_y - self.height//2
        head_x2 = self.center_x + head_r
        head_y2 = head_y1 + head_r*2
        self.canvas.create_oval(head_x1, head_y1, head_x2, head_y2, outline='black',tag=self.tag)

        # body
        body_l = self.height//2.5
        body_x1 = self.center_x
        body_y1 = head_y2
        body_x2 = self.center_x
        body_y2 = head_y2 + body_l
        self.canvas.create_line(body_x1, body_y1, body_x2, body_y2, fill='black',tag=self.tag)

        # arms
        arm_w = self.width//2
        arm_h = self.height//7
        self.canvas.create_line(self.center_x, head_y2+arm_h, self.center_x +
                        arm_w, head_y2, fill='black',tag=self.tag)
        self.canvas.create_line(self.center_x, head_y2+arm_h, self.center_x -
                        arm_w, head_y2, fill='black',tag=self.tag)

        # legs
        leg_w = self.width//2
        self.canvas.create_line(self.center_x, body_y2, self.center_x+leg_w,
                        self.center_y+self.height//2, fill='black',tag=self.tag)
        self.canvas.create_line(self.center_x, body_y2, self.center_x-leg_w,
                        self.center_y+self.height//2, fill='black',tag=self.tag)


    def keep_moving_horizontally(self):
        self.canvas.update()
        w = self.canvas.winfo_width()
        self.center_x += self.speed
        self.center_x %= w

        self.canvas.delete(self.tag)
        self.draw_human()
        self.canvas.after(20,self.keep_moving_horizontally)


def main():
    

    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    human = Human(canvas,150, 150, 70, 100,'human')

    human.draw_human()
    human.keep_moving_horizontally()

    
    root.mainloop()


if __name__ == '__main__':
    main()
