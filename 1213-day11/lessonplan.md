# Day 11: Final Class - Games, Physics & Trivia

## Class Overview (2.5 hours)

| Time | Topic | File |
|------|-------|------|
| 1 hour | Game Development with Pygame | `game_dev.ipynb` |
| 1 hour | Physics Simulations | `physics_simulation.ipynb` |
| 30 min | Course Trivia | `trivia.txt` |

---

## Part 1: Game Development with Pygame (1 hour)

### Topics Covered
- Installing and importing Pygame
- The game loop (events → update → draw)
- Screen coordinates (0,0 is top-left)
- Drawing shapes (rectangles, circles)
- Handling keyboard input
- Collision detection
- Game state management (score, game over)

### Games Created
1. **first_window.py** - Basic window with shapes
2. **moving_player.py** - Keyboard-controlled player
3. **coin_collector.py** - Collect coins with collision detection
4. **dodge_game.py** - Complete game with enemies, score, and game over

### Key Concepts
```python
pygame.init()                              # Initialize
screen = pygame.display.set_mode((W, H))   # Create window
pygame.draw.rect(screen, color, rect)      # Draw rectangle
keys = pygame.key.get_pressed()            # Get input
clock.tick(60)                             # Control FPS
```

---

## Part 2: Physics Simulations (1 hour)

### Topics Covered
- Projectile motion equations
- Bouncing ball simulation (coefficient of restitution)
- Pendulum motion (solving differential equations)
- Orbital mechanics (gravity simulation)
- Spring oscillator (Hooke's Law)
- Effect of air resistance

### Key Libraries
- **NumPy** - Numerical calculations
- **Matplotlib** - Visualization
- **SciPy** - Solving differential equations with `odeint`

### Physics Formulas Used
| Topic | Formula |
|-------|---------|
| Projectile | x = v₀cos(θ)t, y = v₀sin(θ)t - ½gt² |
| Pendulum | T = 2π√(L/g) |
| Spring | F = -kx, T = 2π√(m/k) |
| Gravity | F = Gm₁m₂/r² |

---

## Part 3: Course Trivia (30 minutes)

### Format
- 20 questions covering all 10 previous days
- Split into 6 rounds:
  1. Basics (Q1-5)
  2. Control Flow (Q6-10)
  3. Data Structures (Q11-14)
  4. Classes & OOP (Q15-16)
  5. Algorithms (Q17-18)
  6. Data Science (Q19-20)
- 5 bonus questions for tiebreakers

### Scoring
- Regular questions: 10 points
- Bonus questions: 15 points
- Maximum score: 275 points

---

## Course Summary

Over this semester, students learned:

1. **Day 1**: Variables, types, input/output, operators
2. **Day 2**: Conditionals, loops, functions
3. **Day 3**: Lists, tuples, sets, dictionaries
4. **Day 4**: Strings, classes, recursion
5. **Day 5**: Searching, sorting, lambdas
6. **Day 6**: NumPy, Pandas basics
7. **Day 7**: Machine learning fundamentals
8. **Day 8**: Data science in practice
9. **Day 9**: Web development with Flask
10. **Day 10**: File I/O, stock analysis project
11. **Day 11**: Game dev, physics simulations, wrap-up

🎉 **Congratulations on completing Intro to Python!**

