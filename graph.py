from facepy import GraphAPI
import json
from json2html import *
import webbrowser
graph= GraphAPI('https://graph.facebook.com/endpoint?key=value&amp;access_token=185059841956329|dfe61870ac12dbdcc7b4d09893dbc49c')

print("Please enter the page-id  " )
PageId=raw_input()

variable = graph.get(str(PageId)+'/posts?fields=comments.limit(5){message},message&since=today&limit=5')


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
