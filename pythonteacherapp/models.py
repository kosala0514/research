from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    test_marks = models.FloatField(max_length=15, default='0.00', editable=False)

    class Meta:
        db_table = 'user'

class PreTest(models.Model):
    question = models.CharField(max_length=256)
    explanation = models.CharField(max_length=256)
    answer_A = models.CharField(max_length=100)
    answer_B = models.CharField(max_length=100)
    answer_C = models.CharField(max_length=100)
    answer_D = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    class Meta:
        db_table = 'pre_test'

