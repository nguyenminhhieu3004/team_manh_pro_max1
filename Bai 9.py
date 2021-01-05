import os
import time
shutdown = True
while shutdown:
    shutdown = input("Do you want to Shutdown? (nhập yes hoặc no) ")
    if shutdown =="yes" :
        os.system('shutdown -s')
        shutdow = False
    else:
        print("chờ 1 lát rồi được hỏi lại")
        time.sleep(30)
© 2021 GitHub, Inc.