from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users with unique _id
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities with unique activity_id
        activities = [
            {"_id": ObjectId(), "activity_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": "01:00:00"},
            {"_id": ObjectId(), "activity_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": "02:00:00"},
            {"_id": ObjectId(), "activity_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": "01:30:00"},
            {"_id": ObjectId(), "activity_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": "00:30:00"},
            {"_id": ObjectId(), "activity_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": "01:15:00"},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries with unique leaderboard_id
        leaderboard = [
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "leaderboard_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts with unique workout_id
        workouts = [
            {"_id": ObjectId(), "workout_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "workout_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "workout_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "workout_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "workout_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
