#coding=utf-8
'''
Created on 2014-10-30

@author: ZJ

'''

import xml.sax


class MovieHandler(xml.sax.ContentHandler): #xml.sax.handler中的ContentHandler
    def __init__(self): #__init__()方法:类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.CurrentData="" #记录当前数据
        self.type=""
        self.format=""
        self.year=""
        self.stars=""
        self.description=""
    #
    def startElement(self,tag,attributes):
        self.CurrentData=tag        
        if tag=="movie":
            print "----------movie----------"
            title=attributes["title"]
            print "Title:",title
            
    #
    def endElement(self, tag):
       if self.CurrentData=="type":
           print "type:",self.type
       elif self.CurrentData == "format":
         print "Format:", self.format
       elif self.CurrentData == "year":
         print "Year:", self.year
       elif self.CurrentData == "rating":
         print "Rating:", self.rating
       elif self.CurrentData == "stars":
         print "Stars:", self.stars
       elif self.CurrentData == "description":
         print "Description:", self.description
       self.CurrentData = ""  #置空
     #内容事件处理 ！！！！！！！！！！！！！
    def characters(self, content):
         if self.CurrentData == "type":
             self.type = content
         elif self.CurrentData == "format":
             self.format = content
         elif self.CurrentData == "year":
             self.year = content
         elif self.CurrentData == "rating":
             self.rating = content
         elif self.CurrentData == "stars":
             self.stars = content
         elif self.CurrentData == "description":
             self.description = content
         
if(__name__=="___main___"):
    #创建XMLReader
    parser =xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    #重写ContextHandler
    Handler=MovieHandler()
    parser.setContentHandler(Handler)
    
    parser.parse("E:/movies.xml")
    