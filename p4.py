import tkinter as tk


def draw_human(canvas, center_x, center_y, width, height):
    # head
    head_r = height//6.5
    head_x1 = center_x - head_r
    head_y1 = center_y - height//2
    head_x2 = center_x + head_r
    head_y2 = head_y1 + head_r*2
    canvas.create_oval(head_x1, head_y1, head_x2, head_y2, outline='black')

    # body
    body_l = height//2.5
    body_x1 = center_x
    body_y1 = head_y2
    body_x2 = center_x
    body_y2 = head_y2 + body_l
    canvas.create_line(body_x1, body_y1, body_x2, body_y2, fill='black')

    # arms
    arm_w = width//2
    arm_h = height//7
    canvas.create_line(center_x, head_y2+arm_h, center_x +
                       arm_w, head_y2, fill='black')
    canvas.create_line(center_x, head_y2+arm_h, center_x -
                       arm_w, head_y2, fill='black')

    # legs
    leg_w = width//2
    canvas.create_line(center_x, body_y2, center_x+leg_w,
                       center_y+height//2, fill='black')
    canvas.create_line(center_x, body_y2, center_x-leg_w,
                       center_y+height//2, fill='black')


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    draw_human(canvas, 150, 150, 70, 100)
    root.mainloop()


if __name__ == '__main__':
    main()
