# import required libraries
import matplotlib.pyplot as plt
from randomwalk_module import RandomWalk
while True:
    # make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # plot the random walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (16,9))
    point_numbers = range(rw.num_points)
    #ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Greens, edgecolors = 'none', s= 10)
    ax.plot(rw.x_values, rw.y_values, color = 'green', linewidth = 1)
    
    # remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # plot start and end points
    ax.scatter(0,0, color = 'blue', edgecolors= 'none', s = 100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], color = 'red', edgecolors= 'none', s = 100)


    # axis settings
    ax.set_aspect('equal')
    plt.show()
    
    #exiting the program
    keep_running = input('another one? (y/n): ')
    if keep_running == 'n':
        break