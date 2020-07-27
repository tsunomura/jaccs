import os
import csv

class CsvFile:

    def __init__(self):
        #self.path = os.path.join('/mnt','c','Users','kazuo','Dropbox (ethos)','ethos経営管理','99.個人フォルダ','角村（ドラフト）')
        self.path = os.path.join('/mnt','c','Users','kazuo','Downloads')

    def my_list(self):
        print(self.path)
        for i in os.listdir(self.path):
            print(i)

    def get_sg_csv(self):
        result = [i for i in os.listdir(self.path) if i.startswith('customer_')]
        full_path = self.path + '/' + result[-1]
        return full_path

    def get_reader(self):
        full_path = self.get_sg_csv()
        return csv.reader(open(full_path,'r',encoding='cp932'))

    def count_original_rows(self):
        reader = self.get_reader()
        num_lines = sum(1 for line in reader)
        print('lines: ' + str(num_lines))

    def get_col(self,col_name):
        header = next(self.get_reader())
        return header.index(col_name)

    def delete_non_member(self):
        out = open('sg_csv_edited.csv','w',newline='')
        writer = csv.writer(out)
        for row in self.get_reader():
            if row[self.get_col('会員番号')] == '=""':
                continue
            elif row[self.get_col('お名前(姓)')] == '日本橋浜町店':
                continue
            else:
                writer.writerow(row)

    def count_rows(self,filename):
        with open(filename,'r') as f:
        #with open(filename,'r') as f:
            reader = csv.reader(f)
            num_lines = sum(1 for line in reader)
            print('lines: ' + str(num_lines))

    def get_dictreader(self):
        full_path = self.get_sg_csv()
        with open(full_path,'r',encoding='cp932') as f:
            dreader = csv.DictReader(f)
            for row in dreader:
                if row['口座振替_金額'] and int(row['口座振替_金額'])>0:
                    print(row['会員番号'],row['口座振替_契約者番号'],row['口座振替_振替用紙'],row['プラン'],row['口座振替_金額'])
   
c = CsvFile()
"""
c.count_original_rows()
c.delete_non_member()
c.count_rows('sg_csv_edited.csv')
"""
c.get_dictreader()
    


