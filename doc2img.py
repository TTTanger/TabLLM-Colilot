from PIL import Image, ImageDraw, ImageFont
import docx


def read_docx_lines(file_path):
    # 初始化一个空列表来存储行
    lines = []

    # 读取DOCX文件
    doc = docx.Document(file_path)

    # 遍历段落并将每个段落添加到列表中
    for para in doc.paragraphs:
        lines.append(para.text)

    return lines


# 创建一个白色背景的空白图像
width, line_height = 1000, 60
docx_file_path = "git.docx"
lines_list = read_docx_lines(docx_file_path)
font_size = 20
font = ImageFont.truetype("arial.ttf", font_size)
line_spacing = 20
text_x, text_y = 10, 40

# 计算图像高度
height = len(lines_list) * line_height

image = Image.new("RGB", (width, height), "white")

# 初始化绘图上下文
draw = ImageDraw.Draw(image)
for line in lines_list:
    print(line)
    # 向图像添加文本
    text = line

    text_y = text_y + line_spacing
    draw.text((text_x, text_y), text, fill="black", font=font)

    # 将图像保存为 "text_image.png"
    image.save("text_image.png")
