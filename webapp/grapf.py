import matplotlib.pyplot as plt
import mpld3
import pandas as pd


def get_grapf(all_data):

    rub_data = {}
    kB_data = {}

    for item in all_data:

        rub_data[item.date] = item.summ
        kB_data[item.date] = item.t1 + item.t2


    fig = plt.figure(figsize=(14, 10))

    x1 = plt.subplot(321)
    x1.title.set_text('Расход в кВ')
    kB_plot = pd.Series(kB_data)
    kB_plot.plot()


    x2 = plt.subplot(322)
    x2.title.set_text('Расход в рублях')
    rub_plot = pd.Series(rub_data)
    rub_plot.plot()

    # fig.savefig('webapp/static/img/stat.png')

    fig_html = mpld3.fig_to_html(fig)

    return fig_html
