from matplotlib import pyplot as plt

list_x = []
list_y = []


def plot_method(args):
    length = len(args)
    for key in args:
        temp_arr = args[key].split(' ')
        list_x.append(temp_arr[0])
        list_y.append(float(temp_arr[1]))
    plt.rcParams['figure.figsize'] = (15.0, 10.0)
    plt.plot(list_x, list_y)
    plt.xlim(0, length)
    plt.xticks(range(0, length, 2))
    plt.xticks(rotation=45)
    plt.show()

