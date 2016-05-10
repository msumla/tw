import os, time

url = 'http://bootcamp-api.transferwise.com/'
task1 = 'hiddenFee/forCompany/'
bank = 'HighStreetBank'
bank1 = 'HighStreetBank1/'
bank2 = 'HighStreetBank2/'
bank3 = 'HighStreetBank3/'
am = 100
task2 = '/EUR/USD/'
pc = 0
token = '?token=82c83634209f2ade37925f9ce415f2fbd9df7984'
method = ' -X POST'
start = 'curl http://bootcamp-api.transferwise.com/task/4/start?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'
fin = 'curl http://bootcamp-api.transferwise.com/task/finish?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'

for a in range(100):
    am = 100
    print('Cycle: ' + str(a+1), '')
    os.system(start)
    print('', '')
    time.sleep(1)
    for i in range(3):
        os.system('curl '+url+task1+bank+str(i+1)+'/'+str(am)+task2+str(pc)+str('.0')+token+method)
        print('', '')
        am *= 10
        time.sleep(1)
    pc += 1
    os.system(fin)
    print('Percentage: ' + str(pc))
    time.sleep(2)

os.system('curl '+url+task1+bank1+str(am)+task2+str(pc)+str('3.0')+token+method)
time.sleep(1)
os.system('curl '+url+task1+bank2+str(am)+task2+str(pc)+str('3.0')+token+method)
time.sleep(1)
os.system('curl '+url+task1+bank3+str(am)+task2+str(pc)+str('5.0')+token+method)
time.sleep(2)
os.system(fin)
