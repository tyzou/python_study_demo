
import random
from PIL import Image, ImageDraw, ImageFont,ImageFilter



class Demo001:

    @staticmethod
    def demo1():
        print('----------------读取图像获得Image对象-------------------')
        # 读取图像获得Image对象
        image = Image.open('temp_file/1751031763020.jpg')
        # 通过Image对象的format属性获得图像的格式
        print("图像的格式:", image.format)  # JPEG
        # 通过Image对象的size属性获得图像的尺寸
        print("图像的尺寸:", image.size)  # (500, 750)
        # 通过Image对象的mode属性获取图像的模式
        print("图像的模式:", image.mode)  # RGB
        # 通过Image对象的show方法显示图像
        image.show()

    @staticmethod
    def demo2():
        print('----------------剪裁图像-------------------')
        # 读取图像获得Image对象
        image = Image.open('temp_file/1751031763020.jpg')
        # 通过Image对象的crop方法指定剪裁区域剪裁图像
        image.crop((80, 20, 310, 360)).show()
    @staticmethod
    def demo3():
        print('----------------生成缩略图-------------------')
        image = Image.open('temp_file/1751031763020.jpg')
        # 通过Image对象的thumbnail方法生成指定尺寸的缩略图
        image.thumbnail((300, 300))
        image.show()

    @staticmethod
    def demo4():
        print('----------------缩放和黏贴图像-------------------')

        # 读取骆昊的照片获得Image对象
        luohao_image = Image.open('temp_file/1751031763020.jpg')
        # 读取吉多的照片获得Image对象
        guido_image = Image.open('temp_file/1751031763022.jpg')
        # 从吉多的照片上剪裁出吉多的头
        guido_head = guido_image.crop((80, 20, 310, 360))
        width, height = guido_head.size
        # 使用Image对象的resize方法修改图像的尺寸
        # 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
        luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
        luohao_image.show()

    @staticmethod
    def demo5():
        print('----------------旋转和翻转-------------------')
        image = Image.open('temp_file/1751031763020.jpg')
        # 使用Image对象的rotate方法实现图像的旋转
        image.rotate(45).show()
        # 使用Image对象的transpose方法实现图像翻转
        # Image.FLIP_LEFT_RIGHT - 水平翻转
        # Image.FLIP_TOP_BOTTOM - 垂直翻转
        image.transpose(Image.FLIP_TOP_BOTTOM).show()

    @staticmethod
    def demo6():
        print('----------------操作像素-------------------')
        image = Image.open('temp_file/1751031763020.jpg')
        for x in range(80, 310):
            for y in range(20, 360):
                # 通过Image对象的putpixel方法修改图像指定像素点
                image.putpixel((x, y), (128, 128, 128))
        image.show()

    @staticmethod
    def demo6():
        print('----------------滤镜效果-------------------')
        image = Image.open('temp_file/PixPin_2024-11-19_23-31-24.png')
        # ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
        image.filter(ImageFilter.CONTOUR).show()

    @staticmethod
    def demo7():
        print('----------------使用Pillow绘图-------------------')

        def random_color():
            """生成随机颜色"""
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            return red, green, blue

        width, height = 800, 600
        # 创建一个800*600的图像，背景色为白色
        image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
        # 创建一个ImageDraw对象
        drawer = ImageDraw.Draw(image)
        # 通过指定字体和大小获得ImageFont对象
        # font = ImageFont.truetype('Kongxin.ttf', 32)
        # 通过ImageDraw对象的text方法绘制文字
        # drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0), font=font)
        # 通过ImageDraw对象的line方法绘制两条对角直线
        drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
        drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
        xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
        # 通过ImageDraw对象的rectangle方法绘制矩形
        drawer.rectangle(xy, outline=(255, 0, 0), width=2)
        # 通过ImageDraw对象的ellipse方法绘制椭圆
        for i in range(4):
            left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
            drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
        # 显示图像
        image.show()
        # 保存图像
        image.save('temp_file/使用Pillow绘图.png')

if __name__ == '__main__':
    # Demo001.demo1()
    # Demo001.demo2()
    # Demo001.demo3()
    # Demo001.demo4()
    # Demo001.demo5()
    # Demo001.demo6()
    Demo001.demo7()
