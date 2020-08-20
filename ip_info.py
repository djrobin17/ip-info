import urllib3
import json

http = urllib3.PoolManager()

r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))

IP=data['ip']
city = data['city']
region=data['region']
country=data['country']
org=data['org']

print ('Your IP details are-')
print ('IP : {0} \nCity : {1} \nRegion : {2} \nCountry : {3} \nOrg : {4}'.format(IP,city,region,country,org))
