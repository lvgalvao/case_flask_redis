from redis_om import get_redis_connection

redis_db = get_redis_connection(
    host = '0.0.0.0', port='6379'
)