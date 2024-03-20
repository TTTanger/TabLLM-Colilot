import gradio as gr
import cv2
from paddleocr import PaddleOCR
import pythoncom
import pandas as pd
import fitz
from PIL import Image
import os
import win32com.client as win32


def word_to_pdf(word_rel_path):
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 拼接相对路径和当前目录，得到完整的Word文件路径
    word_abs_path = os.path.join(script_dir, word_rel_path)

    # 初始化Word应用
    word = win32.Dispatch("Word.Application")
    word.Visible = False  # 设置Word应用为不可见

    # 打开Word文档
    doc = word.Documents.Open(word_abs_path)

    # 指定PDF文件的保存路径和文件名
    pdf_path = os.path.join(script_dir, "output.pdf")

    # 保存为PDF
    doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat=17 表示PDF格式

    # 关闭Word文档
    doc.Close(False)

    # 退出Word应用
    word.Quit()

    return pdf_path


def pdf_to_image(file_path):
    output_folder = "images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # 创建输出文件夹
    try:
        doc = fitz.open(file_path)
        images = []
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(image)
        doc.close()

        # 拼接图像
        combined_image = Image.new("RGB", (images[0].width, sum(image.height for image in images)))
        y_offset = 0
        for image in images:
            combined_image.paste(image, (0, y_offset))
            y_offset += image.height

        # 保存拼接后的图像
        combined_image_path = f"{output_folder}\\file_image.png"
        combined_image.save(combined_image_path)

    except Exception as e:
        print("无法转换PDF为图像:", str(e))

    return combined_image_path


def excel_to_dataframe(file):

    # 指定Excel文件的路径
    excel_path = file

    # 使用pandas的read_excel函数读取Excel文件
    df = pd.read_excel(excel_path)
    print(df)
    # 显示DataFrame的内容
    return df


def file_extension(file):
    filename = file.name
    if "." in filename:
        return filename.rsplit(".", 1)[1]
    else:
        return None


def file_convert(files):
    pythoncom.CoInitialize()
    final_df = pd.DataFrame()
    # 使用默认模型
    paddleocr = PaddleOCR(lang='ch', show_log=False)
    result_dfs = []  # 创建一个空列表来存储结果的DataFrame
    for file in files:
        # Default value set to None
        file_img = None
        file_ex = file_extension(file)
        if file_ex == 'docx' or file_ex == 'doc' or file_ex == 'pdf':
            if file_ex == 'docx' or file_ex == 'doc':
                file_pdf = word_to_pdf(file)
                file_img = pdf_to_image(file_pdf)
                print(file_img)
                os.remove(file_pdf)

            elif file_ex == 'pdf':
                file_img = pdf_to_image(file)

            if file_img is not None:
                # 打开image文件
                img = cv2.imread(file_img)
                result = paddleocr.ocr(img)
                if result is not None and len(result) > 0:
                    alist = []
                    for i in range(len(result[0])):
                        alist.append(result[0][i][1][0])
                    print(alist)
                    # Convert the result to a DataFrame
                    file_df = pd.DataFrame({'识别结果': alist})
                    result_dfs.append(file_df)  # 将当前文件的DataFrame追加到列表中
                    print("Succeeded in transforming")
                    # 删除临时文件
                    os.remove(file_img)
                else:
                    print("Failed in transforming")

        elif file_ex == 'xlsx':
            file_df = excel_to_dataframe(file)
            result_dfs.append(file_df)  # 将当前文件的DataFrame追加到列表中
    final_df = pd.concat(result_dfs)

    return final_df


iface = gr.Interface(file_convert, gr.File(file_count="multiple",), gr.Dataframe(), title="表格转换器", live=True,)
iface.launch()
