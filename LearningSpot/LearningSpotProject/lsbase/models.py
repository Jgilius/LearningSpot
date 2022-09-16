from django.db import models
from django.contrib.auth.models import User

# Model for learning intention, creating objects by the input of a title. 
# happy, unsure and sad attributes are connected to corresponding class via M:M relationship

class Learning_Intention(models.Model):
    title = models.CharField(max_length=150,  default=None, blank=True)
    happy = models.ManyToManyField(User, default=None, blank=True, related_name='happy') 
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

# select options for button action logic
SELECT_CHOICES = (
    ('Select', 'Select'),
    ('Unselect', 'Unselect'),
)

# Student response to learning intention
class Happy_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)

# Student response to learning intention
class Unsure_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)

# Student response to learning intention
class Sad_Select(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_intention = models.ForeignKey(Learning_Intention, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_intention)

# Model for learning task, creating objects by the input of a title. 
# notstarted, inprogress, complete and need help attributes are connected to corresponding class via M:M relationship
class Learning_Task(models.Model):
    title = models.CharField(max_length=150,  default=None, blank=True)
    notstarted = models.ManyToManyField(User, default=None, blank=True, related_name='notstarted')
    inprogress = models.ManyToManyField(User, default=None, blank=True, related_name='inprogress')
    complete = models.ManyToManyField(User, default=None, blank=True, related_name='complete')
    needhelp = models.ManyToManyField(User, default=None, blank=True, related_name='needhelp')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ltauthor', blank=True, null=True)

    def __str__(self):
        return str(self.title)

    @property
    def num_happy(self):
        return self.notstarted.all().count()

    @property
    def num_unsure(self):
        return self.inprogress.all().count()

    @property
    def num_sad(self):
        return self.complete.all().count()
    
    @property
    def num_sad(self):
        return self.needhelp.all().count()

# Student response to learning task
class LTComplete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_task = models.ForeignKey(Learning_Task, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_task)

# Student response to learning task
class LTNotStarted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_task = models.ForeignKey(Learning_Task, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_task)

# Student response to learning task
class LTInProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_task = models.ForeignKey(Learning_Task, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_task)

# Student response to learning task
class LTNeedHelp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_task = models.ForeignKey(Learning_Task, on_delete=models.CASCADE)
    value = models.CharField(choices=SELECT_CHOICES, default='Select', max_length=10)

    def __str__(self):
        return str(self.learning_task)