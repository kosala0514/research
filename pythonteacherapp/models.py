from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    test_marks = models.FloatField(max_length=15, default='0.00', editable=False)
    chapter_level = models.IntegerField(default=1, editable=False)
    assignment_level = models.IntegerField(default=1, editable=False)
    assignment_progress_level = models.IntegerField(default=1, editable=False)

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

class Assignment(models.Model):
    message = models.CharField(max_length=200)
    assignment_progress_level = models.CharField(max_length=200)
    assignment_level = models.CharField(max_length=200)
    answer = models.TextField()
    time = models.TextField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
