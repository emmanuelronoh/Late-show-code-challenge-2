import csv
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  
from models import db, Episode, Guest, Appearance

def seed_data():
    with open('seed.csv', mode='r') as file: 
        reader = csv.DictReader(file)
        guests_dict = {}

        for row in reader:
            year = row['YEAR'].strip()
            occupation = row['GoogleKnowlege_Occupation'].strip()  # Corrected column name
            appearance_date = row['Raw_Guest_List'].strip()
            guest_name = row['Raw_Guest_List'].strip()

            episode = Episode.query.filter_by(date=appearance_date).first()
            if not episode:
                episode = Episode(date=appearance_date, number=int(year))
                db.session.add(episode)

            if guest_name not in guests_dict:
                guest = Guest(name=guest_name, occupation=occupation)
                db.session.add(guest)
                guests_dict[guest_name] = guest
            else:
                guest = guests_dict[guest_name]

            appearance = Appearance(rating=5, episode=episode, guest=guest)
            db.session.add(appearance)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
        seed_data()
