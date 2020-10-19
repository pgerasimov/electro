from webapp import create_app
from webapp.model import db, electro

app = create_app()

with app.app_context():
    new_record = electro(t1=524, t2=178, tarif1=6.65, tarif2=2.51, date='04/20', summ=2417)
    new_record1 = electro(t1=1368, t2=616, tarif1=6.65, tarif2=2.51, date='05/20', summ=6711)
    new_record2 = electro(t1=2250, t2=1087, tarif1=6.65, tarif2=2.51, date='06/20', summ=7047)
    new_record3 = electro(t1=2833, t2=1332, tarif1=6.65, tarif2=2.51, date='07/20', summ=4491)
    new_record4 = electro(t1=3339, t2=1613, tarif1=6.8, tarif2=2.61, date='08/20', summ=4174)
    new_record5 = electro(t1=3635, t2=1826, tarif1=6.8, tarif2=2.61, date='09/20', summ=2568)

    db.session.add(new_record)
    db.session.add(new_record1)

    db.session.add(new_record2)

    db.session.add(new_record3)

    db.session.add(new_record4)

    db.session.add(new_record5)

    db.session.commit()