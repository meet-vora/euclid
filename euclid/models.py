from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import json

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	questions_solved = models.CharField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return self.user.username

	def addQuestionSolve(self, x):
		self.questions_solved = json.dumps(x)

	def getQuestionSolved(self, x):
		return json.loads(self.questions_solved)

class Question(models.Model):
	DIFFICULTY = (
			('easy', 'Easy'),
			('medium', 'Medium'),
			('hard', 'Hard'),
		)
	question_text = models.CharField(max_length=500)
	answer = models.IntegerField(default=0)
	level = models.CharField(max_length=10, choices = DIFFICULTY)
	def __unicode__(self):
		return self.question_text