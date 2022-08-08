from django.db import models

class learning_intention(models.Model):
    id = models.AutoField(primary_key=True)
    li = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.li

#------------------------------------------------------------------------------------------

class learning_task(models.Model):
    id = models.AutoField(primary_key=True)
    lt = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lt