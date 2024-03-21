import turtle

# 创建一个Turtle对象
t = turtle.Turtle()

# t.left, t.right, forward, speed(0)最快, color('red')， pensize, goto(1,2)
# penup(),pendown() 抬笔落笔跳过中间步骤

# speed:
# "fastest": 最快的速度，等同于0
# "fast": 较快的速度，等同于5
# "normal": 正常速度，等同于10
# "slow": 较慢的速度，等同于3
# "slowest": 最慢的速度，等同于1

###   part 1
# t.speed(5)
# t.color('red')
# t.pensize(3)

# t.circle(100)
# t.left(90)

# for i in range(12):
#     t.right(91)
#     t.circle(100+i)


###   part 2
# t.pensize(9)
# t.color('black')
# t.circle(75)

# t.penup()
# t.goto(-160,0)
# t.pendown()

# t.color('blue')
# t.circle(75)

# t.penup()
# t.goto(160,0)
# t.pendown()

# t.color('red')
# t.circle(75)

# t.penup()
# t.goto(80,-100)
# t.pendown()

# t.color('green')
# t.circle(75)

# t.penup()
# t.goto(-80,-100)
# t.pendown()

# t.color('yellow')
# t.circle(75)


###   part 3
# step 1
t.speed(0)
t.penup()
t.goto(0,-200)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(200)
t.end_fill()

# step 2
t.penup()
t.goto(0,-150)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(150)
t.end_fill()

# step 3
t.penup()
t.goto(0,-100)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

# step 4
t.penup()
t.goto(0,-50)
t.pendown()
t.color('blue')
t.begin_fill()
t.circle(50)
t.end_fill()

# step 5
t.penup()
t.goto(-40,10)
t.pendown()
t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()


# # save 
# canvas = t.getcanvas()
# canvas.postscript(file="my_drawing.eps")


# # convert to jpg # remeber pip install Pillow
# from PIL import Image

# # 打开EPS文件
# eps_file = "my_drawing.eps"
# img = Image.open(eps_file)

# # 将EPS文件转换为JPEG格式
# jpg_file = "my_drawing.jpg"
# img.save(jpg_file, "JPEG")

# # 关闭图像文件
# img.close()


#结束绘制
turtle.done()



### 指令集合：
# 基本移动指令：
# forward(distance): 向当前方向移动一定距离。
# backward(distance): 向相反方向移动一定距离。
# right(angle): 向右旋转一定角度。
# left(angle): 向左旋转一定角度。
# 画笔控制指令：
# penup(): 抬起画笔，移动时不绘制图形。
# pendown(): 落下画笔，移动时绘制图形。
# pensize(width): 设置画笔宽度。
# color(color): 设置画笔颜色。
# 海龟控制指令：
# speed(speed): 设置海龟移动速度。
# shape(shape): 设置海龟的形状。
# 图形控制指令：
# circle(radius): 绘制一个圆形。
# dot(size): 在当前位置绘制一个点。
# begin_fill(): 开始填充图形。
# end_fill(): 结束填充图形。
# 其他指令：
# reset(): 重置海龟图形窗口。
# clear(): 清除海龟绘制的图形，但不移动海龟。
# done(): 等待图形窗口关闭。

# 其他可尝试help(turtle)查看