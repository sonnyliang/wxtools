# 3. 在需要使用异步的app中定义task
from celery import shared_task

@shared_task
def dosomething():
    return 'hello'