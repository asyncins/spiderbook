import time
from datetime import datetime
def wait():
    time.sleep(5)
print("开始", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
wait()
print("结束", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))