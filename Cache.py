import redis
import Config

r = redis.StrictRedis(host=Config.get('redis_host'), port=Config.get('redis_port'), db=Config.get('redis_db'))
def get(arg):
    return r.get(arg)
def set(key, value, *arg):
    if arg[0]:
        return r.setex(key, int(arg[0]), value)
    return r.set(key, value)
