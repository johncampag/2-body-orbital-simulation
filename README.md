# Orbital Simulation 🛰️

A 2-body orbital mechanics simulator built in Python. Simulates a satellite orbiting Earth using real physics and numerical integration, then visualizes it as both a static plot and a real-time animation.

Built as a personal project to apply physics and math concepts from my freshman year of Mechanical Engineering at Clemson University.

---

## How It Works

The simulation is driven by Newton's Law of Gravitation:

**F = G(m₁m₂) / r²**

Since the satellite's mass cancels out, the gravitational acceleration at any point is:

**a = GM / r²**

This acceleration vector always points toward Earth. Every time step, the simulation uses **Euler's method** to update the satellite's velocity and position:

    vel = vel + acceleration × dt
    pos = pos + vel × dt

Run this 100,000 times with a 10 second time step and you get a full orbital simulation. The initial orbital velocity is calculated by setting gravitational force equal to centripetal force:

**v = √(GM/r)**

This ensures a perfectly circular orbit at the given radius.

---

## How To Run It

1. Make sure you have Python installed
2. Install dependencies by running: pip install numpy matplotlib
3. Run the simulation: python orbital_sim.py

The static plot will appear first — close it to launch the animation.

---

## Dependencies

- Python 3.x
- NumPy
- Matplotlib

---

## Project Structure

- **Constants** — gravitational constant, Earth's mass, time step
- **Initial Conditions** — orbital radius, starting position and velocity vectors
- **Physics Engine** — Euler's method update loop running 100,000 iterations
- **Static Plot** — full precomputed orbit path visualized on a black background
- **Animation** — real-time satellite movement using matplotlib FuncAnimation

---

## Future Improvements

- Elliptical orbits by adjusting initial velocity
- User input for orbital radius and velocity
- Multiple satellites
- Upgrade from Euler's method to RK4 for higher accuracy
- Add orbital period and velocity readouts

---

## Author

Johnny Campagna — Mechanical Engineering, Clemson University  
