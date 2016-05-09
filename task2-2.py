# this one really seemed like an infinite loop, so I thought I'd try a different approach, scripting myself out of this!

import os, time

url = 'http://bootcamp-api.transferwise.com/'
task1 = 'survivor/'
token = '?token=82c83634209f2ade37925f9ce415f2fbd9df7984'
method = ' -X POST'
start = 'curl http://bootcamp-api.transferwise.com/task/2/start?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'
fin = 'curl http://bootcamp-api.transferwise.com/task/finish?token=82c83634209f2ade37925f9ce415f2fbd9df7984 -X POST'

for a in range(1):
    print('Cycle: ' + str(a+1), '\n')
    os.system(start)
    print('\n')
    time.sleep(1)
    os.system('curl '+url+task1+str(31)+'/'+token+method)
    print('\n')
    time.sleep(1)
    os.system(fin)
    print('Chair no: ' + str(a))
    time.sleep(2)
