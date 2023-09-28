




from app import app
from models import db, Bird  

db.init_app(app)


with app.app_context():
    print('Deleting existing birds...')
    Bird.query.delete()  

    print('Creating bird objects...')
    
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

    print('Adding bird objects to the transaction...')
    db.session.add_all([chickadee, grackle, starling, dove]) 
    print('Committing the transaction...')
    db.session.commit()  

    print('Seeding complete.')

if __name__ == '__main__':
    app.run()
