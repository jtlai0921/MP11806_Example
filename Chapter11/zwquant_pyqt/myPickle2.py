# -*- coding: utf-8 -*-

import pickle

'''
# write python dict to a file
# mydict = {'����`����': '13', '�����馬�q�v': '0.156', '�̪��^�M�ɶ�': '182', '�}�l�ɶ�': '2015-01-02'}
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

#my_list = ['ABC', '123', '����', ['123']] #�s�W�@�Ӵ��զC��
#my_list = {'����`����': '13', '�����馬�q�v': '0.156', '�̪��^�M�ɶ�': '182', '�}�l�ɶ�': '2015-01-02'}
my_list = [['����`����', '13'], ['����`�էQ', '-8834.15'], ['�̲׸겣����', '$13810.89'], ['�̲ײ{���겣����', '$1165.85'], ['�̲��Ҩ�겣����', '$12645.04'], ['�֭p�^���v', '38.11'], ['�����馬�q�v', '0.156'], ['�馬�q�v��t', '0.0244'], ['sharp��v', '0.695,�]0.05�Q�v�^'], ['�L���I�Q�v', '0.05'], ['sharp��v�]�L���I�^', '0.824'], ['�̤j�^�M�v', '0.1357'], ['�̪��^�M�ɶ�', '182'], ['�^�M�ɶ�(�̰��I��)', '2015-05-28'], ['�^�M�̰��I��', '15979.060'], ['�^�M�̧C�I��', '9937.720'], ['�ɶ��P��', '464 (Day)'], ['�ɶ��P���]�����^', '257 (Day)'], ['�}�l�ɶ�', '2015-01-01'], ['�����ɶ�', '2016-04-08'], ['�M�צW��', 'macd20'], ['�����W��', 'macd20'], ['�����Ѽ��ܼ� staVars[]', '12  26  2015-01-01  ']]

pickle_file = open('my_list.pkl', 'wb') #�ɮ�(my_list.pkl)�����H�G�i��i�g�Ҧ��}�ҡA�Y"wb"
pickle.dump(my_list, pickle_file) #�I�spickle.dump��k�A�Nmy_list�H�G�i��覡�g�Jpickle_file����
pickle_file.close() #�����ɮת���

import os; os.getcwd() #�ޤJos�]�A�˵���epython�ؿ� 'D:\\Python33'
os.listdir('C:\\Sources\\Python36') #�˵����w�ؿ��U���ɮסA�i�H�ݨ�w�g�ͦ��@�ӦW��my_list.pkl���G�i���ɮ� [... 'my_list.pkl', .....]

pickle_file2 = open('my_list.pkl', 'rb') #�ɮ�(my_list.pkl)�����H�G�i��iŪ�Ҧ��}�ҡA�Y"rb"
my_list2 = pickle.load(pickle_file2) #�I�sickle.load��k�A�N�H�G�i��榡�x�s�������٭�^��
pickle_file2.close()

print (my_list2)
