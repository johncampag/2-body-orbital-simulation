# Orbital Simulation - 2 Body (Earth + Satellite)
# Simulates gravitational orbit using Euler's method
# Physics: Newton's Law of Gravitation F = G(m1*m2)/r^2
# Author: Johnny Campagna

import numpy as np                              # numerical computing library
import matplotlib.pyplot as plt                 # plotting library
from matplotlib.animation import FuncAnimation  # animation tool from matplotlib

# --- House Keeping ---
import os
os.system('cls')                                # clears terminal before each run

# --- Constants ---
G = 6.674e-11       # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24        # Mass of Earth (kg)
dt = 10             # Time step - how many seconds pass each iteration (s)

# --- Initial Conditions ---
r = 7.0e6                        # Orbital radius from Earth's center (m) — just above atmosphere
pos = np.array([r, 0.0])         # Starting position vector of satellite [x, y] in meters
v_circ = np.sqrt(G * M / r)     # Circular orbit velocity derived from F_gravity = F_centripetal (m/s)
vel = np.array([0.0, v_circ])   # Starting velocity vector [x, y] — perpendicular to position for circular orbit

# --- Storage ---
x_vals = []     # stores x position of satellite each time step for static plot
y_vals = []     # stores y position of satellite each time step for static plot

# --- Update Loop ---
# runs 100,000 iterations to simulate full orbit, storing position each step
for i in range(100000):
    distance = np.linalg.norm(pos)              # magnitude of position vector = distance from Earth (m)
    direction = -pos / distance                  # unit vector pointing from satellite toward Earth (negative = inward)
    acceleration = (G * M / distance**2) * direction   # gravitational acceleration vector (m/s^2) using F=GMm/r^2, mass cancels
    vel = vel + acceleration * dt               # Euler's method: update velocity using acceleration
    pos = pos + vel * dt                        # Euler's method: update position using velocity
    x_vals.append(pos[0])                       # store x position
    y_vals.append(pos[1])                       # store y position

# --- Static Plot ---
# plots the full precomputed orbit path on a black background
fig_static, ax_static = plt.subplots(figsize=(8, 8))
fig_static.patch.set_facecolor('black')         # outer figure background
ax_static.set_facecolor('black')                # plot area background
ax_static.plot(x_vals, y_vals, color='cyan', label='Orbit Path')           # full orbit path
ax_static.plot(0, 0, 'bo', markersize=20, label='Earth')                   # Earth at origin
ax_static.plot(x_vals[0], y_vals[0], 'r*', markersize=15, label='Satellite Start')  # starting position
ax_static.set_aspect('equal')                   # equal axis scaling so orbit looks circular not elliptical
ax_static.legend(facecolor='black', labelcolor='white', loc='upper right')
ax_static.set_title('Orbital Simulation', color='white')
ax_static.set_xlabel('x position (m)', color='white')
ax_static.set_ylabel('y position (m)', color='white')
ax_static.tick_params(colors='white')           # white tick marks to match black background
ax_static.grid(True, color='gray', linestyle='--', alpha=0.3)  #  grid 
fig_static.tight_layout()                       # prevents text from overlapping
plt.show()

# --- Reset for Animation ---
# pos and vel are at end of loop, reset to initial conditions before animating
pos = np.array([r, 0.0])
vel = np.array([0.0, v_circ])

# --- Animation ---
# animates the satellite moving in real time using the same physics as the update loop
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')                # outer figure background
ax.set_facecolor('black')                       # plot area background
ax.set_xlim(-1.5e7, 1.5e7)                     # x axis limits in meters
ax.set_ylim(-1.5e7, 1.5e7)                     # y axis limits in meters
ax.set_aspect('equal')                          # equal scaling so orbit looks circular
ax.tick_params(colors='white')
ax.grid(True, color='gray', linestyle='--', alpha=0.3)

satellite, = ax.plot([], [], 'ro', markersize=8)    # satellite represented as a red dot
ax.plot(0, 0, 'bo', markersize=20)                  # Earth at origin as a blue dot

def update(frame):
    # called every frame by FuncAnimation — runs one physics step and moves satellite dot
    global pos, vel                                         # access variables defined outside function
    distance = np.linalg.norm(pos)                         # distance from Earth
    direction = -pos / distance                             # unit vector toward Earth
    acceleration = (G * M / distance**2) * direction       # gravitational acceleration vector
    vel = vel + acceleration * dt                           # update velocity
    pos = pos + vel * dt                                    # update position
    satellite.set_data([pos[0]], [pos[1]])                  # move satellite dot to new position
    return satellite,                                       # return updated object for blitting

# runs the animation — calls update() every 20ms for 100,000 frames
ani = FuncAnimation(fig, update, frames=100000, interval=20)
plt.show()