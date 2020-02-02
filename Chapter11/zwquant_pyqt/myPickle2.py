# -*- coding: utf-8 -*-

import pickle

'''
# write python dict to a file
# mydict = {'交易總次數': '13', '平均日收益率': '0.156', '最長回撤時間': '182', '開始時間': '2015-01-02'}
mydict = {'a': 1, 'b': 2, 'c': 3}
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

# read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()

print (mydict)
print (mydict2)
'''

#my_list = ['ABC', '123', '中文', ['123']] #新增一個測試列表
#my_list = {'交易總次數': '13', '平均日收益率': '0.156', '最長回撤時間': '182', '開始時間': '2015-01-02'}
my_list = [['交易總次數', '13'], ['交易總盈利', '-8834.15'], ['最終資產價值', '$13810.89'], ['最終現金資產價值', '$1165.85'], ['最終證券資產價值', '$12645.04'], ['累計回報率', '38.11'], ['平均日收益率', '0.156'], ['日收益率方差', '0.0244'], ['sharp比率', '0.695,（0.05利率）'], ['無風險利率', '0.05'], ['sharp比率（無風險）', '0.824'], ['最大回撤率', '0.1357'], ['最長回撤時間', '182'], ['回撤時間(最高點位)', '2015-05-28'], ['回撤最高點位', '15979.060'], ['回撤最低點位', '9937.720'], ['時間周期', '464 (Day)'], ['時間周期（交易日）', '257 (Day)'], ['開始時間', '2015-01-01'], ['結束時間', '2016-04-08'], ['專案名稱', 'macd20'], ['策略名稱', 'macd20'], ['策略參數變數 staVars[]', '12  26  2015-01-01  ']]

pickle_file = open('my_list.pkl', 'wb') #檔案(my_list.pkl)必須以二進制可寫模式開啟，即"wb"
pickle.dump(my_list, pickle_file) #呼叫pickle.dump方法，將my_list以二進制的方式寫入pickle_file物件
pickle_file.close() #關閉檔案物件

import os; os.getcwd() #引入os包，檢視當前python目錄 'D:\\Python33'
os.listdir('C:\\Sources\\Python36') #檢視指定目錄下的檔案，可以看到已經生成一個名為my_list.pkl的二進制檔案 [... 'my_list.pkl', .....]

pickle_file2 = open('my_list.pkl', 'rb') #檔案(my_list.pkl)必須以二進制可讀模式開啟，即"rb"
my_list2 = pickle.load(pickle_file2) #呼叫ickle.load方法，將以二進制格式儲存的物件還原回來
pickle_file2.close()

print (my_list2)
