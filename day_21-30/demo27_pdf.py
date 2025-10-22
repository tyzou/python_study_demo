import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


class Demo27:

    @staticmethod
    def demo1():
        print('----------------提取文本-------------------')

        reader = PyPDF2.PdfReader('temp_file/25诗词大会1.pdf')
        for page in reader.pages:
            print(page.extract_text())

    @staticmethod
    def demo2():
        print('----------------旋转pdf文件-------------------')

        reader = PyPDF2.PdfReader('temp_file/25诗词大会1.pdf')
        writer = PyPDF2.PdfWriter()

        for no, page in enumerate(reader.pages):
            if no % 2 == 0:
                # 旋转
                new_page = page.rotate(-90)
            else:
                # 旋转
                new_page = page.rotate(90)
            writer.add_page(new_page)

        with open('temp_file/25诗词大会——旋转版本.pdf', 'wb') as file_obj:
            writer.write(file_obj)

    @staticmethod
    def demo3():
        print('----------------加密PDF文件-------------------')

        reader = PyPDF2.PdfReader('temp_file/25诗词大会1.pdf')
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt('foobared')

        with open('temp_file/25诗词大会-加密版.pdf', 'wb') as file_obj:
            writer.write(file_obj)

    @staticmethod
    def demo4():
        print('----------------批量添加水印-------------------')

        reader1 = PyPDF2.PdfReader('XGBoost.pdf')
        reader2 = PyPDF2.PdfReader('watermark.pdf')
        writer = PyPDF2.PdfWriter()
        watermark_page = reader2.pages[0]

        for page in reader1.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        with open('temp.pdf', 'wb') as file_obj:
            writer.write(file_obj)

    @staticmethod
    def demo5():
        print('----------------创建PDF文件-------------------')
        pdf_canvas = canvas.Canvas('temp_file/auto_create.pdf', pagesize=A4)
        width, height = A4

        # 绘图
        image = canvas.ImageReader('temp_file/1751031763020.jpg')
        pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

        # 显示当前页
        pdf_canvas.showPage()

        # 注册字体文件
        # pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
        # pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/青呱石头体.ttf'))

        # 写字
        # pdf_canvas.setFont('Font2', 40)
        pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
        pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
        # pdf_canvas.setFont('Font1', 40)
        pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
        pdf_canvas.rotate(18)
        pdf_canvas.drawString(250, 250, 'hello, world!')

        # 保存
        pdf_canvas.save()
        print('pdf创建完成')


if __name__ == '__main__':
    # Demo27.demo1()
    # Demo27.demo2()
    # Demo27.demo3()
    # Demo27.demo4()
    Demo27.demo5()
