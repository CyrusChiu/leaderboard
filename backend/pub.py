import redis
import random
import itertools
import time

random.seed(10)


r = redis.Redis(host='redis', port=6379)

user_list = [
    "cyrus",
    "daniel",
    "kent",
    "raix",
    "ken",
    "johnson",
    "peter"
]
question_list= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#keys = itertools.product(user_list, question_list)

for ques in question_list:
    random.shuffle(user_list)
    for user in user_list:
        key = user
        field = ques
        val = random.randint(80,100)
        r.hsetnx(key, field, val)
        r.publish('develop', user)
    time.sleep(5)



#for each in keys:
#    r.publish('develop', each[0]) 
#    key = each[0]
#    field = each[1]
#    val = random.randint(80, 100)
#    r.hsetnx(key, field, val)
#    print (each[0])
#    time.sleep(0.5)

#for i in range(len(question_list)):
#    key = f'{user_a}'
#    field = question_list[i]
#    val = int(score_1[i])
#    r.hsetnx(key, field, val)
#
