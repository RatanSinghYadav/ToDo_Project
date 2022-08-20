from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    status_choices =[
        ('Completed', 'COMPLETED'),
        ('Panding','PENDING')

    ]

    priority_choices =  [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟')


    ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10 , choices= status_choices)
    date = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    priority = models.CharField(max_length=10 , choices=priority_choices)
