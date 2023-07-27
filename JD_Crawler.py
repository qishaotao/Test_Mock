# import os,re
#
# # 两个文件夹的路径
# folder1 = ".//tttttt/"
# folder2 = ".//sequence_files/"
#
# # 获取文件夹1中的所有文件名
# files_folder1 = set([file for file in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, file))])
#
# # 获取文件夹2中的所有文件名
# files_folder2 = set([file for file in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, file))])
#
# # 找出两个文件夹中不同的文件名
# different_files = files_folder1.symmetric_difference(files_folder2)
# # 打印不同的文件名
# for file in different_files:
#     pattern = r"-([0-9]+)\."
#     match_result = re.search(pattern,file)
#     print(match_result.group(1))
# print(len(different_files))
#

from PIL import Image, ImageDraw, ImageFont
import random

# 创建画布
canvas_width = 200
canvas_height = 100
canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')

# 创建绘图对象
draw = ImageDraw.Draw(canvas)

# 定义字符集合
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# 生成验证码字符串
code_length = 4
code = ''.join(random.sample(characters, code_length))

# 设置字体和字体大小
font_path = 'Picture/zh-hans.ttf'
font_size = 40
font = ImageFont.truetype(font_path, font_size)

# 设置字符位置
x = 10
y = 30

# 绘制字符
draw.text((x, y), code, font=font, fill='black')

# 绘制干扰线
for _ in range(5):
    x1 = random.randint(0, canvas_width)
    y1 = random.randint(0, canvas_height)
    x2 = random.randint(0, canvas_width)
    y2 = random.randint(0, canvas_height)
    draw.line((x1, y1, x2, y2), fill='black')

# 绘制干扰点
for _ in range(50):
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    draw.point((x, y), fill='black')

# 保存验证码图片
canvas.save('./Picture/captcha.png')








