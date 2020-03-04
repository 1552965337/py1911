# author sqz
# date 2020/3/4 14:24
# file_name throttling
from rest_framework import throttling

class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon':'200/day'
    }

class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user':'400/day'
    }