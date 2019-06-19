import tkinter as tk

def redraw_all(data):
    pass

def timer_fired(data):
    pos_info = data.f.readline().split(";")


def run_tk(data, width=600, height=600):
    def redraw_all_wrapper(canvas, data):
        canvas.delete(ALL)
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
    data.timer_delay = 100 # milliseconds
    data.is_paused = False
    data.color_list = ["blue", "red", ]

    data.f = open(data.res_filename, "r")

    # create the root and the canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    timer_fired_wrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    data.f.close()