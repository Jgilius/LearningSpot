from django.db import models
from django.contrib.auth.models import User


class Learning_Intention(models.Model):
    title = models.CharField(max_length=150, default=None, blank=True)
    happy = models.ManyToManyField(User, default=None, blank=True, related_name='happy') #user added when they like and removed when unlike
    unsure = models.ManyToManyField(User, default=None, blank=True, related_name='unsure')
    sad = models.ManyToManyField(User, default=None, blank=True, related_name='sad')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
    @property
    def num_happy(self):
        return self.happy.all().count()

    @property
    def num_unsure(self):
        return self.unsure.all().count()

    @property
    def num_sad(self):
        return self.sad.all().count()

SELECT_CHOICES = (
    ('Select', 'Select'),
    ('Unselect', 'Unselect'),
)

class Happy_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)

class Unsure_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)

class Sad_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)