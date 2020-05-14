import matplotlib.pyplot as plt

def get_grapf(all_data):


    month = []
    kB = []
    rub = []

    for item in all_data:
        month.append(item.date)
        kB.append(item.t1+item.t2)
        rub.append(item.summ)



    fig = plt.figure(figsize=(23, 5))

    plt.subplot(131)
    plt.plot(month, kB)

    plt.subplot(132)
    plt.plot(month, rub)


    fig.savefig('webapp/static/img/stat.png')
    plt.close()

    return 'ok'

