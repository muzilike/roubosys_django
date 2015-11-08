# encoding: utf-8
import urllib2
import json

def now():
    res_text = ""
    url = "http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=shanghai"
    apikey = "f90d577c266f1869340ae74e1c409669"
    headers = { 'apikey' : apikey}
    req = urllib2.Request(url = url, headers = headers)
    f = urllib2.urlopen(req)
    res = json.loads(f.read())
    if res["errMsg"] == "success":
        res_text = u"城市: " + res["retData"]["city"] + '\n'
        res_text = res_text + u"天气:" + res["retData"]["weather"] + "\n"
        res_text = res_text + u"温度: " + res["retData"]["tmp"] + "\n"
        res_text = res_text + u"温度范围: " + res["retData"]["l_tmp"] + "~" + res["retData"]["h_tmp"] + "\n"
    else:
        res_text = "Get weather failed: " + res["errMsg"]
    return res_text
