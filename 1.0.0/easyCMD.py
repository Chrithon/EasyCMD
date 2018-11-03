import os
import time


print("""EasyCMD 1.0.0
ying2002 2018-10""")
while True:
    cmd = input("EasyCMD:")
    if cmd == "exit":
        exit()
    if cmd == "about":
        print("""
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                       EasyCMD 1.0.0
                                   Written by Python 3.6
                                     Author ying2002
                               Putuo District, Shanghai, China
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        A simple CMD based on Windows CMD and written by Python.
        ========================================================================
        """)
        time.sleep(4)
    else:
        os.system(cmd)
