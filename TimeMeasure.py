# Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>

import time

START_TIME = time.time()

# main function ##############
__import__("python.1000")
##############################

END_TIME = time.time()

print(f"time : {END_TIME-START_TIME}")