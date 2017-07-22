# Python 字典类型转换为 JSON 对象
import json


class JsonSample:
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = '{"no": 1,"name": "Runoob","url": "http://www.runoob.com"}'

    def printStr(self):
        tempStr = json.dumps(self.data)
        print("Python 原始数据：", repr(self.data))
        print("JSON 对象：", tempStr)

    def printObject(self):
        # 将 JSON 对象转换为 Python 字典
        data2 = json.loads(self.json_str)
        print("data2['name']: ", data2['name'])
        print("data2['url']: ", data2['url'])

    def writeJsonInFile(self):
        # 写入 JSON 数据
        with open('./files/data.json', 'w') as f:
            json.dump(self.data, f)

    def readJsonFromFile(self):
        # 读取数据
        with open('./files/data.json', 'r') as f:
            print("read jsonFile: " + repr(json.load(f)))
