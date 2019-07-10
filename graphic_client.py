import tkinter as tk

def _create_circle(self, x, y, r, **kwargs):
    """  ref 
https://stackoverflow.com/questions/17985216/draw-circle-in-tkinter-python
    """
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle


def redraw_all(canvas, data):
    for (i, ball) in enumerate(data.ball_list):
        canvas.create_circle(ball.pos[0] * data.zoom_index, 
            ball.pos[1] * data.zoom_index, ball.r * data.zoom_index,
            outline="", fill=data.color_list[i])

def timer_fired(data):
    if not data.is_paused:
        pos_info = data.f.readline().split(";")
        if pos_info == [""]:
            data.is_paused = True
            return
        # positions are stored as "(x,y,z)"
        pos = [s[1:-1].split(",") for s in pos_info]
        for (i, ball) in enumerate(data.ball_list):
            ball.pos = list(map(float, pos[i]))


def init_zoom(data):
    data.zoom_index = data.width / data.container.x

def run_tk(data, width=600, height=600):
    """
    the visualization now only works with 2d collision,
    and the container should be approximately square
    """

    def redraw_all_wrapper(canvas, data):
        canvas.delete("all")
        redraw_all(canvas, data)
        canvas.update()    

    def timer_fired_wrapper(canvas, data):
        timer_fired(data)
        redraw_all_wrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timer_delay, timer_fired_wrapper, canvas, data)
        
    # Set up data
    data.width = width
    data.height = height
    data.timer_delay = 35 # milliseconds
    data.is_paused = False
    data.color_list = ["blue", "red", "yellow", "green", "red",]

    init_zoom(data)

    data.f = open(data.res_filename, "r")

    # create the root and the canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    timer_fired_wrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    data.f.close()