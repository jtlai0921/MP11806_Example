# -*- coding: utf-8 -*-

'''
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_run import Ui_MainWindow

from craw import get_one_page_data
import requests
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
import datetime
import os
import re

import threading
import copy


class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Class documentation goes here.
    '''
    signal_status = pyqtSignal(str, list)  # 自訂的訊號，用來顯示狀態列。

    def __init__(self, parent=None):
        '''
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        '''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.total_pages_content = 1
        self.total_pages_title = 1
        self.current_page_num_title = 1
        self.current_page_num_content = 1
        self.sort_type = 'desc'
        self.sort_name = 'nothing'
        self.comboBox_dict = {'相關度': 'nothing', '時間': 'pubdate', '代碼': 'stockcode_cat', '昇冪': 'asc', '降冪': 'desc'}
        self.frame_advanced.hide() # 預設隱藏 frame
        self.download_info_list = []  # 儲存要下載的資訊，每個元素是字典形式，包括下載的標題，url等資訊。
        self.download_path = os.path.abspath(r'./下載')
        self.label_show_path.setText('目前儲存目錄為：' + self.download_path)
        self.tableWidget_title_checked = Qt.Unchecked  # 設定tableWidget的預設選擇方式。
        self.tableWidget_content_checked = Qt.Unchecked
        self.select_title_page_info = set()  # 記錄checkBox_select選擇的頁面資訊。
        self.select_content_page_info = set()# 記錄checkBox_select選擇的頁面資訊。
        self.filter_title_list = [] # 顯示過濾title的list
        self.filter_content_list = [] # 顯示過濾content的list


        '''下面四行程式碼一定要按照順序執行，否則self.start_time與self.end_time這兩行會無效'''
        self.dateEdit.setDateTime(datetime.datetime.now())
        self.dateEdit_2.setDateTime(datetime.datetime.now())
        self.start_time = ''
        self.end_time = ''

        self.dateEdit.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        self.comboBox_type.setEnabled(False)
        self.comboBox_name.setEnabled(False)
        self.lineEdit_filter_content.setEnabled(False)
        self.lineEdit_filter_title.setEnabled(False)

        '''連接訊號與槽'''
        # 顯示 or 隱藏進階選項
        self.pushButton_setting_advanced.toggled['bool'].connect(self.frame_advanced.setHidden)
        # 下載
        self.pushButton_download_select_title.clicked.connect(self.download_pdf)
        self.pushButton_download_select_content.clicked.connect(self.download_pdf)
        download_thread.signal.connect(self.show_status)  # 子執行緒的訊號連結主執行緒的槽
        # 修改儲存路徑
        self.pushButton_change_save_path.clicked.connect(self.change_save_path)
        # tableWidget相關
        self.tableWidget_title.itemChanged.connect(self.select_item)
        self.tableWidget_content.itemChanged.connect(self.select_item)
        self.tableWidget_title.cellClicked.connect(self.view_one_new)
        self.tableWidget_content.cellClicked.connect(self.view_one_new)
        # 顯示狀態列
        self.signal_status.connect(self.show_status)  # 狀態列訊號連結至槽
        # 在lineEdit控制項按下Enter鍵，就可以觸發搜索或跳轉到頁碼
        self.lineEdit.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_filter_title.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_filter_content.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_content_page.returnPressed.connect(self.pushButton_content_jump_to.click)
        self.lineEdit_title_page.returnPressed.connect(lambda: self.page_go('title_jump_to'))
        # 頁碼跳轉函數
        self.pushButton_title_down.clicked.connect(lambda: self.page_go('title_down'))
        self.pushButton_content_down.clicked.connect(lambda: self.page_go('content_down'))
        self.pushButton_title_up.clicked.connect(lambda: self.page_go('title_up'))
        self.pushButton_content_up.clicked.connect(lambda: self.page_go('content_up'))
        self.pushButton_title_jump_to.clicked.connect(lambda: self.page_go('title_jump_to'))
        self.pushButton_content_jump_to.clicked.connect(lambda: self.page_go('content_jump_to'))
        # 選擇標題 or 內容
        self.checkBox_select_title.clicked['bool'].connect(self.select_checkBox)
        self.checkBox_select_content.clicked['bool'].connect(self.select_checkBox)
        # 顯示/下載過濾操作
        self.checkBox_filter_title.clicked['bool'].connect(self.filter_enable)
        self.checkBox_filter_content.clicked['bool'].connect(self.filter_enable)

        # 初始化下載目錄
        if not os.path.isdir(self.download_path):
            os.mkdir(self.download_path)

    def filter_df(self, df, filter_title_list=[],filter_content_list=[]):
        '''
        過濾df的主函數。
        :param df: df.columns
                Out[10]: 
                Index(['content', 'download_url', 'time', 'title'], dtype='object')

        :param filter_title_list: filter_title_list=['成都','年度'|'季度']
        filter_content_list: filter_content_list=['成都','年度'|'季度']
        :return: df_filter
        '''
        for each in filter_title_list:
            ser = df.title
            df = df[ser.str.contains(each)]
        filter_content_list = [each + '|None' for each in filter_content_list] # 處理內容返回為None的情況，代表若沒有文章內容返回，則不進行過濾
        for each in filter_content_list:
            ser = df.content
            df = df[ser.str.contains(each)]
        return df

    def get_filter_list(self,filter_text):
        filter_text = re.sub(r'[\s()（）]','',filter_text) #剔除空格，(,),（,）,分行符號等元素。
        filter_list = filter_text.split('&')
        return filter_list

    def filter_enable(self, bool):
        sender = self.sender()
        if sender.objectName() == 'checkBox_filter_title':
            if bool == True:
                self.lineEdit_filter_title.setEnabled(True)
            else:
                self.lineEdit_filter_title.setEnabled(False)
        elif sender.objectName() == 'checkBox_filter_content':
            if bool == True:
                self.lineEdit_filter_content.setEnabled(True)
            else:
                self.lineEdit_filter_content.setEnabled(False)


    def select_tableWidget(self, tableWidget):
        '''選擇tableWidget的函數'''
        row_count = tableWidget.rowCount()
        for index in range(row_count):
            item = tableWidget.item(index, 0)
            if item.checkState() == Qt.Unchecked:
                item.setCheckState(Qt.Checked)

    def select_tableWidget_clear(self, tableWidget):
        '''清除選擇tableWidget的函數'''
        row_count = tableWidget.rowCount()
        for index in range(row_count):
            item = tableWidget.item(index, 0)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)

    def select_checkBox_one(self, sender, tableWidget):
        if sender.checkState() == Qt.Checked:
            self.select_tableWidget(tableWidget)
            if tableWidget.objectName() == 'tableWidget_title':
                self.select_title_page_info.add(self.current_page_num_title)
            elif tableWidget.objectName() == 'tableWidget_content':
                self.select_content_page_info.add(self.current_page_num_content)
        else:
            self.select_tableWidget_clear(tableWidget)
            if tableWidget.objectName() == 'tableWidget_title':
                if self.current_page_num_title in self.select_title_page_info:
                    self.select_title_page_info.remove(self.current_page_num_title)
            elif tableWidget.objectName() == 'tableWidget_content':
                if self.current_page_num_content in self.select_content_page_info:
                    self.select_content_page_info.remove(self.current_page_num_content)

    def select_checkBox(self, bool):
        sender = self.sender() # sender()返回觸發這個訊號的哪個控制項
        if sender.objectName() == 'checkBox_select_title':
            self.select_checkBox_one(sender, self.tableWidget_title)
        elif sender.objectName() == 'checkBox_select_content':
            self.select_checkBox_one(sender, self.tableWidget_content)


    def page_go(self, go_type):
        '''頁面跳轉主函數'''
        if go_type == 'title_down': # 觸發下一頁按鈕
            _temp = self.current_page_num_title
            self.current_page_num_title += 1
            if 1 <= self.current_page_num_title <= self.total_pages_title: # 如果待跳轉的頁面真實有效，則繼續。否則不進行跳轉
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'title_up':
            _temp = self.current_page_num_title
            self.current_page_num_title -= 1
            # print(self.current_page_num_title)
            if 1 <= self.current_page_num_title <= self.total_pages_title:
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'content_up':
            _temp = self.current_page_num_content
            self.current_page_num_content -= 1
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp
        elif go_type == 'content_down':
            _temp = self.current_page_num_content
            self.current_page_num_content += 1
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp
        elif go_type == 'title_jump_to':
            _temp = self.current_page_num_title
            self.current_page_num_title = int(self.lineEdit_title_page.text())
            if 1 <= self.current_page_num_title <= self.total_pages_title:
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'content_jump_to':
            _temp = self.current_page_num_content
            self.current_page_num_content = int(self.lineEdit_content_page.text())
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp


    # def select(self, select_type):
    #     '''
    #     :param select_type:is a string: title,content, two
    #     :return:
    #     '''
    #     if select_type == 'title':
    #         self.select_tableWidget(self.tableWidget_title)
    #     elif select_type == 'content':
    #         self.select_tableWidget(self.tableWidget_content)



    # def select_clear(self):
    #     '''清除選擇的槽函數'''
    #     self.select_tableWidget_clear(self.tableWidget_content)
    #     self.select_tableWidget_clear(self.tableWidget_title)


    def download_pdf(self):
        '''下載pdf的主函數'''
        if download_thread.isRunning() == True:
            QMessageBox.warning(self, '警告!', '檢查到有下載程式正在執行，請不要重複執行！', QMessageBox.Yes)
            return None

        download_thread.download_list = self.download_info_list.copy()
        download_thread.download_path = copy.copy(self.download_path)
        download_thread.start()

    def view_one_new(self, row, column):
        '''查看新聞的主函數'''
        sender = self.sender()
        if column == 2:  # 只針對第三行--->查看
            if sender.objectName() == 'tableWidget_title':
                download_one = self.list_target_title[row]
            else:
                download_one = self.list_target_content[row]
            download_path = copy.copy(self.download_path)
            view_thread = threading.Thread(target=self.view_one_new_thread, args=(download_path, download_one),
                                           daemon=True)
            view_thread.start()

    def view_one_new_thread(self, download_path, download_one):
        '''查看功能的多執行緒程式'''
        download_url = download_one['download_url']
        title = download_one['title']
        title = title.replace(':', '：')
        title = title.replace('?', '？')
        title = title.replace('*', '★')

        path = download_path + os.sep + '%s.pdf' % title
        if not os.path.isfile(path):
            try:
                r = requests.get(download_url, stream=True)
                data = r.raw.read()
            except:
                return
            f = open(path, "wb")
            f.write(data)
            f.close()
        os.system(path)


    def show_status(self, type, list_args):
        if type == 'download_status':
            count_num, count_all, count_right, count_err, title = list_args
            self.statusBar().showMessage(
                '完成:{0}/{3}，正確:{1}，錯誤：{2}，本次下載：{4}'.format(count_num, count_right, count_err, count_all, title))
        if type == 'download_status_err':
            count_num, count_all, count_right, count_err, title = list_args
            self.statusBar().showMessage(
                '重新下載失敗：完成:{0}/{3}，正確:{1}，錯誤：{2}，本次下載：{4}'.format(count_num, count_right, count_err, count_all, title))
        if type == 'select_status':
            self.statusBar().showMessage('已選擇：%d' % len(self.download_info_list))
        if type == 'change_save_path_status':
            self.statusBar().showMessage('儲存目錄修改為：%s' % self.download_path)
        if type == 'clear':
            self.statusBar().showMessage(' ')

    def change_save_path(self):
        '''修改儲存目錄
        '''

        if not os.path.isdir(self.download_path):
            os.mkdir(self.download_path)
        directory1 = QFileDialog.getExistingDirectory(self,
						"選取資料夾",
						self.download_path)  # 起始路徑
        self.download_path = QDir.toNativeSeparators(directory1)  # 路徑是windows支援的顯示方式
        self.label_show_path.setText('目前儲存目錄為： ' + self.download_path)
        self.signal_status.emit('change_save_path_status', [])

    def show_tablewidget(self, dict_data, tableWidget, clear_fore=True):
        '''傳入dict_data 與 tableWidget，以便在tablewidget上面呈現dict_data'''
        '''擷取自己需要的資訊：'''
        if clear_fore == True:  # 檢查搜索之前是否要清空下載購物車內容
            self.download_info_list = []

        # 更新狀態列資訊
        self.signal_status.emit('clear', []) # 清空狀態列

        # 檢查checkBox之前是否已經被選中，若是則設定為選中，否則為不選中
        if tableWidget.objectName() == 'tableWidget_title':
            if self.current_page_num_title in self.select_title_page_info:
                self.checkBox_select_title.setCheckState(Qt.Checked)
            else:
                self.checkBox_select_title.setCheckState(Qt.Unchecked)
            flag = 'title'
        else:
            if self.current_page_num_content in self.select_content_page_info:
                self.checkBox_select_content.setCheckState(Qt.Checked)
            else:
                self.checkBox_select_content.setCheckState(Qt.Unchecked)
            flag = 'content'

        '''檢測過濾顯示的資訊'''
        if self.lineEdit_filter_title.isEnabled() == True:
            filter_text = self.lineEdit_filter_title.text()
            self.filter_title_list = self.get_filter_list(filter_text)
        else:
            self.filter_title_list=[]
        if self.lineEdit_filter_content.isEnabled() == True:
            filter_text = self.lineEdit_filter_content.text()
            self.filter_content_list = self.get_filter_list(filter_text)
        else:
            self.filter_content_list=[]

        '''從網路爬蟲抓取的資料中提取所需的資料'''
        if len(dict_data) > 0:
            # key_word = self.lineEdit.text()
            len_index = len(dict_data)
            list_target = []  # 從dict_data提取目標資料，基本元素是下面的dict_target
            for index in range(len_index):
                dict_temp = dict_data[index] # 提取從伺服器返回的其中一列
                dict_target = {} # 從dict_temp提取所需的資訊，主要包括title,content,time,download_url等等
                # 提取標題與內容
                _temp_title = dict_temp['announcementTitle']
                _temp_content = dict_temp['announcementContent']
                for i in ['<em>', '</em>']: # <em>, </em>是伺服器對搜索關鍵字加入的標記，這裡予以剔除
                    _temp_title = _temp_title.replace(i, '')
                    _temp_content = str(_temp_content).replace(i, '')

                dict_target['title'] = _temp_title
                dict_target['content'] = _temp_content

                # 提取時間
                _temp = dict_temp['adjunctUrl']
                dict_target['time'] = _temp.split(r'/')[1]

                # 提取url
                id = _temp.split(r'/')[2].split('.')[0]
                download_url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/download/{}?announceTime={}'.format(
                    id, dict_target['time'])
                dict_target['download_url'] = download_url
                dict_target['flag'] = flag
                # print(download_url)
                # 加入處理的結果
                list_target.append(dict_target)

            '''根據過濾規則自訂過濾條件，預設是不過濾'''
            df = DataFrame(list_target)
            df = self.filter_df(df,filter_title_list=self.filter_title_list,filter_content_list = self.filter_content_list)

            '''過濾後，更新list_target'''
            _temp = df.to_dict('index')
            list_target = list(_temp.values())

        else:  # 處理沒有資料的情況
            list_target = []

        '''tableWidget的初始化'''
        list_col = ['time', 'title', 'download_url']
        len_col = len(list_col)
        len_index = len(list_target)  # list_target可能有變化，需要重新計算長度
        if tableWidget.objectName() == 'tableWidget_title':
            self.list_target_title = list_target
        else:
            self.list_target_content = list_target
        tableWidget.setRowCount(len_index) # 設定列數
        tableWidget.setColumnCount(len_col) # 設定行數
        tableWidget.setHorizontalHeaderLabels(['時間', '標題', '查看']) # 設定垂直方向的名字
        tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len_index + 1)]) # 設定水平方向的名字
        tableWidget.setCornerButtonEnabled(True) # 左上角一點擊就全選

        '''填充tableWidget的資料'''
        for index in range(len_index):
            for col in range(len_col):
                name_col = list_col[col]
                if name_col == 'download_url':
                    item = QTableWidgetItem('查看')
                    item.setTextAlignment(Qt.AlignCenter)
                    font = QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    item.setBackground(QColor(218, 218, 218))
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    tableWidget.setItem(index, col, item)
                elif name_col == 'time':
                    item = QTableWidgetItem(list_target[index][name_col])
                    item.setFlags(Qt.ItemIsUserCheckable |
                                  Qt.ItemIsEnabled)
                    '''查看目前列代表的內容是否已經在購物車裡面，如過是就設為選中'''
                    if list_target[index] in self.download_info_list:
                        item.setCheckState(Qt.Checked)
                    else:
                        item.setCheckState(Qt.Unchecked)
                    tableWidget.setItem(index, col, item)
                else:
                    tableWidget.setItem(index, col, QTableWidgetItem(list_target[index][name_col]))
        # tableWidget.resizeColumnsToContents()
        tableWidget.setColumnWidth(1, 500)

    def select_item(self, item):
        '''處理選擇item的主函數'''
        # print('item+change')
        column = item.column()
        row = item.row()
        if column == 0:  # 只針對第一行
            if item.checkState() == Qt.Checked:
                if item.tableWidget().objectName() == 'tableWidget_title':
                    download_one = self.list_target_title[row]
                else:
                    download_one = self.list_target_content[row]
                if download_one not in self.download_info_list:
                    self.download_info_list.append(download_one)
                    self.signal_status.emit('select_status', [])
            else:
                if item.tableWidget().objectName() == 'tableWidget_title':
                    download_one = self.list_target_title[row]
                else:
                    download_one = self.list_target_content[row]
                if download_one in self.download_info_list:
                    self.download_info_list.remove(download_one)
                    self.signal_status.emit('select_status', [])

    def update_tablewidget_title(self, page_num=1):
        '''更新tablewidget_title'''
        key_word = self.lineEdit.text()
        '''從網路爬蟲取得資料'''
        total_pages_title, dict_data_title = get_one_page_data(key_word, fulltext_str_flag='false', page_num=page_num,
                                                               date_start=self.start_time, date_end=self.end_time,
                                                               sortName=self.sort_name, sortType=self.sort_type)
        '''把資料顯示到表格上'''
        if total_pages_title != None:
            self.total_pages_title = total_pages_title
            self.show_tablewidget(dict_data_title, self.tableWidget_title, clear_fore=False)
            self.label_page_info_title.setText('%d/%d' % (self.current_page_num_title, self.total_pages_title)) # 更新目前頁碼資訊

    def update_tablewidget_content(self, page_num=1):
        '''更新tablewidget_content'''
        key_word = self.lineEdit.text()
        total_pages_content, dict_data_content = get_one_page_data(key_word, fulltext_str_flag='true',
                                                                   page_num=page_num, date_start=self.start_time,
                                                                   date_end=self.end_time, sortName=self.sort_name,
                                                                   sortType=self.sort_type)
        if total_pages_content != None:
            self.total_pages_content = total_pages_content
            self.show_tablewidget(dict_data_content, self.tableWidget_content, clear_fore=False)
            self.label_page_info_content.setText('%d/%d' % (self.current_page_num_content, self.total_pages_content))

    def get_dateEdit_time(self, dateEdit):
        dateEdit_day = dateEdit.text().replace('/', '-')
        datetime_day = datetime.datetime.strptime(dateEdit_day, '%Y-%m-%d')
        return datetime_day.strftime('%Y-%m-%d')

    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        '''
        Slot documentation goes here.
        '''
        self.download_info_list = [] # 每一次重新搜索都要清空下載購物車
        self.current_page_num_title = 1 # 初始化搜索，預設目前頁碼為1
        self.current_page_num_content = 1
        self.update_tablewidget_title() # 更新標題搜索
        self.update_tablewidget_content() # 更新內容搜索

    @pyqtSlot(bool)
    def on_checkBox_unlimite_time_flag_clicked(self, checked):
        '''
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        '''

        if checked == True:
            self.dateEdit.setEnabled(False)
            self.dateEdit_2.setEnabled(False)
            self.end_time = ''
            self.start_time = ''
        else:
            self.dateEdit.setEnabled(True)
            self.dateEdit_2.setEnabled(True)
            self.start_time = self.get_dateEdit_time(self.dateEdit)
            self.end_time = self.get_dateEdit_time(self.dateEdit_2)
            # print(self.start_time,self.end_time)

    @pyqtSlot(QDate)
    def on_dateEdit_dateChanged(self, date):
        self.start_time = self.get_dateEdit_time(self.dateEdit)

    @pyqtSlot(QDate)
    def on_dateEdit_2_dateChanged(self, date):
        self.end_time = self.get_dateEdit_time(self.dateEdit_2)

    @pyqtSlot(bool)
    def on_checkBox_sort_flag_clicked(self, checked):
        if checked == True: # 恢復預設的排序
            self.comboBox_name.setEnabled(False)
            self.comboBox_type.setEnabled(False)
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        elif self.comboBox_name.currentText() == '相關度': # 對於相關度，有些特殊
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(False) # 上面comboBox_name.currentText()=="相關度"，則這個控制項不可用。這是模擬官網的操作。
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        else:# 對於其他，則設定對應參數
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(True)
            sort_name = self.comboBox_name.currentText()
            sort_type = self.comboBox_type.currentText()

            self.sort_name = self.comboBox_dict[sort_name]
            self.sort_type = self.comboBox_dict[sort_type]

    @pyqtSlot(str)
    def on_comboBox_name_currentTextChanged(self, p0):
        if p0 == '相關度':
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(False)
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        else:
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(True)
            sort_name = self.comboBox_name.currentText()
            self.sort_name = self.comboBox_dict[sort_name]

    @pyqtSlot(str)
    def on_comboBox_type_currentTextChanged(self, p0):
        sort_type = self.comboBox_type.currentText()
        self.sort_type = self.comboBox_dict[sort_type]


class WorkThread(QThread):
    #宣告一個包括str和list類型參數的訊號
    signal = pyqtSignal(str, list)

    def __int__(self):
        self.download_list = self.download_path = []
        self.download_list_err = []
        self.filter_content_list = self.filter_title_list = []
        super(WorkThread, self).__init__()

    def main_download(self, download_list, download_path, download_status='download_status'):
        count_all = len(download_list)
        count_err = count_right = count_num = 0
        self.download_list_err = []
        for key_dict in download_list:
            count_num += 1
            download_url = key_dict['download_url']
            time = key_dict['time']
            title = key_dict['title']
            total_title = time + '_' + title
            total_title = total_title.replace(':', '：')
            total_title = total_title.replace('?', '？')
            total_title = total_title.replace('*', '★')

            file_path = download_path + os.sep + '%s.pdf' % total_title
            if os.path.isfile(file_path) == True: # 若檔案已存在，則預設為下載成功。
                count_right += 1
                signal_list = [count_num, count_all, count_right, count_err, title]
                self.signal.emit(download_status, signal_list)  # 迴圈完畢後發出訊號
                continue
            else:
                f = open(file_path, "wb")  # 先建立一個檔案，以免其他執行緒重複建立
                try:
                    r = requests.get(download_url, stream=True)
                    data = r.raw.read()
                except:
                    self.download_list_err.append(key_dict)
                    count_err += 1
                    f.close()
                    os.remove(file_path)  # 檔案下載失敗，要先關閉open函數，然後刪除該檔
                    signal_list = [count_num, count_all, count_right, count_err, title]
                    self.signal.emit(download_status, signal_list)  # 迴圈完畢後發出訊號
                    continue
                f.write(data)
                f.close()
                count_right += 1
                signal_list = [count_num, count_all, count_right, count_err, title]
                self.signal.emit(download_status, signal_list)  # 迴圈完畢後發出訊號

    def run(self):
        self.main_download(self.download_list, self.download_path, download_status='download_status')
        self.main_download(self.download_list_err, self.download_path, download_status='download_status_err')
        self.main_download(self.download_list_err, self.download_path, download_status='download_status_err')


if __name__ == "__main__":
    import sys

    download_thread = WorkThread()
    app = QApplication(sys.argv)
    ui = MainWindow()
    # ui.showMaximized()
    ui.show()

    sys.exit(app.exec_())
