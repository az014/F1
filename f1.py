import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure for plotting
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

# Set up plot limits
ax.set_xlim(0, 100)  # x-axis will show the last 100 points
ax.set_ylim(0, 100)  # y-axis range for random values

# Function to update the graph
def update(frame):
    # Add new data point (incremental x and random y)
    x_data.append(len(x_data))  # x-axis increments by 1 each frame
    y_data.append(random.randint(0, 100))  # random y-axis value between 0 and 100

    # Keep only the last 100 points in the graph
    if len(x_data) > 100:
        x_data.pop(0)
        y_data.pop(0)
    
    # Update the line data
    line.set_data(x_data, y_data)
    
    return line,

# Animate the plot, updating every 100ms (10 frames per second)
ani = animation.FuncAnimation(fig, update, interval=100)

# Show the plot
plt.title('Real-Time Data Simulation')
plt.xlabel('Time (frames)')
plt.ylabel('Random Value')
plt.show()
