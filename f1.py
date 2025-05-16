import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 100
interval = 1000  # milliseconds

# Initialize lists for data
time = []
temperature = []
tire_pressure = []
overtaking_events = []
speed = []

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

def generate_data():
    # Simulate data
    temp = np.random.uniform(30, 40)
    pressure = np.random.uniform(1.8, 2.5)
    overtake = np.random.randint(0, 2)
    spd = np.random.uniform(150, 250)
    return temp, pressure, overtake, spd

def update(frame):
    # Update data
    temp, pressure, overtake, spd = generate_data()
    time.append(frame)
    temperature.append(temp)
    tire_pressure.append(pressure)
    overtaking_events.append(overtake)
    speed.append(spd)
    
    # Limit the length of data lists
    if len(time) > num_points:
        time.pop(0)
        temperature.pop(0)
        tire_pressure.pop(0)
        overtaking_events.pop(0)
        speed.pop(0)
    
    # Clear and update the plots
    ax1.clear()
    ax2.clear()
    
    # Plot Temperature and Tire Pressure
    ax1.plot(time, temperature, label='Temperature (°C)', color='red')
    ax1.plot(time, tire_pressure, label='Tire Pressure (bar)', color='blue')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature / Pressure')
    ax1.legend(loc='upper left')
    
    # Plot Speed and Overtaking Events
    ax2.plot(time, speed, label='Speed (km/h)', color='green')
    ax2.plot(time, np.array(overtaking_events)*max(speed), label='Overtaking Events', color='purple', linestyle='--')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Speed / Overtaking')
    ax2.legend(loc='upper left')

# Animation
ani = FuncAnimation(fig, update, interval=interval)

# Show the plot
plt.tight_layout()
plt.show()
