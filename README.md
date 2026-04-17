#  Pong Game – Python Turtle Edition

A classic **Pong arcade-style game** built using **Python Turtle Graphics** and **Object-Oriented Programming (OOP)** principles.

This project recreates the core mechanics of the original Pong experience including paddle control, ball physics, scoring logic, and collision detection inside a structured modular architecture.

---

##  Features

- Two-player paddle control
- Ball movement with velocity system
- Paddle collision detection
- Wall collision detection
- Dynamic ball speed increase after paddle hits
- Scoreboard tracking system
- Center dashed divider rendering
- Boundary-aware paddle movement
- Reset mechanics after scoring
- Clean OOP-based architecture

---

##  Project Structure

```
pong-game/
│
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
└── README.md
```

---

##  Concepts Used

This project demonstrates:

- Object-Oriented Programming
- Class inheritance (`Turtle`)
- Event listeners (`onkeypress`)
- Game loop architecture
- Collision detection logic
- Coordinate-based motion system
- State updates using frame refresh cycles
- Speed scaling mechanics

---

##  Controls

| Player | Move Up | Move Down |
|-------|---------|-----------|
| Right Paddle | ↑ Arrow | ↓ Arrow |
| Left Paddle | W | S |

---

##  How the Game Works

### Paddle System

Each paddle is implemented as a custom class extending Turtle:

- Moves vertically
- Stays within screen boundaries
- Responds to keyboard input

---

### Ball Physics Engine

The ball:

- Moves using velocity (`dx`, `dy`)
- Bounces off top and bottom walls
- Reflects on paddle collision
- Speeds up after paddle hits
- Resets position after scoring

---

### Collision Logic

Three types of collisions handled:

**Wall Collision**
```
Reverse vertical direction
```

**Paddle Collision**
```
Reverse horizontal direction
Increase speed slightly
```

**Miss Detection**
```
Award opponent a point
Reset ball position
```

---

### Scoreboard System

Tracks:

- Left player score
- Right player score

Updates dynamically after each point.

---

##  Run the Game

Execute:

```
python main.py
```

---

##  Future Improvements (Planned)

Possible upgrades:

- Sound effects on collision
- AI opponent mode
- Start / Pause screen
- Game-over condition
- Difficulty scaling
- Multiplayer score limit mode
- Ball spin mechanics

---

##  Learning Goals Achieved

This project helped practice:

- Structuring a game using OOP
- Managing object interaction
- Designing collision systems
- Building reusable class components
- Creating frame-based motion loops

---

##  Inspiration

Inspired by the original **1972 Atari Pong**, recreated using modern Python fundamentals.

---

##  Tech Stack

Python (Intermediate Level)
