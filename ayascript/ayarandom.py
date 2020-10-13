import datetime
import re
import math
import time

def __getseed():
    timer = str(datetime.datetime.now())
    timer = int(re.sub("[-.: ]", "", timer)[-10:])
    s1, s2, s3 = timer, math.floor(timer/2), math.floor(timer/4)
    time.sleep(.01)
    return [s1, s2, s3]

def __randomise(seeds):
    seed1 = (171*seeds[0]) % 30269
    seed2 = (172 * seeds[0]) % 30307
    seed3 = (170 * seeds[0]) % 30323
    return (seed1/30269 + seed2/30307 + seed3/30323) % 1

def number(bottom, top):
    seed = __getseed()
    rng = __randomise(seed)
    nums = range(bottom, top+1)
    return nums[math.floor(rng*len(nums))]

def choice(inputs):
    seed = __getseed()
    rng = __randomise(seed)
    return inputs[math.floor(rng*len(inputs))]