from webapp import create_app
from webapp.model import db, electro

app = create_app()

with app.app_context():
    new_record = electro(t1=7382, t2=3791, tarif1=6.8, tarif2=2.61, date='12/20', summ=10529)
    # new_record1 = electro(t1=1368, t2=616, tarif1=6.65, tarif2=2.51, date='05/20', summ=6711)
    # new_record2 = electro(t1=2250, t2=1087, tarif1=6.65, tarif2=2.51, date='06/20', summ=7047)
    # new_record3 = electro(t1=2833, t2=1332, tarif1=6.65, tarif2=2.51, date='07/20', summ=4491)
    # new_record4 = electro(t1=3339, t2=1613, tarif1=6.8, tarif2=2.61, date='08/20', summ=4174)
    # new_record5 = electro(t1=3635, t2=1826, tarif1=6.8, tarif2=2.61, date='09/20', summ=2568)
    # new_record6 = electro(t1=4337, t2=2215, tarif1=6.8, tarif2=2.61, date='10/20', summ=5689)




    db.session.add(new_record)
    # db.session.add(new_record1)
    #
    # db.session.add(new_record2)
    #
    # db.session.add(new_record3)
    #
    # db.session.add(new_record4)
    #
    # db.session.add(new_record5)
    # db.session.add(new_record6)


    db.session.commit()