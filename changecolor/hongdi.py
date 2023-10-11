import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import font

def replace_background():
    # 弹出文件对话框，选择图片文件
    file_path = filedialog.askopenfilename()

    if not file_path:
        print("未选择文件，程序退出")
        return

    # 读取照片
    img = cv2.imread(file_path)

    # 图像缩放——可选
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # 打印图片的信息————分辨率、图片通道
    rows, cols, channels = img.shape
    print(("图片分辨是：%s*%s  此图片是%s通道") % (rows, cols, channels))
    cv2.imshow('img', img)

    # 图片转换为灰度图
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)

    # 图片的二值化处理
    lower_blue = np.array([85, 70, 70])  # [85,70,70]
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 先膨胀，再腐蚀
    dilate = cv2.dilate(mask, None, iterations=1)
    cv2.imshow('dilate', dilate)

    erode = cv2.erode(dilate, None, iterations=1)
    cv2.imshow('erode', erode)

    # 遍历替换
    for i in range(rows):
        for j in range(cols):
            if erode[i, j] == 255:
                img[i, j] = (0, 0, 255)  # 红色底部--此处替换颜色，为BGR通道，不是RGB通道
    cv2.imshow('res', img)

    # 保存图片 可以以png、jpg、bmp方式保存，默认是以.png保存
    output_path = 'output_picture_red.png'
    s = cv2.imwrite(output_path, img)
    if s > 0:
        print("图片底色替换为红色，并保存成功！！")

    # 其他格式保存图片：
    # s = cv2.imwrite('output_picture2.jpg', img)
    # s = cv2.imwrite('output_picture3.bmp', img)

    # 键盘上按下q键退出
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()

# 创建UI界面
root = tk.Tk()
root.title("红底")

# 设置窗口大小
root.geometry("600x400")

# 创建 Frame 放置按钮
frame = tk.Frame(root, bg="lightgrey")
frame.pack(expand=True)
frame.place(relx=0.5, rely=0.5, anchor="center")

# 定义按钮样式
btn_style = {'font': font.Font(family="Arial", size=16),
             'bg': 'red',
             'fg': 'white',
             'activebackground': 'darkred',
             'activeforeground': 'white'}

# 添加按钮
btn = tk.Button(frame, text="开始替换底色", command=replace_background, **btn_style)
btn.pack()

# 添加标签
label = tk.Label(root, text="504巨献", font=font.Font(family="Helvetica", size=24), bg="lightgrey")
label.place(relx=0.5, rely=0.01, anchor="n")

root.mainloop()