# Texas Hold'em Poker

This repository contains a Python implementation of Texas Hold'em, a popular poker variant. The project provides functionality to determine the winner(s) of a game.

## Features

- Hand evaluation: Determine the hand rankings and winners based on the players' cards.
- Rules enforcement: Implement the rules and betting rounds of Texas Hold'em.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdulrafey7047/Texas-Hold-em-Poker.git texas-holdem
   ```

2. Navigate to the project directory:

   ```bash
   cd texas-holdem
   ```

## Usage

- First you need to place your game's data in a json file in the same format as [sample_data.json](#).

- The following tables shows how the crads and suits must be represented for the `Game` class to determine the winner(s)

  | Number  | Representation |
  | :----   | :--- | 
  | `2`     | `2`  | 
  | `3`     | `3`  | 
  | `4`     | `4`  | 
  | `5`     | `5`  | 
  | `6`     | `6`  | 
  | `7`     | `7`  | 
  | `8`     | `8`  | 
  | `9`     | `9`  | 
  | `10`    | `T`  | 
  | `Jack`  | `J`  | 
  | `Queen` | `K`  | 
  | `King`  | `Q`  |
  | `Ace`   | `A`  | 


  | Suit       | Representation |
  | :--------  | :--- | 
  | `Hearts`   | `H`  | 
  | `Diamonds` | `D`  | 
  | `Clubs`    | `C`  | 
  | `Spades`   | `S`  | 

- Each card must be represented by a string of 2 charaters, first being the number representation and the second being the suit representation. The card `4 of Diamonds` should be represented as `4D`, `Ace of Spades` should be represented as `AS`.

- To find winner of a Texas Hold'em game, run the following command:

  ```bash
  python main.py <path_to/game_data_file.json>
  ```
  This would print the winner(s) of the game to the console.

- If you want to integrate this into your own project you can use the `Game` class for it via this conde snippet:

  ```
  from game import Game 

  game = Game.from_json('path_to/game_data_file.json')
  winners = game.find_winner()
  ```

## Sample Data

The repository includes a sample data file named `sample_data.json`, which contains example game data and player information.

## Contributing

Contributions to this project are welcome! If you would like to contribute, please fork the repository and submit a pull request. Ensure that you follow the repository's coding style and guidelines.

## License

This project is free for anyone to use or to implement in their own projects.

## Contact

For any inquiries or suggestions, please feel free to open an issue or contact me at [abdul.rafey7047@gmail.com](mailto:abdul.rafey7047@gmail.com).