import xlrd
import xlwt
import random
from xlutils.copy import copy


class Demo001:

    @staticmethod
    def demo1():
        print('----------------读Excel文件（工作簿）-------------------')
        # 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
        wb = xlrd.open_workbook('temp_file/testnoformatting.xls')
        sheet_names = wb.sheet_names()
        print(sheet_names)
        # 通过指定的表单名称获取Sheet对象（工作表）
        sheet = wb.sheet_by_name(sheet_names[0])
        # 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
        print(sheet.nrows, sheet.ncols)

        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                value = sheet.cell(row, col).value
                print(value, end='\t')
            print()

        # 获取最后一个单元格的数据类型
        # 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
        last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>获取最后一个单元格的数据类型>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(last_cell_type)
        # 获取第一行的值（列表）
        print(sheet.row_values(0))
        # 获取指定行指定列范围的数据（列表）
        # 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
        print(sheet.row_slice(3, 0, 5))

    @staticmethod
    def demo2():
        print('----------------写Excel文件-------------------')
        student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
        print(scores)
        # 创建工作簿对象（Workbook）
        wb = xlwt.Workbook()
        # 创建工作表对象（Worksheet）
        sheet = wb.add_sheet('一年级二班')
        # 添加表头数据
        titles = ('姓名', '语文', '数学', '英语')

        for index, title in enumerate(titles):
            sheet.write(0, index, title)

        # 将学生姓名和考试成绩写入单元格
        for row in range(len(scores)):
            sheet.write(row + 1, 0, student_names[row])
            for col in range(len(scores[row])):
                sheet.write(row + 1, col + 1, scores[row][col])

        # 保存Excel工作簿
        wb.save('temp_file/考试成绩表.xls')
        print("文件写入成功，文件名：考试成绩表.xls")

    @staticmethod
    def demo3():
        print('----------------写Excel文件|整单元格样式-------------------')
        student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
        print(scores)
        # 创建工作簿对象（Workbook）
        wb = xlwt.Workbook()
        # 创建工作表对象（Worksheet）
        sheet = wb.add_sheet('一年级二班')
        # 添加表头数据
        titles = ('姓名', '语文', '数学', '英语')

        print('将表头单元格的背景色修改为黄色')
        header_style = xlwt.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
        pattern.pattern_fore_colour = 5
        header_style.pattern = pattern


        print('为表头设置指定的字体')
        font = xlwt.Font()
        # 字体名称
        font.name = '华文楷体'
        # 字体大小（20是基准单位，18表示18px）
        font.height = 20 * 18
        # 是否使用粗体
        font.bold = True
        # 是否使用斜体
        font.italic = False
        # 字体颜色
        font.colour_index = 4
        header_style.font = font

        print('表头垂直居中对齐')
        align = xlwt.Alignment()
        # 垂直方向的对齐方式
        align.vert = xlwt.Alignment.VERT_CENTER
        # 水平方向的对齐方式
        align.horz = xlwt.Alignment.HORZ_CENTER
        header_style.alignment = align

        print('给表头加上黄色的虚线边框')
        borders = xlwt.Borders()
        props = (
            ('top', 'top_colour'), ('right', 'right_colour'),
            ('bottom', 'bottom_colour'), ('left', 'left_colour')
        )

        # 通过循环对四个方向的边框样式及颜色进行设定
        for position, color in props:
            # 使用setattr内置函数动态给对象指定的属性赋值
            setattr(borders, position, xlwt.Borders.DASHED)
            setattr(borders, color, 5)
        header_style.borders = borders

        for index, title in enumerate(titles):
            # 设置列宽为200px
            sheet.col(index).width = 20 * 200
            sheet.write(0, index, title,header_style)

        # 将学生姓名和考试成绩写入单元格
        for row in range(len(scores)):
            sheet.write(row + 1, 0, student_names[row])
            for col in range(len(scores[row])):
                sheet.write(row + 1, col + 1, scores[row][col])

        # 保存Excel工作簿
        wb.save('temp_file/考试成绩表.xls')
        print("文件写入成功，文件名：考试成绩表.xls")

    @staticmethod
    def demo4():
        print('----------------公式计算-------------------')
        wb_for_read = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
        sheet1 = wb_for_read.sheet_by_index(0)
        nrows, ncols = sheet1.nrows, sheet1.ncols
        wb_for_write = copy(wb_for_read)
        sheet2 = wb_for_write.get_sheet(0)
        sheet2.write(nrows, 4, xlwt.Formula(f'average(E2:E{nrows})'))
        sheet2.write(nrows, 6, xlwt.Formula(f'sum(G2:G{nrows})'))
        wb_for_write.save('阿里巴巴2020年股票数据汇总.xls')


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
    Demo001.demo4()
    Demo001.demo5()
    Demo001.demo6()
