import os, json, requests, time

url = 'http://bootcamp-api.transferwise.com/'
task1 = 'payment/history'
task2 = 'payment'
task3 = 'fraud'
token = '?token=82c83634209f2ade37925f9ce415f2fbd9df7984'
method1 = ' -X PUT'
method2 = ' -X DELETE'
start = 'curl http://bootcamp-api.transferwise.com/task/6/start?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'
fin = 'curl http://bootcamp-api.transferwise.com/task/finish?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'

fraud_ip = ''
frauds = []
norms = []
pays = requests.get(url + task2 + token).json()
illegals = requests.get(url + task1 + token).json()

os.system(start)
time.sleep(1)

for ill in illegals:
    if ill['fraud'] == True:
        fraud_ip = ill['ip'][:-3]
        print fraud_ip
        break

for pay in pays:
    if fraud_ip in (pay)['ip']:
        frauds.append(pay['id'])
    else:
        norms.append(pay['id'])

for f in frauds:
    os.system('curl ' + url + task2 + '/' + f + '/' + task3 + token + method1)

for n in norms:
    os.system('curl ' + url + task2 + '/' + n + '/' + task3 + token + method2)

time.sleep(2)
os.system(fin)