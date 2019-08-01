
import urllib.request
import urllib.parse
import json
import time
import re
result=''
file=open('traned_imagenet_synset_to_human_label_map.txt','w')
file.write(result)
file.close()
word_re=re.compile(r'.*')
file=open('imagenet_synset_to_human_label_map.txt')
index_dict=dict()
for line in file.readlines():
    cut_words=word_re.findall(str(line))
    for word in cut_words:
        if word!='' and word != '\n':
            content = word
            val="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
            data={}
            data['action']='FY_BY_REALTIME'
            data['client']='fanyideskweb'
            data['doctype']='json'
            data['from']='AUTO'
            data['i']=content
            data['keyfrom']='fanyi.web'
            data['salt']='1525252417040'
            data['sign']='4632e1f3f77f0c44a487ab5c674bf964'
            data['smartresult']='dict'
            data['to']='AUTO'
            data['typoResult']='false'
            data['version']='2.1'
            data=urllib.parse.urlencode(data).encode('utf-8')
            url=urllib.request.urlopen(val,data)
            html = url.read().decode('utf-8')
            a = json.loads(html)
            print(content,"翻译结果：%s" % (a['translateResult'][0][0]['tgt']))
            result=result+content+' '+a['translateResult'][0][0]['tgt']+'\n'
result=result[:-1]
file.close()
file=open('traned_imagenet_synset_to_human_label_map.txt','w')
file.write(result)
file.close()
