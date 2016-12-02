from facepy import GraphAPI
import json
from json2html import *
import webbrowser
graph= GraphAPI('EAACoT5okWekBAE3Np7Gt4SpAuuaVodn0FVqUxeQ6FLgwgOCRC4vPZBU6tjtnv4HBpZCqzihehOmZAHc5xTcKFWEuAVnqERPkvtKZAWNIcOCs1RHHJBHrFwDx6d2Fn8QiJxW1XtZBNAxV3ZBeoW1IO56Juz2LGEM5aFgZBBKZAuVnqgZDZD')

print("Please enter the page-id  " )
PageId=raw_input()

variable = graph.get(str(PageId)+'/posts?fields=comments.limit(4){message},message&since=today&limit=4')


import json
with open('data.json', 'wb') as outfile:
    json.dump(variable, outfile)

#infoFromJson = json.loads(variable)
table = json2html.convert(json = variable)
htmlfile=table.encode('utf-8')
#print(htmlfile)
f = open('Table.html','w')
f.write(htmlfile)
f.close()

webbrowser.open("Table.html")
