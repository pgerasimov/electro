from webapp import create_app
from webapp.model import db, electro

app = create_app()

with app.app_context():
    new_record = electro(t1=1000, t2=1100, tarif1=6.65, tarif2=2.51, date='07/20', summ=40000)

    db.session.add(new_record)
    db.session.commit()