from time import sleep
import datetime
import contextlib


@contextlib.contextmanager
def cm_timer_1():
    t1 = datetime.datetime.now()
    yield
    t2 = datetime.datetime.now()
    res = t2 - t1
    res1 = str(res.seconds) + '.' + str(res.microseconds)
    print('Execution time {0}'.format(res1))


class timer:
    def __enter__(self):
        self.t1 = datetime.datetime.now()

    def __exit__(self, exp_type, exp_value, traceback):
        t2 = datetime.datetime.now()
        res = t2 - self.t1
        print('Execution time {0}'.format(res))


print('cm_timer_1 start\n...\n')
with cm_timer_1():
    sleep(5.5)
print('\ncm_timer_2 start\n...\n')
with timer():
    sleep(5.5)