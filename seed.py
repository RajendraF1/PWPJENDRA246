from app import create_app, db
from app.models import User

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        users = [
            User(username="Ivan", role="user", email="ivanpriyatama@gmail.com"),
            User(username="Haikal", role="user", email="haikalandito15@gmail.com"),
            User(username="Bilal", role="user", email="bilalramdhan7@gmail.com"),
            User(username="Romo", role="user", email="romogymnastyar01@gmail.com")
        ]
        for user in users:
            user.set_password("password")
        db.session.bulk_save_objects(users)
        db.session.commit()
        print("Berhasil Bolo")

if __name__ == "__main__":
    seed_data()