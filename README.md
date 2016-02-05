# Lifecell API
Python library for interfacing with [lifecell](http://lifecell.com.ua) API.

Based on [life-api Ruby library](https://github.com/mamantoha/life-api/)

## Sample usage

```python
from  lifecellapi import LifecellApi, LifecellSession
import json

msisdn = '380931234567'
pwd = '123456'
s = LifecellSession(msisdn, pwd)
api = LifecellApi(s)
ansv = api.getBalances()

print json.dumps(ansv, indent=4)
```

Response

```
{
    "@method": "getBalances", 
    "responseCode": "0", 
    "balance": [
        {
            "@code": "Bundle_Gprs_Internet", 
            "@amount": "0.00", 
            "measure": "Bytes", 
            "name": "Free Internet"
        }, 
        {
            "@code": "GigaInternet_Count", 
            "@amount": "0.00", 
            "measure": "Bytes", 
            "name": "Free Internet [Internet, EDGE+/GPRS+]"
        }, 
        {
            "@code": "Bundle_Gprs_All", 
            "@amount": "0.00", 
            "measure": "Bytes", 
            "name": "Free Internet [Internet, WAP]"
        }, 
        {
            "@code": "Bundle_Gprs_All_CMS", 
            "@amount": "0.00", 
            "measure": "Bytes", 
            "name": "Free Internet [Internet, WAP]: CMS"
        }, 
        {
            "@code": "Bundle_Gprs_Internet_Youth", 
            "@amount": "0.00", 
            "measure": "Bytes", 
            "name": "Internet Crazy Day 2016"
        }, 
        {
            "@code": "Bundle_Internet_3G_Tariff", 
            "@amount": "3219587072.00", 
            "measure": "Bytes", 
            "name": "\u0110\u02d8ariff package of 3G Internet"
        }, 
        {
            "@code": "Bundle_Mms_Ukraine", 
            "@amount": "0.00", 
            "measure": "MMS", 
            "name": "Free MMS [in Ukraine]"
        }, 
        {
            "@code": "ICB_Counter_Minutes", 
            "@amount": "0.00", 
            "measure": "Minutes", 
            "name": "Minutes [incomming call from other networks]"
        }, 
        {
            "@code": "Bundle_Sms_Ukraine", 
            "@amount": "997.00", 
            "measure": "SMS", 
            "name": "Free SMS [in Ukraine]"
        }, 
        {
            "@code": "Bundle_Sms_Onnet", 
            "@amount": "0.00", 
            "measure": "SMS", 
            "name": "Free SMS [life:) network]"
        }, 
        {
            "@code": "Bundle_Youth_Voice_Omo_Pstn", 
            "@amount": "0.00", 
            "measure": "Seconds", 
            "name": "Crazy Day classic - Minutes to other mobile operators"
        }, 
        {
            "@code": "Bundle_UsageN_FF_FREE", 
            "@amount": "0.00", 
            "measure": "Seconds", 
            "name": "Free minutes [Family Numbers]"
        }, 
        {
            "@code": "Bundle_Voice_Onnet", 
            "@amount": "13391280.00", 
            "measure": "Seconds", 
            "name": "Free minutes [life:) network]"
        }, 
        {
            "@code": "Bundle_Voice_Offnet", 
            "@amount": "12000.00", 
            "measure": "Seconds", 
            "name": "Free minutes [other mobile operators and fixed-line numbers]"
        }, 
        {
            "@code": "Line_Bonus", 
            "@amount": "0.00", 
            "measure": "UAH", 
            "name": "Line Bonus"
        }, 
        {
            "@code": "Line_Main", 
            "@amount": "1.96", 
            "measure": "UAH", 
            "name": "Line Main"
        }
    ]
}
```

