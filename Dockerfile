FROM registry.cn-beijing.aliyuncs.com/ctgpub/python27-with-flask-redis:1.0-alpine
ENV REDIS_HOST "redis"
COPY comment_redis.py /
EXPOSE 80
CMD ["python", "/comment_redis.py"]
