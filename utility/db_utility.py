

def save_to_database(db, image_to_save):
    db.session.add(image_to_save)
    db.session.commit()