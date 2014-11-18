import redis
import Config

r = redis.StrictRedis(host=Config.get('redis_host'), port=Config.get('redis_port'), db=Config.get('redis_db'))
def get(arg):
    return r.get(arg)
def set(key, value):
    return r.set(key, value)
