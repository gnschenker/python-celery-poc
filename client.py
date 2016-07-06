import time
from tasks import add, do_long_running_task

def calculator(a, b):
    result = add.delay(a,b)
    while result.ready() == False:
        time.sleep(1)
    print('Result: %d + %d = %d' % (a,b,result.get()))

print("********* Waiting for 10 sec **************")
time.sleep(10)

calculator(2,2)
calculator(3,2)
calculator(4,2)
calculator(2,5)

do_long_running_task('Hello')
do_long_running_task('World!')