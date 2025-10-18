class ReadAndWrite:

    @staticmethod
    def read_file():
        # 用`open`函数打开文本文件时，需要指定文件名并将文件的操作模式设置为`'r'`
        # ，如果不指定，默认值也是`'r'`；如果需要指定字符编码，
        # 可以传入`encoding`参数，如果不指定，默认值是None，
        # 那么在读取文件时使用的是操作系统默认的编码。需要提醒大家，
        # 如果不能保证保存文件时使用的编码方式与`encoding`参数指定的编码方式是一致的，
        # 那么就可能因无法解码字符而导致读取文件失败。
        file = open('D:/AAA/aaa.txt', 'r', encoding='utf-8')
        print(file.read())
        file.close()

    @staticmethod
    def read_lines():
        print("方式一：使用`for-in`循环逐行读取")
        file = open('D:/AAA/aaa.txt', 'r', encoding='utf-8')
        for line in file:
            print(line, end='')
        file.close()

        print("方式二：用`readlines`方法将文件按行读取到一个列表容器中")
        file = open('D:/AAA/aaa.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            print(line, end='')
        file.close()

    @staticmethod
    def write_file():
        # a表示追加，将内容写入到已有文件的末尾
        file = open('D:/AAA/aaa.txt', 'a', encoding='utf-8')
        file.write('\n标题：《致橡树》')
        file.write('\n作者：舒婷')
        file.write('\n时间：1977年3月')
        file.close()

    @staticmethod
    def file_error_handle():
        file = None
        try:
            file = open('D:/AAA/aaa1.txt', 'r', encoding='utf-8')
            print(file.read())
        except FileNotFoundError:
            print('无法打开指定的文件！')
        except LookupError:
            print('指定了未知的编码')
        except UnicodeDecodeError:
            print('读取文件时解码错误！')
        finally:
            if file:
                file.close()

    @staticmethod
    def auto_close_file():
        with open('D:/AAA/aaa.txt', 'r', encoding='utf-8') as file:
            print(file.read())

        if file.closed:
            print("文件流已经被自动关闭")

    @staticmethod
    def copy_file1():
        file1_path = 'D:/AAA/aaa.txt'
        file2_path = 'D:/AAA/aaa2.txt'
        try:
            with open(file1_path, 'rb') as file1:
                data = file1.read()
            with open(file2_path, 'wb') as file2:
                file2.write(data)
        except FileNotFoundError:
            print('指定的文件无法打开.')
        except IOError:
            print('读写文件时出现错误.')

        print('文件复制完成')

    @staticmethod
    def copy_file2():
        """如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，
        为了减少对内存的占用，可以为`read`方法传入`size`参数来指定每次读取的字节数，
        通过循环读取和写入的方式来完成上面的操作，代码如下所示。"""
        file1_path = 'D:/AAA/aaa.txt'
        file2_path = 'D:/AAA/aaa2.txt'
        with open(file1_path, 'rb') as file1, open(file2_path, 'wb') as file2:
            data = file1.read(512)
            while data:
                file2.write(data)
                data = file1.read(512)
        print('文件复制完成')


if __name__ == '__main__':
    # ReadAndWrite.read_file()
    # ReadAndWrite.read_lines()
    # ReadAndWrite.write_file()
    # ReadAndWrite.file_error_handle()
    # ReadAndWrite.auto_close_file()
    # ReadAndWrite.copy_file1()
    ReadAndWrite.copy_file2()
