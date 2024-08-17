# Snake Game

Welcome to the Snake Game project! 
This is a classic Snake game built using Python, as my final assignment for Python course in Code Academy. 
The game features a simple gameplay where you control a snake that grows in length as it eats food. 
The objective is to keep the snake alive by avoiding collisions with the walls and itself.
Coliding the snake head an fruit will "eat" it, and make your snake grow by one block. Eating an apple will adds 1 point to your final score, while eating a pineapple adds 2 points to the final score. 
In game text and instructions are in Serbian language. 
Game is split in main entry point and three game modules, as per project requirement. 

## Project Structure

The project is organized as follows:
```
python_snake_game/
│
├── glavni.py                  # Main entry point of the game
├── Materijali/                # Folder containing game icons
│   ├── ananas.png             # Pineapple image file
│   ├── ikonica.png            # Snake thumbnail image file
│   ├── jabuka.png             # Apple image file
│   └── kocka.jpg              # Square immage file used as snake body 
│── ekrani.py                  # First game module
│── igrica.py                  # Second game module
│── objekti.py                 # Third game module
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies 
```

### Files and Folders

- **`glavni.py`**: The main file that runs the game. This script imports functions and classes from the modules.
- **`Materijali/`**: Contains the icons used in the game, such as food or snake head icons.
- **`ekrani.py`**: Manages game screen and message display.
- **`igrica.py`**: Handles snake movement, input detection, checks for colision and snake movement.
- **`objekti.py`**: Contains instruction for food object display, snake object display and growth .

## Requirements

To run the Snake Game, you'll need Python installed on your machine. You can install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```
## How to run

1.	Clone this repository to your local machine:

  ```bash
  git clone https://github.com/najeden/python_snake_game.git
  ```

2.	Navigate to the project directory:

  ```bash
  cd python_snake_game
  ```

3. Run the game using Python

   ```bash
   python glavni.py
   ```

## Contributing
All contributions are more than welcome! If you find any bugs or have ideas to improve this game, feel free to open an issue or submit a pull request. 

## License
This project is released into the public domain under the [Unlicense](LICENSE). You are free to use, modify, and distribute this software without any restrictions. For more details, see the [LICENSE](https://unlicense.org/) file.
