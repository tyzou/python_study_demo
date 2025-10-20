import json
import requests
import ujson


class Demo22:

    @staticmethod
    def demo1():
        print('----------------对象的序列化和反序列化-------------------')
        my_dict = {
            'name': '骆昊',
            'age': 40,
            'friends': ['王大锤', '白元芳'],
            'cars': [
                {'brand': 'BMW', 'max_speed': 240},
                {'brand': 'Audi', 'max_speed': 280},
                {'brand': 'Benz', 'max_speed': 280}
            ]
        }
        #  将字典处理成JSON格式,使用`json`模块的`dumps`函数,用Unicode编码显示的
        print(json.dumps(my_dict))
        # 写入
        with open('temp_file/data.json', 'w') as file:
            json.dump(my_dict, file)

        # 读取
        with open('temp_file/data.json', 'r') as file:
            my_dict = json.load(file)
            print(type(my_dict))
            print(my_dict)

    @staticmethod
    def demo2():
        print('----------------包管理工具pip-------------------')
        # 安装ujson第三方库：pip install ujson
        # 搜索ujson第三方库： pip search ujson
        # 查看已安装三方库：pip list
        # 更新`ujson`三方库：pip install -U ujson
        # 删除ujson三方库：pip uninstall -y ujson
        my_dict = {
            'name': '骆昊',
            'age': 40,
            'friends': ['王大锤', '白元芳'],
            'cars': [
                {'brand': 'BMW', 'max_speed': 240},
                {'brand': 'Audi', 'max_speed': 280},
                {'brand': 'Benz', 'max_speed': 280}
            ]
        }
        #  将字典处理成JSON格式,使用`json`模块的`dumps`函数,用Unicode编码显示的
        print(ujson.dumps(my_dict))
        # 写入
        with open('temp_file/data2.json', 'w') as file:
            ujson.dump(my_dict, file)

        # 读取
        with open('temp_file/data2.json', 'r') as file:
            my_dict = ujson.load(file)
            print(type(my_dict))
            print(my_dict)


    @staticmethod
    def demo3():
        print('----------------使用网络API获取数据-------------------')
        resp = requests.get('https://api.codelife.cc/bing/list?lang=cn&page=1&size=16')
        if resp.status_code == 200:
            data_model = resp.json()
            for item in data_model['data']:
                print(item['_id'])
                print(item['fullSrc'])
                print(item['copyright'])



if __name__ == '__main__':
    Demo22.demo1()
    Demo22.demo2()
    Demo22.demo3()
    Demo22.demo4()
    Demo22.demo5()
    Demo22.demo6()
