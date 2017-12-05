#!/usr/bin/env python
#encoding=utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import MySQLdb
import re
import sys
import types
app=Flask(__name__)

reload(sys)
sys.setdefaultencoding("utf-8")


conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='a821200725',
    db='webjob',
    charset='utf8'
)

#sys.setdefaultencoding('utf-8')

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        InNumber=request.form['InNumber']
        InNumber=numsort(InNumber)
        return render_template('index.html',result=InNumber)
    else: 
        return render_template('index.html')

@app.route('/province',methods=['POST','GET'])
def province():
    if request.method=='POST':
        rev=request.get_json()['city']
        result=selcity(rev)
        return result
    else:
        return render_template('province.html')


def numsort(number):
    print number
#    tmp=number.split(' *')
    tmp=re.split("\s+",number)
    print tmp
    for i in range(len(tmp)):
        tmp[i]=int(tmp[i])
    print tmp
    tmp.sort()
    res=""
    for i in tmp:
        res+=(str(i)+" ")
    return res

def selcity(city):
    sql="select litcity from Bigcity where city='"+city+"'"
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchone()
    results=result[0]
#    results=results.decode("unicode-escape")
    return results



if __name__=='__main__':
    app.run(debug=True)