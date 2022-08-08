from django.db import models

class learning_intention(models.Model):
    id=models.AutoField(primary_key=True)
    li = models.CharField(max_length=100,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.li


#------------------------------------------------------------------------------------------



