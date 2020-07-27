import csv
import datetimetest as d
from datetime import datetime

class Member:
    def __init__(self):
        #意味なし
        self.filename = 'first_edit.csv'

    def readFile(self,filename):
        file = open(filename,'r')
        reader = csv.DictReader(file)
        readerlist = list(reader)
        return readerlist

    def getNewestDate(self,itemDate1,itemDate2,itemDate3,itemDate4,itemDate5):
        itemDate = ''
        if itemDate1:
            itemDate = itemDate1
        if itemDate2:
            itemDate = itemDate2
        if itemDate3:
            itemDate = itemDate3
        if itemDate4:
            itemDate = itemDate4
        if itemDate5:
            itemDate = itemDate5
        return itemDate

    def editFile(self,filename):
        readerlist2 = []
        for row in self.readFile(filename):

            if row['会員状態'] in ('仮会員','未入会','退会員', '転出','除名','移籍'):
                continue

            if row['退会日']:
                if d.getOnlyDate(row['退会日']) <= d.LAST_DAY_THIS_MONTH:
                    continue
            if row['転出日']:
                if d.getOnlyDate(row['転出日']) <= d.LAST_DAY_THIS_MONTH:
                    continue
            if row['移籍日']:
                if d.getOnlyDate(row['移籍日']) <= d.LAST_DAY_THIS_MONTH:
                    continue
            if row['除名日']:
                if d.getOnlyDate(row['除名日']) <= d.LAST_DAY_THIS_MONTH:
                    continue

            if row['会員状態'] == '休会員':
                freezeEndDate = self.getNewestDate(row['休会期間1_終了日'],\
                                                    row['休会期間2_終了日'],\
                                                    row['休会期間3_終了日'],\
                                                    row['休会期間4_終了日'],\
                                                    row['休会期間5_終了日'])
                if d.getOnlyDate(freezeEndDate) != d.LAST_DAY_THIS_MONTH:
                    continue

            freezeStartDate = self.getNewestDate(row['休会期間1_開始日'],\
                                                    row['休会期間2_開始日'],\
                                                    row['休会期間3_開始日'],\
                                                    row['休会期間4_開始日'],\
                                                    row['休会期間5_開始日'])
            if freezeStartDate:
                if d.getOnlyDate(freezeStartDate) == d.FIRST_DAY_NEXT_MONTH:
                    continue

            if not row['口座振替_初回振替日']:
                continue
            if d.getOnlyDate(row['口座振替_初回振替日']) >= d.FIRST_DAY_NEXT_MONTH:
                continue       

            if row['会員状態'] == '本会員(転入)':
                if not row['口座振替_初回振替日']:
                    continue 

            if row['口座振替_振替用紙'] == '口座振替依頼書_未回収':
                continue
            if row['口座振替_振替用紙'] == 'モバイル決済_未完了':
                continue
                
            readerlist2.append(row)
        return readerlist2



