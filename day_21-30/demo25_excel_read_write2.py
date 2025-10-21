import datetime
import random

import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

class Demo001:

    @staticmethod
    def demo1():
        print('----------------读取Excel文件-------------------')
        # 加载一个工作簿 ---> Workbook
        wb = openpyxl.load_workbook('temp_file/二审确定名单(1).xlsx')
        # 获取工作表的名字
        print(wb.sheetnames)
        # 获取工作表 ---> Worksheet
        sheet = wb.worksheets[0]
        # 获得单元格的范围
        print(sheet.dimensions)
        # 获得行数和列数
        print(sheet.max_row, sheet.max_column)

        # 获取指定单元格的值
        print(sheet.cell(3, 3).value)
        print(sheet['C3'].value)
        print(sheet['G255'].value)

        # 获取多个单元格（嵌套元组）
        print(sheet['A2:C5'])

        print('读取文件所有内容：')
        for row_ch in range(2, sheet.max_row + 1):
            for col_ch in 'ABCDEFG':
                value = sheet[f'{col_ch}{row_ch}'].value
                print(value, end='\t')
            print()

    @staticmethod
    def demo2():
        print('----------------写Excel文件-------------------')
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = '期末成绩'
        titles = ('姓名', '语文', '数学', '英语')
        for col_index, title in enumerate(titles):
            sheet.cell(1, col_index + 1, title)

        names = ('关羽', '张飞', '赵云', '马超', '黄忠')
        for row_index, name in enumerate(names):
            sheet.cell(row_index + 2, 1, name)
            for col_index in range(2, 5):
                sheet.cell(row_index + 2, col_index, random.randrange(50, 101))

        wb.save('temp_file/考试成绩单2.xlsx')
        print('文件写入成功')
    @staticmethod
    def demo3():
        print('----------------写Excel文件|整单元格样式-------------------')
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = '期末成绩'
        titles = ('姓名', '语文', '数学', '英语')
        for col_index, title in enumerate(titles):
            sheet.cell(1, col_index + 1, title)

        names = ('关羽', '张飞', '赵云', '马超', '黄忠')
        for row_index, name in enumerate(names):
            sheet.cell(row_index + 2, 1, name)
            for col_index in range(2, 5):
                sheet.cell(row_index + 2, col_index, random.randrange(50, 101))

        wb.save('temp_file/考试成绩单2.xlsx')
        print('文件写入成功')
    @staticmethod
    def demo4():
        print('----------------公式计算-------------------')


    @staticmethod
    def demo5():
        print('----------------demo-------------------')

    @staticmethod
    def demo6():
        print('----------------demo-------------------')


if __name__ == '__main__':
    # Demo001.demo1()
    # Demo001.demo2()
    Demo001.demo3()
