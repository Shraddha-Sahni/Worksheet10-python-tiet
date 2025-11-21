# import tkinter as tk

# root = tk.Tk()
# root.title("Robot Control Panel")
# root.geometry("500x400")
# root.configure(bg="yellow")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# # Draw a black point at (100,100)
# canvas.create_oval(98, 98, 102, 102, fill="black")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# points = [(20,50), (100,120), (180,90), (250,150)]
# canvas.create_line(points, fill="blue", width=3)

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# point = canvas.create_oval(10, 190, 20, 200, fill="red")

# def move_point():
#     canvas.move(point, 5, 0)
#     root.after(50, move_point)

# move_point()
# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# # Robot body
# canvas.create_rectangle(200, 150, 300, 250, fill="gray")

# # Wheels
# canvas.create_oval(190, 240, 220, 270, fill="black")
# canvas.create_oval(280, 240, 310, 270, fill="black")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# robot = canvas.create_oval(240, 190, 260, 210, fill="green")

# def move_up():
#     canvas.move(robot, 0, -10)

# def move_down():
#     canvas.move(robot, 0, 10)

# def move_left():
#     canvas.move(robot, -10, 0)

# def move_right():
#     canvas.move(robot, 10, 0)

# frame = tk.Frame(root)
# frame.pack()

# tk.Button(frame, text="Up", command=move_up).grid(row=0, column=1)
# tk.Button(frame, text="Left", command=move_left).grid(row=1, column=0)
# tk.Button(frame, text="Right", command=move_right).grid(row=1, column=2)
# tk.Button(frame, text="Down", command=move_down).grid(row=2, column=1)

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# ball = canvas.create_oval(185, 135, 215, 165, fill="blue")

# dx, dy = 3, 3

# def move_ball():
#     global dx, dy
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)

#     if x1 <= 0 or x2 >= 500:
#         dx = -dx
#     if y1 <= 0 or y2 >= 400:
#         dy = -dy

#     root.after(30, move_ball)

# move_ball()
# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# robot = canvas.create_oval(45, 195, 55, 205, fill="red")

# def move_robot():
#     canvas.move(robot, 5, 0)
#     x1, y1, x2, y2 = canvas.coords(robot)
#     if x2 < 450:
#         root.after(50, move_robot)

# move_robot()
# root.mainloop()


# import tkinter as tk
# import math

# root = tk.Tk()
# root.title("Four-Bar Mechanism")
# canvas = tk.Canvas(root, width=600, height=500, bg="white")
# canvas.pack()

# A = (150, 300)
# D = (400, 300)
# L2 = 120
# L3 = 150
# L4 = 130
# theta = math.radians(30)

# Bx = A[0] + L2 * math.cos(theta)
# By = A[1] - L2 * math.sin(theta)
# B = (Bx, By)

# dx = D[0] - B[0]
# dy = D[1] - B[1]
# d = math.sqrt(dx**2 + dy**2)

# a = (L3**2 - L4**2 + d**2) / (2*d)
# h = math.sqrt(abs(L3**2 - a**2))
# xm = B[0] + a * dx / d
# ym = B[1] + a * dy / d
# rx = -dy * (h/d)
# ry = dx * (h/d)

# Cx1 = xm + rx
# Cy1 = ym + ry
# Cx2 = xm - rx
# Cy2 = ym - ry
# C = (Cx1, Cy1)

# canvas.create_line(A[0], A[1], B[0], B[1], fill="red", width=3)
# canvas.create_line(B[0], B[1], C[0], C[1], fill="blue", width=3)
# canvas.create_line(C[0], C[1], D[0], D[1], fill="green", width=3)
# canvas.create_line(A[0], A[1], D[0], D[1], fill="black", width=3)

# for (x,y) in [A,B,C,D]:
#     canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("Robot Path Simulation")
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()

# robot = canvas.create_oval(240, 190, 260, 210, fill="red")
# last_pos = (250, 200)

# def move_robot(dx, dy):
#     global last_pos
#     canvas.move(robot, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(robot)
#     cx, cy = (x1+x2)/2, (y1+y2)/2
#     canvas.create_line(last_pos[0], last_pos[1], cx, cy, fill="blue")
#     last_pos = (cx, cy)

# def reset():
#     global last_pos, robot
#     canvas.delete("all")
#     robot = canvas.create_oval(240, 190, 260, 210, fill="red")
#     last_pos = (250, 200)

# root.bind("<Up>", lambda e: move_robot(0, -5))
# root.bind("<Down>", lambda e: move_robot(0, 5))
# root.bind("<Left>", lambda e: move_robot(-5, 0))
# root.bind("<Right>", lambda e: move_robot(5, 0))

# btn = tk.Button(root, text="RESET", command=reset)
# btn.pack()

# root.mainloop()