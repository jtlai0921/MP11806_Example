'''
ParameterTree的主函數，顯示基金產品的文字/數值資訊
'''

import copy
import pickle
from pyqtgraph.parametertree import Parameter


# 建立參數樹的資料
params = [
    {'name': '基本收益資訊', 'type': 'group', 'children': [
        {'name': '今年收益', 'type': 'float', 'value': -2.45, 'siPrefix': True, 'suffix': '%'},
        {'name': '累計收益', 'type': 'float', 'value': -2.72, 'step': 0.1, 'siPrefix': True, 'suffix': '%'},
        {'name': '最近淨值日期', 'type': 'str', 'value': "2017-02-03"},
        {'name': '最新淨值', 'type': 'float', 'value': 0.9728, 'step': 0.01},
        {'name': '累計淨值', 'type': 'float', 'value': 0.9728, 'step': 0.01},
    ]},
    {'name': '基本產品資訊', 'type': 'group', 'children': [
        {'name': '開放日', 'type': 'str', 'value': '6個月'},
        {'name': '累計收益', 'type': 'str', 'value': '封閉期後，每個自然季度的最後一個月的20日至22日'},
        {'name': '認購起點', 'type': 'float', 'value': 100.00, 'step': 10, 'siPrefix': True, 'suffix': '萬(台幣)'},
        {'name': '追加起點', 'type': 'float', 'value': 10.00, 'step': 1, 'siPrefix': True, 'suffix': '萬(台幣)'},
        {'name': '認購費率', 'type': 'float', 'value': 1.00, 'step': 0.1, 'siPrefix': True, 'suffix': '%'},
        {'name': '贖回費率', 'type': 'float', 'value': 0, 'step': 0.1},
        {'name': '預警線', 'type': 'float', 'value': 85, 'step': 1, 'siPrefix': True, 'suffix': '%'},
        {'name': '停損線', 'type': 'float', 'value': 80, 'step': 1, 'siPrefix': True, 'suffix': '%'},
    ]},

    {'name': '投顧資訊', 'type': 'group', 'children': [
        {'name': '投資顧問', 'type': 'str', 'value': '和聚投資'},
        {'name': '業績報酬', 'type': 'float', 'value': 20, 'step': 1, 'siPrefix': True, 'suffix': '%'},
        {'name': '基金管理人', 'type': 'str', 'value': '千石資本'},
        {'name': '管理人管理費', 'type': 'str', 'value': '0'},
        {'name': '基金託管人', 'type': 'str', 'value': '光大銀行'},
        {'name': '證券經紀商', 'type': 'str', 'value': '未設'},
        {'name': '期貨經紀商', 'type': 'str', 'value': '未設'},
    ]},
    {'name': '其他資訊', 'type': 'group', 'children': [
        {'name': '成立日期', 'type': 'str', 'value': '2015-08-04'},
        {'name': '是否分級', 'type': 'str', 'value': '否'},
        {'name': '產品類型', 'type': 'str', 'value': '公募專屬'},
        {'name': '投資策略', 'type': 'str', 'value': '股票策略'},
        {'name': '子策略', 'type': 'str', 'value': '股票多頭'},

    ]},
]


## 建立參數樹物件
p = Parameter.create(name='params', type='group', children=params)


## 若樹裡面的任何內容發生變化，則輸出這些變化
def change(param, changes):
    print("tree changes:")
    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        print('  parameter: %s' % childName)
        print('  change:    %s' % change)
        print('  data:      %s' % str(data))
        print('  ----------')


p.sigTreeStateChanged.connect(change)


def valueChanging(param, value):
    print("Value changing (not finalized):", param, value)


# Too lazy for recursion:
for child in p.children():
    child.sigValueChanging.connect(valueChanging)
    for ch2 in child.children():
        ch2.sigValueChanging.connect(valueChanging)


