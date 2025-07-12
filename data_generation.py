# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Creating Numbers List
numbers = list(range(500))
cube_numbers = [i**3 for i in numbers]

# Plot the Lits
#plt.style.use('seaborn') => didn't work. sns used instead.
fig, ax = plt.subplots()
ax.plot(numbers, cube_numbers,color = 'red', linewidth = 1)
ax.scatter(numbers, cube_numbers,c= cube_numbers, cmap = plt.cm.Reds, s = 20)

# Set Chart Title and Labels
ax.set_title('cubic values', fontsize = 14)
ax.set_xlabel('value', fontsize = 10)
ax.set_ylabel('cube value', fontsize = 10)

# Set Axis Settings
ax.tick_params(labelsize = 8)
#ax.axis([0,6,0,70])
ax.ticklabel_format(style = 'scientific')

plt.show()

