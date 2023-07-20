import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Read data from the text file
def read_data_from_file(file_path):
    timestamps = []
    temperatures_a = []
    temperatures_b = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            timestamp = values[0]
            temperature_a = float(values[1])
            temperature_b = float(values[2])

            timestamps.append(timestamp)
            temperatures_a.append(temperature_a)
            temperatures_b.append(temperature_b)

    return timestamps, temperatures_a, temperatures_b

# Plot temperature vs. time
def plot_temperature_vs_time(timestamps, temperatures_a, temperatures_b):
    plt.plot(timestamps, temperatures_a, label='Temperature A')
    plt.plot(timestamps, temperatures_b, label='Temperature B')
    plt.xlabel('Time')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature vs. Time')

    # Set x-axis locator to show 10 ticks
    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(nbins=12))

    # Format x-axis ticks as dates
    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.show()

# Main program
file_path = '/Users/larryli/Desktop/Physics/Madhukar/tempData/temperature_data_20230720_132933.txt'  # Replace with your file path

timestamps, temperatures_a, temperatures_b = read_data_from_file(file_path)
plot_temperature_vs_time(timestamps, temperatures_a, temperatures_b)
