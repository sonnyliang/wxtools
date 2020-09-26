from django.db import models

# Create your models here.

class todoListCollect(models.Model):
    listName = models.CharField(max_length=256,default='default')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        # 当managed = False 的时候不会进行数据迁移操作
        managed = False
        db_table = 'todoListCollect'

    def __str__(self):
        return self.name
    

class todoList(models.Model):
    user = models.CharField(max_length=256)
    todo = models.CharField(max_length=256)
    todoType = models.CharField(max_length=32)
    listName = models.ForeignKey(todoListCollect, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 当managed = False 的时候不会进行数据迁移操作
        managed = False
        db_table = 'todoList'
