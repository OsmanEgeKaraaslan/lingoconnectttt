from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    finished_quizzes = models.ManyToManyField('Quiz', blank=True, default=None)
    total_score = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    false_answers = models.IntegerField(default=0)



    def update_correct_answers(self, num_correct):
        self.correct_answers += num_correct
        self.save()
    def update_false_answers(self, num_correct):
        self.false_answers += 10-num_correct
        self.save()




    def create_user_profile(sender, instance, created,**kwargs):
       if created:
        user_profile=UserProfile(user=instance)
        user_profile.save()

    post_save.connect(create_user_profile,sender=user)

    class Meta:
        app_label="app"






    objects = models.Manager()
class question(models.Model):
    text=models.CharField(max_length=10000)
    correct_answer=models.CharField(max_length=10000)
    option1=models.CharField(max_length=10000,null=True)
    option2=models.CharField(max_length=10000,null=True)
    option3=models.CharField(max_length=10000,null=True)
    option4=models.CharField(max_length=10000,null=True)
    number_of_fails=models.IntegerField(null=True)
    number_of_passes=models.IntegerField(null=True)
    total_number=models.IntegerField(null=True)
    category=models.CharField(max_length=1500)
    difficulty=models.CharField(max_length=1500)


    objects = models.Manager()
class Quiz(models.Model):
    name=models.TextField()
    category=models.CharField(max_length=15)
    difficulty=models.CharField(max_length=15)
    q1=models.ForeignKey(question,related_name='%(class)s_requests_created10',on_delete=models.CASCADE)
    q2=models.ForeignKey(question,related_name='%(class)s_requests_created9',on_delete=models.CASCADE)
    q3=models.ForeignKey(question,related_name='%(class)s_requests_created8',on_delete=models.CASCADE)
    q4=models.ForeignKey(question,related_name='%(class)s_requests_created7',on_delete=models.CASCADE)
    q5=models.ForeignKey(question,related_name='%(class)s_requests_created6',on_delete=models.CASCADE)
    q6=models.ForeignKey(question,related_name='%(class)s_requests_created5',on_delete=models.CASCADE)
    q7=models.ForeignKey(question,related_name='%(class)s_requests_created4',on_delete=models.CASCADE)
    q8=models.ForeignKey(question,related_name='%(class)s_requests_created3',on_delete=models.CASCADE)
    q9=models.ForeignKey(question,related_name='%(class)s_requests_created2',on_delete=models.CASCADE)
    q10=models.ForeignKey(question,related_name='%(class)s_requests_created1',on_delete=models.CASCADE)
    objects = models.Manager()
