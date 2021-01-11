from django.db import models
from django.contrib.auth.models import User




class Quiz(models.Model):
	name = models.CharField(max_length=200,default="",blank=False)
	questions_count = models.IntegerField(default="")
	description = models.TextField(max_length=10000,default="",blank=False)
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	slug = models.SlugField(max_length=200,unique=True,blank=False)
	roll_out = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,default="",related_name='quiz')
	label = models.CharField(max_length=2000,default="")
	order = models.IntegerField(default="")

	def __str__(self):
		return self.label



class Answer(models.Model):
	question =models.ForeignKey(Question, on_delete=models.CASCADE,default="")
	correct = models.BooleanField(default="")
	text = models.CharField(max_length=1000,default="")

	def __str__(self):
		return self.text


class QuizTaker(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,default="")
	user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
	correct_answers = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	score = models.FloatField()

	def __str__(self):
		return self.user.username



class Response(models.Model):
	quiztaker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE,default="")
	question = models.ForeignKey(Question, on_delete=models.CASCADE,default="")
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.question.label


# class UserAnswer(models.Model):
# 	quiz_taker = models.ForeignKey(QuizTaker,on_delete=CASCADE,default="")
# 	question = models.ForeignKey(Question,on_delete=CASCADE,default="")
# 	answer = models.ForeignKey(Answer,on_delete=CASCADE,null=True)

# 	def __str(self):
# 		return self.question.label


