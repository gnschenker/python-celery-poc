import time
from tasks import add, do_long_running_task, book_received

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

book_received.apply_async(
    args=['NHibernate 4.0 for Beginners'],
    queue='books',
    routing_key='books')

book_received.apply_async(
    args=['The big storm'],
    queue='books',
    routing_key='books')

do_long_running_task.delay('Hello')
do_long_running_task.delay('World!')
