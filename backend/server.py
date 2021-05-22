import asyncio
import concurrent.futures
import json
# import logging
import os
import time
from datetime import datetime

import redis
import websockets

loop = asyncio.get_event_loop()
pool = concurrent.futures.ThreadPoolExecutor((os.cpu_count() or 1))


cache = redis.StrictRedis(host="redis", port=6379, decode_responses=True)


def get_data_from_redis(key):
    data = redis_sum_all_scores_by(key)
    return data
    # print (key, sum_score)


def redis_sum_all_scores_by(key):
    print(f"getting user data: {key}")
    _data = cache.hgetall(key)
    data = [json.loads(x) for x in _data.values()]
    scores = [int(each["score"]) for each in data]
    sum_score = sum(scores)
    new_data = {
        "user_id": data[-1]["user_id"],
        "display_name": data[-1]["display_name"],
        "profile_picture": data[-1]["profile_picture"],
        "score": sum_score,
    }
    return new_data


def redis_create_snapshot(data):
    ts = round(time.time() * 1000)
    cache.zadd("snapshot", {json.dumps(data): ts})


def redis_sub(pubsub):
    # try:
    for message in pubsub.listen():
        if message["type"] == "message":
            data = message.get("data")
            return str(data)
    # except:
    #    time.sleep(1)
    #    return "waiting..."


async def pull(websocket, path):

    pubsub = cache.pubsub()
    pubsub.subscribe(["develop"])

    leaderboard = {}

    while True:
        # try:
        # message = await websocket.recv()

        redis_key = await loop.run_in_executor(pool, redis_sub, pubsub)
        if not redis_key:
            continue

        new_data = get_data_from_redis(redis_key)

        # sum the result
        leaderboard[redis_key] = new_data
        redis_create_snapshot(leaderboard)

        await websocket.send(json.dumps(leaderboard))

        # response1 = await loop.run_in_executor(pool, get_data_from_redis, message)

        # await websocket.send(response1)

        # except Exception as e:
        # logging.error(e)


if __name__ == "__main__":
    start_server = websockets.serve(pull, "0.0.0.0", 5000)
    loop.run_until_complete(start_server)
    loop.run_forever()
