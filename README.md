# Differential-Drive Robot Kinematics Simulator

This project implements a Python-based kinematics simulator for a differential-drive mobile robot. The simulator converts left and right wheel velocity inputs into body-frame motion and propagates robot pose over time using first-order Euler integration.

## Features
- Differential-drive kinematic modeling
- Wheel-to-body velocity mapping
- Euler integration of robot pose
- Simulation of straight-line and constant-curvature motion
- Modular structure separating inputs, model, and simulation logic

## Project Structure
- `configs.py` — simulation parameters and initial conditions  
- `inputs.py` — wheel velocity input profiles  
- `model.py` — kinematic equations and Euler integration  
- `simulation.py` — time-stepping loop and state storage  

## Validation
The simulator was validated against analytical expectations:
- Straight-line motion results in linear position growth and constant heading
- Turning motion produces sinusoidal Cartesian components and linear angular growth

## Future Work
- Higher-order integration methods (RK4)
- Closed-loop control (go-to-goal)
- Noise and slip modeling
- Trajectory tracking

## Usage
Run `simulation.py` to execute the simulation and visualize results.
