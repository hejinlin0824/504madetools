# 504madetools
这是一个小功能合集，由504开发，将以前做的各个小件集合成一个实用包，目前还在 开发中，又贪吃蛇测试例，记账程序，英文word翻译汉语word程序，证件照换底程序。当我开发完所有功能后，会逐个对各个项目进行优化升级，包括UI界面，以及交互感受，就当这是我一个进入工业革命时代后的乐趣项目吧，希望对大家有帮助。将持续开发，供和我一样的小白一起学习进步，一起为开源事业做贡献！
Chapter 1
（如果你已经装过python环境了，请直接chapter2）
使用说明：首先请确保你的电脑安装了python环境，安装地址：python.org
 
下拉选单：
 
选择python3.9，最稳定一些，然后点击下载。
下载完后是这样（因为我已经下载了，我用csdn上图来做解释：）：
 

接下来是： 
 
个人建议不要放在系统盘，在D盘或者其他盘新建文件夹放入即可。
接下来图片见下：
 
点击close安装成功。


验证安装成功：win+R呼出CMD：


 


点击确认，弹出终端框，此时输入python，点击回车，出现这样的界面及安装成功：
 
此时输入exit()，注意，一定是英文括号，你将又回到终端界面，
 
首先输入：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
此行代码会让你下载速度飞快，因为将国内清华镜像添加为默认包下载源。
环境配置基本结束。
·如果你想玩贪吃蛇游戏，那就输入这行代码：
pip install pygame
·如果你想进行记账：
pip install tkinter回车等待结束
pip install matplotlib回车等待结束
pip install pandas 回车等待结束

如果你想照片换底：
pip install cv2
pip install numpy
pip install tkinter
如果终端显示缺什么你就pip install 什么，直接win+R叫出cmd即可直接pip

如果你想翻译英文word，我希望你先别用，因为我的API收费太贵了，我只有50元，算了你先别用，我哪天改成百度API。
至此，程序基本环境没有问题。

