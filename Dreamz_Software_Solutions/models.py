from django.db import models
class signupUser(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    date_of_birth=models.DateField(auto_now=False,auto_now_add=False)
    profile_image=models.ImageField(upload_to='Profile_Image',blank=True)
    security_question=models.CharField(max_length=100)
    question_answer=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name