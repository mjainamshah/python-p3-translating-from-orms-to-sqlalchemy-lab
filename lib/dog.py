from models import Dog

def create_table(base, engine): 
    base.metadata.create_all(engine) 
    # contains function "create_table()" that takes a declarative_base and creates a SQLite database.
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    # contains function "save()" that takes a Dog instance as an argument and saves the dog to the database.
    pass

def get_all(session):
    return session.query(Dog).all()
    # contains function "get_all()" that takes a session and returns a list of Dog instances for every record in the database.
    pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    # contains function "find_by_name()" that takes a session and name and returns a Dog instance corresponding to its database record retrieved by name.
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    # contains function "find_by_id()" that takes a session and id and returns a Dog instance corresponding to its database record retrieved by id.
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    # contains function "find_by_name_and_breed()" that takes a session, a name, and a breed as arguments and returns a Dog instance matching that record.
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    # contains function "update_breed()" that takes a session instance, and breed as arguments and updates the instance's breed.
    pass