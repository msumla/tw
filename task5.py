import os, json, requests, time

d = []
pep = []
peps_ = []
pep_ids = []
no_pep_ids = {}
url = 'http://bootcamp-api.transferwise.com/'
task1 = 'payment/'
task2 = '/aml'
token = '?token=82c83634209f2ade37925f9ce415f2fbd9df7984'
method1 = ' -X PUT'
method2 = ' -X DELETE'
start = 'curl http://bootcamp-api.transferwise.com/task/5/start?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'
fin = 'curl http://bootcamp-api.transferwise.com/task/finish?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'

os.system(start)
time.sleep(1)

peps = requests.get(url + 'task' + token).json()['peps']
for p in peps:
    pep.append(p)
for index in pep:
    pepe, couy = index.split('-')
    peps_.append(pepe[:-1])

pays = requests.get(url + 'payment' + token).json()
for pay in pays:
    d.append(pay)

for i in d:
    for a in range(len(peps_)):
        if peps_[a] in i['recipientName']:
            pep_ids.append(i['id'])
            print('')
        else:
            no_pep_ids[i['id']] = a

for id in pep_ids:
    os.system('curl ' + url + task1 + id + task2 + token + method1)

for id in no_pep_ids:
    os.system('curl ' + url + task1 + id + task2 + token + method2)

time.sleep(3)
os.system(fin)