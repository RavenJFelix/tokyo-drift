import tkinter as tk
import robot as r
import vectorz as vec


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
# 
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Fuck\n Don't click"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
# 
#         self.quit = tk.Button(self, text="FUCK NO", fg="red",
#                               command=self.master.destroy)
# 
#         self.quit.pack(side="bottom")
# 
#     def say_hi(self):
#         print("fuck fuck fuck I hope this works")
# 

#class Example(tk.Frame):
#
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.initUI()
#
#    def initUI(self):
#        self.master.title("Lines")
#        self.pack(fill=tk.BOTH, expand=1)
#
#        canvas = tk.Canvas(self)
#        canvas.create_line(15, 15, 200, 25)
#        canvas.create_line(300, 25, 300, 200, dash=(4, 2))
#        canvas.create_rectangle(30, 10, 100, 100, fill='blue')
#
#        canvas.pack(fill=tk.BOTH, expand=1)


def main():
    root = tk.Tk()
    root.title("Fucking robot awesome")
    root.resizable(0, 0)
    root.wm_attributes("-topmost", 1)
    canv = tk.Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
    canv.pack()
    robot = r.Robot(vec.Vec2d(199, 100), vec.Vec2d(200, 290), canv)
    print(robot.size)
    robot.draw()

    # print(robot._generate_body_points()[1])
    # ex = Example(master=root)
    root.update()
    root.mainloop()


main()


#root = tk.Tk()
#app = Application(master=root)
#app.mainloop()

