#coding=utf-8
'''
Created on 2014-10-30

@author: ZJ
'''
#from xml.dom.minidom import parse
import xml.dom.minidom  #解析XML
import glob
import os
import xlwt #写
import xlrd #读
#读取文件夹里所有文件
#读取总文件夹里的小文件夹
root='E:/xiaojiezai1/demo'
dirs=glob.glob('%s\\*' %root)

for d in dirs:  #d是root里的文件
    #处理非文件夹文件
    #如果是文件则跳出，进行下一个循环
    if(os.path.isfile(d)):
        continue 
    print "=================================开始处理文件夹：%s=================================" % d
    if os.path.exists(d+'.xls'):
        dec=raw_input("额，该文件已经存在，选择是否将其覆盖：yes or no\n")
        if dec=="no":
            print "不会写入excel"
            continue
        
    excel=xlwt.Workbook()                    
    sheet=excel.add_sheet("sheet 1",cell_overwrite_ok=True)  
   
    files=glob.glob('%s\\*' %d)
    #第一行
    sheet.write(0,0,'name')
    sheet.write(0,1,'price')
    sheet.write(0,2,'score')
    s=[]        #定义一个空列表，记录name值    
    rowNum=1
    for f in files:
        #使用minidom解析器打开 XML 文档      
        DOMTree = xml.dom.minidom.parse(f)    
        #DOMTree = xml.dom.minidom.parse("E:/demo.xml")      
        shop = DOMTree.documentElement 
        #在集合中获取所有item
        items = shop.getElementsByTagName("item")
        #root.getElementsByTagName( "Table" )将获得所有<Table></Table>标签对，可以用列表方法获取。因为这里就一个<Table></Table>标签，所以直接[0]返回这个单独的对象。     
        #打印每个item的详细信息

        for item in items:
            
            print "*****shop*****"          
            name = item.getElementsByTagName('name')[0]
            print "Name: %s" % name.childNodes[0].data 
            if name.childNodes[0].data not in s: 
                s.append(name.childNodes[0].data)     
                sheet.write(rowNum,0,name.childNodes[0].data)        
                    
                price = item.getElementsByTagName('price')[0]
                print "Price: %s" % price.childNodes[0].data
                sheet.write(rowNum,1,price.childNodes[0].data)  
                     
                score = item.getElementsByTagName('score')[0]
                if len(score.childNodes)==0:
                    print "Score is NULL"
                    sheet.write(rowNum,2,"Null")
                else:   
                    print "Score: %s" % score.childNodes[0].data
                    sheet.write(rowNum,2,score.childNodes[0].data)
            
                rowNum+=1
    excel.save(d+".xls")
   
#     excel1=xlrd.open_workbook(d+".xls")
#     sheet1=excel1.sheets[0]
#     nrows=sheet1.nrows
#     for i in range(nrows):
#         for j in range(nrows):
  #          a=sheet1.row_values(i)[1]
  #          b=sheet1.row_values(j)[1]
  #      if a==b:
            
            
