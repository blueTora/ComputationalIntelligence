from matplotlib import pyplot as plt
import csv

mode = input("Enter Mode: ")


def open_file(d_type):
    data = []
    with open(f'./plot_data/{d_type}_{mode}.csv', 'r') as file:
        f = csv.reader(file)

        for a in f:
            data.append(float(a[0]))

    return data


list_max = open_file('max')
list_avg = open_file('avg')
list_min = open_file('min')

plt.plot(list_max, 'red')
plt.plot(list_avg, 'magenta')
plt.plot(list_min, 'blue')
plt.legend(['max', 'average', 'min'])
plt.show()
