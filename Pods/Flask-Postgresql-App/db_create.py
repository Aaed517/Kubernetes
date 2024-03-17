from app import User, db, app


with app.app_context():
    db.create_all()
    db.session.commit()

def add_default_user(*args, **kwargs):
    with app.app_context():
        db.session.add(User(id=1,name="Mustafa Onur", surname="Çiçekalan"))
        db.session.commit()

add_default_user()