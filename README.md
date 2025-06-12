# Baseball Simulation

A Python GUI baseball game simulator that uses player statistics and Monte Carlo methods to simulate at-bats and track game outcomes.

## Overview

This application presents a simple graphical baseball game powered by `tkinter`. It reads real player statistics, simulates swings based on on-base percentage (OBP), and tracks outs and runs through an interactive interface.

## Features

* **Graphical Interface**: Built with `tkinter` featuring a canvas for hit/strike messages and labels for displaying outs and runs.
* **Probabilistic Simulation**: Each swing is evaluated as a hit or strike by comparing a player's OBP against a random threshold.
* **Game Flow Control**: Start and Swing buttons manage game stages; the Swing button is disabled after 3 outs, and a “Game Over” message is shown.
* **Console Logging**: Current batter, on-deck batter, and previous batter details are printed to the console for insight.

## Requirements

* Python 3.6 or higher
* `tkinter` (included with most Python distributions)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/aniruddhan04/Baseball-Simulation.git
   cd Baseball-Simulation
   ```
2. **Ensure you have Python 3 installed**

## Usage

1. **Place** `player_statistics.txt` in the same directory as `BaseballSim.py`.
2. **Run** the simulator:

   ```bash
   python BaseballSim.py
   ```
3. **Click** **Start Game** to initialize.
4. **Click** **Swing** for each at-bat until you accumulate 3 outs.
5. **View** outs and runs on the window; a **Game Over** label appears when the game ends.

## File Structure

```
├── BaseballSim.py         # Main application script with GUI and simulation logic
├── player_statistics.txt  # Player stats: one line per player, 6 fields
└── README.md              # Project documentation
```

## Data File Format

Each line in `player_statistics.txt` must contain exactly six values separated by spaces:

```
Name AB Runs Hits RBIs OBP
```

* **Name**: Player’s name (no spaces)
* **AB**: At-bats (integer)
* **Runs**: Total runs scored (integer)
* **Hits**: Total hits (integer)
* **RBIs**: Runs batted in (integer)
* **OBP**: On-base percentage (float between 0 and 1)

Example:

```
Jose 566 30 2 30 0.351
```

## Contributing

Contributions are welcome! To propose changes:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes and push to your fork.
4. Open a pull request describing your updates.

## License

This project is open-source under the MIT License. See [LICENSE](LICENSE) for details.
