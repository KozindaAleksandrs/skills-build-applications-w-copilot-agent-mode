from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL, related_name='users')
    workouts = models.ArrayReferenceField('Workout', null=True, blank=True, related_name='user_workouts')
    activities = models.ArrayReferenceField('Activity', null=True, blank=True, related_name='user_activities')
    leaderboard = models.ArrayReferenceField('Leaderboard', null=True, blank=True, related_name='user_leaderboards')

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField('User', null=True, blank=True, related_name='team_members')

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities_set')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Workout(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='workouts_set')
    description = models.TextField()
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='leaderboards_set')
    score = models.IntegerField()

