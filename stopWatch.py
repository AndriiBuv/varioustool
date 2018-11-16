#! python

import time

input()
print ('Started')
startTime = time.time()

lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time()- lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        print("lap %s: %s(%s)" % (lapNum, totalTime, lapTime), end="")
        lapNum +=1
        lastTime = time.time()
except KeyboardInterrupt:

    print ('Done.')
    

if __name__ == '__main__':
    main()
