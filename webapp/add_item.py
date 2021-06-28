from webapp import create_app
from webapp.model import db, electro

app = create_app()

with app.app_context():
    new_record = electro(t1=524, t2=178, tarif1=6.65, tarif2=2.51, date='04/2020', summ=2417)
    new_record1 = electro(t1=1368, t2=616, tarif1=6.65, tarif2=2.51, date='05/2020', summ=6711)
    new_record2 = electro(t1=2250, t2=1087, tarif1=6.65, tarif2=2.51, date='06/2020', summ=7047)
    new_record3 = electro(t1=2833, t2=1332, tarif1=6.65, tarif2=2.51, date='07/2020', summ=4491)
    new_record4 = electro(t1=3339, t2=1613, tarif1=6.8, tarif2=2.61, date='08/2020', summ=4174)
    new_record5 = electro(t1=3635, t2=1826, tarif1=6.8, tarif2=2.61, date='09/2020', summ=2568)
    new_record6 = electro(t1=4337, t2=2215, tarif1=6.8, tarif2=2.61, date='10/2020', summ=5689)
    new_record7 = electro(t1=6080, t2=3149, tarif1=6.8, tarif2=2.61, date='11/2020', summ=14290)
    new_record8 = electro(t1=7382, t2=3791, tarif1=6.8, tarif2=2.61, date='12/2020', summ=10529)
    new_record9 = electro(t1=9926, t2=5103, tarif1=6.8, tarif2=2.61, date='01/2021', summ=21035)
    new_record10 = electro(t1=11334, t2=5798, tarif1=6.8, tarif2=2.61, date='02/2021', summ=11390)
    new_record11 = electro(t1=12783, t2=6552, tarif1=6.8, tarif2=2.61, date='03/2021', summ=11821)
    new_record12 = electro(t1=13621, t2=7063, tarif1=6.8, tarif2=2.61, date='04/2021', summ=7032)
    new_record13 = electro(t1=14665, t2=7650, tarif1=6.8, tarif2=2.61, date='05/2021', summ=8631)
    new_record14 = electro(t1=15209, t2=7946, tarif1=6.8, tarif2=2.61, date='06/2021', summ=4472)

    db.session.add(new_record)
    db.session.add(new_record1)
    db.session.add(new_record2)
    db.session.add(new_record3)
    db.session.add(new_record4)
    db.session.add(new_record5)
    db.session.add(new_record6)
    db.session.add(new_record7)
    db.session.add(new_record8)
    db.session.add(new_record9)
    db.session.add(new_record10)
    db.session.add(new_record11)

    db.session.commit()