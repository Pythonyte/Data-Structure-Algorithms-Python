from datetime import timedelta, datetime
import threading
import logging
from time import sleep
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-1s) %(message)s',
                    )

class RateLimiter:
    mapping = {}
    def __init__(self, thottling_period, rate_limit):
        """
        :param thottling: int time In seconds
        :param rate_limit: int count
        """
        self.thottling_period = thottling_period
        self.rate_limit = rate_limit
        self.sem = threading.Semaphore(1)

    def calculate_end_time(self, current_time):
        return current_time + timedelta(seconds=self.thottling_period)

    def __check_limit(self, unique_id, current_time, end_time):
        if unique_id not in self.mapping:
            self.mapping[unique_id] = {
                'count': 1,
                'end_time': end_time
            }
        elif current_time > self.mapping[unique_id]['end_time']:
            self.mapping[unique_id] = {
                'count': 1,
                'end_time': end_time
            }
        elif self.mapping[unique_id]['count'] < self.rate_limit:
            self.mapping[unique_id]['count'] += 1
        else:
            logging.info("Next request for UID=>{} has been throttled".format(unique_id))
            return False
        logging.info("UID=>{} Count=>{} EndTime=>{} RequestTime=>{}".format(
            unique_id,
            self.mapping[unique_id]['count'],
            str(self.mapping[unique_id]['end_time']),
            str(current_time)
        ))
        return True

    def check_limit(self, unique_id, current_time):
        end_time = self.calculate_end_time(current_time)
        # Critical Section Starts
        self.sem.acquire()
        self.__check_limit(unique_id, current_time, end_time)
        self.sem.release()
        # Critical Section Ends



################## Example ##################
# 5 req per 10 seconds by each userid
rl = RateLimiter(thottling_period=10, rate_limit=5)
for i in range(100):
    sleep(.2)
    threading.Thread(
        target=rl.check_limit,
        name="t{}".format(i),
        args=(i%5, datetime.now())
    ).start()

###OUTPUT####
(t0) UID=>0 Count=>1 EndTime=>2020-03-06 00:01:24.010280 RequestTime=>2020-03-06 00:01:14.010280
(t1) UID=>1 Count=>1 EndTime=>2020-03-06 00:01:24.211592 RequestTime=>2020-03-06 00:01:14.211592
(t2) UID=>2 Count=>1 EndTime=>2020-03-06 00:01:24.412956 RequestTime=>2020-03-06 00:01:14.412956
(t3) UID=>3 Count=>1 EndTime=>2020-03-06 00:01:24.614784 RequestTime=>2020-03-06 00:01:14.614784
(t4) UID=>4 Count=>1 EndTime=>2020-03-06 00:01:24.816427 RequestTime=>2020-03-06 00:01:14.816427
(t5) UID=>0 Count=>2 EndTime=>2020-03-06 00:01:24.010280 RequestTime=>2020-03-06 00:01:15.017977
(t6) UID=>1 Count=>2 EndTime=>2020-03-06 00:01:24.211592 RequestTime=>2020-03-06 00:01:15.219836
(t7) UID=>2 Count=>2 EndTime=>2020-03-06 00:01:24.412956 RequestTime=>2020-03-06 00:01:15.421437
(t8) UID=>3 Count=>2 EndTime=>2020-03-06 00:01:24.614784 RequestTime=>2020-03-06 00:01:15.622916
(t9) UID=>4 Count=>2 EndTime=>2020-03-06 00:01:24.816427 RequestTime=>2020-03-06 00:01:15.824512
(t10) UID=>0 Count=>3 EndTime=>2020-03-06 00:01:24.010280 RequestTime=>2020-03-06 00:01:16.026135
(t11) UID=>1 Count=>3 EndTime=>2020-03-06 00:01:24.211592 RequestTime=>2020-03-06 00:01:16.227994
(t12) UID=>2 Count=>3 EndTime=>2020-03-06 00:01:24.412956 RequestTime=>2020-03-06 00:01:16.429679
(t13) UID=>3 Count=>3 EndTime=>2020-03-06 00:01:24.614784 RequestTime=>2020-03-06 00:01:16.631384
(t14) UID=>4 Count=>3 EndTime=>2020-03-06 00:01:24.816427 RequestTime=>2020-03-06 00:01:16.832968
(t15) UID=>0 Count=>4 EndTime=>2020-03-06 00:01:24.010280 RequestTime=>2020-03-06 00:01:17.034405
(t16) UID=>1 Count=>4 EndTime=>2020-03-06 00:01:24.211592 RequestTime=>2020-03-06 00:01:17.235897
(t17) UID=>2 Count=>4 EndTime=>2020-03-06 00:01:24.412956 RequestTime=>2020-03-06 00:01:17.437369
(t18) UID=>3 Count=>4 EndTime=>2020-03-06 00:01:24.614784 RequestTime=>2020-03-06 00:01:17.638739
(t19) UID=>4 Count=>4 EndTime=>2020-03-06 00:01:24.816427 RequestTime=>2020-03-06 00:01:17.840207
(t20) UID=>0 Count=>5 EndTime=>2020-03-06 00:01:24.010280 RequestTime=>2020-03-06 00:01:18.041773
(t21) UID=>1 Count=>5 EndTime=>2020-03-06 00:01:24.211592 RequestTime=>2020-03-06 00:01:18.243463
(t22) UID=>2 Count=>5 EndTime=>2020-03-06 00:01:24.412956 RequestTime=>2020-03-06 00:01:18.444917
(t23) UID=>3 Count=>5 EndTime=>2020-03-06 00:01:24.614784 RequestTime=>2020-03-06 00:01:18.645842
(t24) UID=>4 Count=>5 EndTime=>2020-03-06 00:01:24.816427 RequestTime=>2020-03-06 00:01:18.846714
(t25) Next request for UID=>0 has been throttled
(t26) Next request for UID=>1 has been throttled
(t27) Next request for UID=>2 has been throttled
(t28) Next request for UID=>3 has been throttled
(t29) Next request for UID=>4 has been throttled
(t30) Next request for UID=>0 has been throttled
(t31) Next request for UID=>1 has been throttled
(t32) Next request for UID=>2 has been throttled
.....
