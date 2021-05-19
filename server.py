import asyncio
from datetime import datetime
import json
#import logging
import os
import time

import redis
import websockets
import concurrent.futures


loop = asyncio.get_event_loop()
pool = concurrent.futures.ThreadPoolExecutor((os.cpu_count() or 1))


cache = redis.StrictRedis(host="redis", port=6379, decode_responses=True)


def get_data_from_redis(key):
    sum_score = redis_sum_all_scores(key)
    return str(sum_score)
    #print (key, sum_score)

def redis_sum_all_scores(key):
    print (f"getting user data: {key}")
    scores = cache.hgetall(key)
    scores = list(scores.values())
    scores = [int(x) for x in scores]
    sum_score = sum(scores)
    print (f"user: {key}, score: {sum_score}")
    return sum_score



def redis_sub(pubsub):
    #try:
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = message.get("data")
            return str(data)
    #except:
    #    time.sleep(1)
    #    return "waiting..."




async def pull(websocket, path):

    pubsub = cache.pubsub()
    pubsub.subscribe(['develop'])
    
    leaderboard = {}

    while True:
        #try:
        #message = await websocket.recv()

        redis_key = await loop.run_in_executor(pool, redis_sub, pubsub)
        if not redis_key:
            continue
        
        new_score = get_data_from_redis(redis_key)

        # sum the result
        leaderboard[redis_key] = new_score


        await websocket.send(json.dumps(leaderboard))

        #response1 = await loop.run_in_executor(pool, get_data_from_redis, message)

        #await websocket.send(response1)

        #except Exception as e:
            #logging.error(e) 

if __name__=='__main__':      
    start_server = websockets.serve(pull, '0.0.0.0', 5000)
    loop.run_until_complete(start_server)
    loop.run_forever()
