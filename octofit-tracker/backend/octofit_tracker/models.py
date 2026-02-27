from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    workouts = models.ArrayReferenceField('Workout', null=True, blank=True)
    activities = models.ArrayReferenceField('Activity', null=True, blank=True)
    leaderboard = models.ArrayReferenceField('Leaderboard', null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField('User', null=True, blank=True)

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    score = models.IntegerField()

