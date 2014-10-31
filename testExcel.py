#coding=utf-8
'''
Created on 2014-10-30

@author: ZJ
'''
import xlwt
from xlrd import open_workbook  

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
# indexing is zero based, row then column
sheet.write(0,1,'a') #第一行第一列
sheet.write(0,2,'a1') #第一行第一列
sheet.write(1,1,'b') #第二行第二列
sheet.write(1,2,'b1') #第一行第一列
wbk.save('E:/test.xls')  

  
wb = open_workbook('E:/test.xls')  
for s in wb.sheets():  
    print 'Sheet:',s.name  
    for row in range(s.nrows):  
        values = []  
        for col in range(s.ncols):  
            values.append(s.cell(row,col).value)  
        print ','.join(values)  
        print values[1]
    print  
    
      #for row in range(rowNum):  #sheet.nrows
      #          values = []  
       #         for col in range(3):  
      #              values.append(sheet.cell(row,col).value)  #sheet.cell(row,col).value
       #             if name==values[1]:
      #                  continue