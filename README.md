# Asteroid video game

## Table of Contents

- [Installation](#installation)
- [Verify Installation](#verify)
- [Run](#run)

## Installation

To get started with this project, you'll need to clone the repository, navigate into the project directory and create a virtual environment at the top level of your project directory and install the pygame dependency. Run the following commands in your terminal:

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

## Verify

Make sure pygame is installed:

```
  python3 -m pygame
```

## Run

To run the game just run the main.py file from your project directory:

```
  python3 main.py
```

## Possible Improvements

- [ ] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped
