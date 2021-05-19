import redis
import random
import itertools
import time
import json

random.seed(10)


r = redis.Redis(host='redis', port=6379)

user_list = [
        {
            "display_name": "cyrus", 
            "user_id": "U63dfde5cbfb4f27e4426340af071f4e9",
            "profile_picture": "https://profile.line-scdn.net/0m0023cf0472519ec7177b4412fda4aea32c4c01a1cb0d",
        },
        {
            "display_name": "daniel", 
            "user_id": "U89d271431d4df4c4350f6fe0a52402e6",
            "profile_picture": "https://profile.line-scdn.net/0h3zG9r1ySbFV6QES2yjATAkYFYjgNbmodAnYrZg1DNWBQICtQTy8iY1pCNDFVd3sFFnR3MVdHNTED",
        },
        {
            "display_name": "Kent", 
            "user_id": "U677203191b7cdc1f3e2c0abaf04f4fe1",
            "profile_picture": "https://profile.line-scdn.net/0h-4xkJ3mXchtFEl35loANTHlXfHYyPHRTPXA8dGIbKShqJ2VIfXRufGRHLytpI2Yde3A0dDdHLCJp",
        },
        {
            "display_name": "raix", 
            "user_id": "U37d633173f03d391ff23bda8dd701c38",
            "profile_picture": "https://profile.line-scdn.net/0m035050fd7251734ee9666dc24fc14874bf3e2b42f4dd",
        },
        {
            "display_name": "ken", 
            "user_id": "U94d1249fab7813869873b2fe676c30bf",
            "profile_picture": "https://profile.line-scdn.net/0m033d8aca725135c46fdad88060e8350c5ecfa84553ad",
        },
        {
            "display_name": "Johnson", 
            "user_id": "U41ca649ecda7a098bd802fb41df410a2",
            "profile_picture": "https://profile.line-scdn.net/0m02d8cd9972510fbe6992820871478f41199a4fc57d66",
        },
        {
            "display_name": "彼得", 
            "user_id": "Ub0609ccd96268da5b3c69d23adfb0bb0",
            "profile_picture": "https://profile.line-scdn.net/0m02d7c5467251d536151f2e4d833ca6aa8161bac03d39",
        },
]
question_list = [str(i) for i in range(1, 11)]
#keys = itertools.product(user_list, question_list)

for ques in question_list:
    random.shuffle(user_list)
    for user in user_list:
        key = user['user_id']
        field = ques
        score = random.randint(80,100)
        user.update({"score": score, "question_num": ques})
        r.hsetnx(key, field, json.dumps(user))
        r.publish('develop', key)
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
