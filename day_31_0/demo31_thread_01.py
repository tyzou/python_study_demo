import glob
import os
import threading
from PIL import Image

PREFIX = 'thumbnails'

class Demo001:
    """
    这是一个多线程批量图像缩略图生成工具，
    能自动将images目录下的PNG图片转换为32x32、64x64、128x128
    三种尺寸的缩略图并保存到thumbnails目录。
    """

    @staticmethod
    def generate_thumbnail(infile, size, format='PNG'):
        print('----------------生成指定图片文件的缩略图-------------------')
        """生成指定图片文件的缩略图"""
        file, ext = os.path.splitext(infile)
        file = file[file.rfind('\\') + 1:]
        outfile = f'{PREFIX}\\{file}_{size[0]}_{size[1]}{ext}'
        img = Image.open(infile)
        img.thumbnail(size, Image.LANCZOS)
        img.save(outfile, format)


    @staticmethod
    def run():
        print('----------------demo-------------------')
        """主函数"""
        if not os.path.exists(PREFIX):
            os.mkdir(PREFIX)
        for infile in glob.glob('images/*.png'):
            for size in (32, 64, 128):
                # 创建并启动线程
                threading.Thread(
                    target=Demo001.generate_thumbnail,
                    args=(infile, (size, size))
                ).start()




if __name__ == '__main__':
    Demo001.run()
