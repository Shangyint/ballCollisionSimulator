import ball, container, graphic_client
import numpy as np
import json, os, itertools
# import tkinter as tk

#############################
##### temp data section #####

# x_max, y_max = 1000
# dimension = 2
# ball_number = 2

# ball_a = ball()

##### only for debuging #####
#############################

def parse_json(filename):
    # json_s = ""
    f = open(filename, "r")
        # json_s = f.read()
    return json.load(f)

def find_file_name():
    res = 0
    while True:
        if os.path.isfile("data_out" + str(res)):
            res += 1
        else:
            return res

def init_other(input_data, data):
    """
    """
    data.time_stamp = input_data["time_stamp"]
    data.time_limit = input_data["time_limit"]
    data.precision = input_data["precision"]
    data.res_filename = "data_out" + str(find_file_name())

def init_container(input_data, data):
    """
    """
    data.container = container.Container(input_data["container"])

def init_balls(input_data, data):
    """

    """
    data.ball_list = []
    for i in range(1, input_data["ball_number"] + 1):
        data.ball_list.append(ball.Ball(input_data["ball"+str(i)]))

def run(data):
    precision = data.precision
    container = data.container
    f = open(data.res_filename, "w")
    for _ in range(int(data.time_limit//data.time_stamp)):
        # update ball position
        for ball in data.ball_list:
            ball.update(data.time_stamp)
            # check coordinates with the boundary of the container
            for i in range(len(ball.pos)):
                # check upper bound
                if ball.pos[i] > container.upper_bound[i] - ball.r:
                    ball.v[i] *= -1
                    ball.pos[i] = container.upper_bound[i] - ball.r
                # check lower bound
                if ball.pos[i] < ball.r:
                    ball.v[i] *= -1
                    ball.pos[i] = ball.r

        # check for collision between balls
        for pair in itertools.combinations(data.ball_list, 2):
            ball1 = pair[0]
            ball2 = pair[1]

            # TODO
            if np.linalg.norm(ball1.pos - ball2.pos) <= ball1.r + ball2.r:
                # change speed
                ball1.v *= -1
                ball2.v *= -1

        for ball in data.ball_list:
            f.write("(" + ",".join([str(round(coo, precision)) for coo in ball.pos]) + ");")
        f.write("\n")

    f.close()

def init(input_data, data):
    init_container(input_data, data)
    init_balls(input_data, data)
    init_other(input_data, data)

def main():
    # filename = input()
    filename = "input.json"
    input_data = parse_json(filename)
    class Struct(object): pass
    data = Struct()
    init(input_data, data)
    
    run(data)
    if data.container.dimension == 2:
        graphic_client.run_tk(data)

if __name__ == '__main__':
    main()