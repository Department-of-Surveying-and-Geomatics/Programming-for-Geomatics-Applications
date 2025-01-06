import matplotlib.pyplot as plt

def plot_data():

    #open the coordinate file specifing the path of the file

    my_file = open('C:/Users/user/Desktop/x_y_coordinates.txt','r')

    #create two empty lists one for x coordinates and one for y coordinates

    x_coords = []
    y_coords = []
    my_file.readline()

    #split the columns and loop

    for line in my_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))

    #generate the scatterplot using the float converted coordinates

    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Coordinates ScatterPlot')
    plt.grid(True)
    plt.show()

plot_data()