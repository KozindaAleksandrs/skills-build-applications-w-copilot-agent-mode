from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(username='IronMan', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(username='CaptainAmerica', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(username='Hulk', email='bruce@marvel.com', team=marvel)
        clark = User.objects.create(username='Superman', email='clark@dc.com', team=dc)
        brucew = User.objects.create(username='Batman', email='bruce@dc.com', team=dc)
        diana = User.objects.create(username='WonderWoman', email='diana@dc.com', team=dc)

        # Add members to teams
        marvel.members.set([tony, steve, bruce])
        dc.members.set([clark, brucew, diana])

        # Create Workouts
        w1 = Workout.objects.create(user=tony, name='Chest Day', duration=60)
        w2 = Workout.objects.create(user=clark, name='Leg Day', duration=45)

        # Create Activities
        a1 = Activity.objects.create(user=tony, type='Run', distance=5)
        a2 = Activity.objects.create(user=clark, type='Swim', distance=2)

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
