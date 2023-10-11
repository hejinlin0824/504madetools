import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import Button, Label
import math
import random

# 按钮点击事件处理函数
def button_click(button_num):
    if button_num == 1:
        # 运行snake.py文件
        subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/snake/snake.py"])
    elif button_num == 2:
        # 运行record.py文件
        subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/money/record.py"])
    elif button_num == 3:
        # 弹出确认窗口
        response = messagebox.askokcancel("确认", "请确保input.docx放入根目录")
        if response:
            # 运行test.py文件
            subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/translate/test.py"])
    elif button_num == 4:
        create_change_background_window()  # 新增按钮处理函数
    else:
        print(f"按钮 {button_num} 被点击了")

# 新的窗口用于切换底色
def create_change_background_window():
    change_background_window = tk.Tk()
    change_background_window.title("切换底色")

    # 切换底色按钮点击事件处理函数
    def change_background_color(color):
        if color == "红底":
            subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/changecolor/hongdi.py"])
        elif color == "白底":
            subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/changecolor/baidi.py"])
        elif color == "蓝底":
            subprocess.Popen(["python", "D:/PY_WorkSpace/anaconda_test/works/504app/changecolor/landi.py"])
        change_background_window.destroy()

    # 创建切换底色按钮
    red_button = Button(change_background_window, text="红底", width=10, height=2, command=lambda: change_background_color("红底"),
                        bg="red", font=("楷体", 18, "bold"), fg="white")
    white_button = Button(change_background_window, text="白底", width=10, height=2, command=lambda: change_background_color("白底"),
                          bg="white", font=("楷体", 18, "bold"), fg="black")
    blue_button = Button(change_background_window, text="蓝底", width=10, height=2, command=lambda: change_background_color("蓝底"),
                         bg="blue", font=("楷体", 18, "bold"), fg="white")

    red_button.pack(pady=10)
    white_button.pack(pady=10)
    blue_button.pack(pady=10)

    change_background_window.geometry("300x300")
    change_background_window.mainloop()

# 创建Tkinter窗口
root = tk.Tk()
root.title("504出品")

# 计算按钮位置
button_positions = []
button_count = 12
radius = 250
center_x = 400
center_y = 300

# 计算按钮之间的角度差
angle_increment = 2 * math.pi / button_count

for i in range(button_count):
    angle = i * angle_increment
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    button_positions.append((x, y))

# 创建标题标签
title_label = Label(root, text="504出品", font=("Helvetica", 38, "bold"), fg="#FF0000")
title_label.place(x=center_x - title_label.winfo_reqwidth() / 2, y=center_y - title_label.winfo_reqheight() / 2)

# 创建按钮
buttons = []
for i in range(1, 13):
    if i == 1:
        text = "贪吃蛇游戏"
        bg_color = "lightblue"
        text_color = "red"
        font_size = 18
    elif i == 2:
        text = "记账软件"
        bg_color = "lightcoral"
        text_color = "blue"
        font_size = 18
    elif i == 3:
        text = "翻译"
        bg_color = "lightgreen"
        text_color = "purple"
        font_size = 18
    elif i == 4:
        text = "换底"
        bg_color = f"#{random.randint(0, 0xFFFFFF):06x}"  # 随机颜色
        text_color = "black"
        font_size = 18
    else:
        text = f"按钮 {i}"
        bg_color = "lightgray"
        text_color = "black"
        font_size = 14

    button = Button(root, text=text, width=10, height=2, font=("楷体", font_size, "bold"),
                    command=lambda num=i: button_click(num), bg=bg_color, fg=text_color, relief=tk.RAISED, bd=4)

    # 使用修改后的按钮位置
    button.place(x=button_positions[i - 1][0] - button.winfo_reqwidth() / 2,
                 y=button_positions[i - 1][1] - button.winfo_reqheight() / 2)

# 设置窗口大小和位置
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 进入主事件循环
root.mainloop()