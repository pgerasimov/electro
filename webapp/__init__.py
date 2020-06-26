import datetime
from html import unescape
import matplotlib
from flask import Flask, render_template, flash
from webapp.forms import data
from webapp.grapf import get_grapf
from webapp.model import db, electro

matplotlib.use('Agg')


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    db.init_app(app)

    @app.route("/", methods=['GET', 'POST'])
    def index():
        form = data()
        all_data = electro.query.all()

        plot = get_grapf(all_data)

        total = 0
        for i in all_data:
            total += i.summ

        round(total)

        avarege = total / len(all_data)


        unescaped = unescape(plot)

        return render_template('base.html', active='index', form=form, data=all_data, total=total, plot=unescaped, avarege=avarege)

    @app.route('/get_data', methods=['POST'])
    def get_data():
        form = data()

        today = datetime.datetime.today().strftime("%m / %Y")
        today = today[0:-2]

        t1_tarif = 6.65
        t2_tarif = 2.51

        t1_data = int(form.T1.data)
        t2_data = int(form.T2.data)

        all_records = electro.query.all()
        last_record_id = str(all_records[-1].id)

        last_record_t1 = electro.query.filter_by(id=last_record_id)[0].t1
        last_record_t2 = electro.query.filter_by(id=last_record_id)[0].t2

        price = ((t1_data - last_record_t1) * t1_tarif) + ((t2_data - last_record_t2) * t2_tarif)
        round(price)

        new_record = electro(t1=t1_data, t2=t2_data, tarif1=t1_tarif, tarif2=t2_tarif, date=today, summ=price)

        db.session.add(new_record)

        db.session.commit()

        all_data = electro.query.all()

        total = 0
        for i in all_data:
            total += i.summ
        round(total)

        avarege = total / len(all_data)


        get_grapf(all_data)

        flash('Показания добавлены')

        return render_template('base.html', active='index', form=form, data=all_data, total=total, avarege=avarege)

    return app
