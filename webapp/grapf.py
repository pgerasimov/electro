import matplotlib.pyplot as plt
import mpld3
import pandas as pd

from webapp.weather import temp_map


def get_grapf(all_data):
    rub_data = []
    kB_data = []

    for item in all_data:
        rub_data.append(item.summ)

    for i in range(len(all_data)):
        if i == 0:
            kB_data.append(all_data[i].t1 + all_data[i].t2)
        else:
            kB_data.append((all_data[i].t1 + all_data[i].t2) - (all_data[i-1].t1 + all_data[i-1].t2))

    print(rub_data)

    fig = plt.figure(figsize=(14, 10))

    plt.subplot(321)
    plt.title('Расход в кВ', fontsize=17)
    plt.plot(rub_data, color="blue", alpha=0.5)  # Полупрозрачная линия
    plt.plot(kB_data, color="#8B008B")  # RGB
    plt.plot(rub_data, kB_data)


    plt.subplot(322)
    plt.title('Расход в рублях', fontsize=17)
    rub_plot = pd.Series(rub_data)
    rub_plot.plot()

    plt.subplot(323)
    plt.title('Погода', fontsize=17)
    rub_plot = pd.Series(temp_map)
    rub_plot.plot()

    # fig.savefig('webapp/static/img/stat.png')

    fig_html = mpld3.fig_to_html(fig)


    return fig_html
