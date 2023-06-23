# Evolutionary Games

In this project, a simple 2D minigame has been implemented. The agent needs to learn to maneuver using a neural network combined with an evolutionary algorithm. In this project, an Artificial Neural Network (ANN) was trained through the evolutionary algorithm to enable it to play the game flawlessly.

## Game Modes
Helicopter             |  Gravity          |  Thrust
:-------------------------:|:-------------------------:|:-------------------------:
![Helicopter](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/helicopter.png?raw=true)  |  ![Gravity](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/gravity.png?raw=true) | ![Thrust](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/thrust.png?raw=true)

## Project Parts

1. Neural network implementation (nn.py file)
2. Implementation of architecture and how to use neural network (player.py file)
3. Implementation of survivor selection (evolution.py file)
4. Implementation of parent selection and generating the new generation (evolution.py file)
5. Implementation of mutation (evolution.py file)

## Playing with it

1. Helicopter
   - `python game.py --mode helicopter --play True`
2. Gravity
   - `python game.py --mode gravity --play True`
3. Thrust
   - `python game.py --mode thrust --play True`

## Contributors
- [Hossein Zaredar](https://github.com/HosseinZaredar)
- [Matin Tavakoli](https://github.com/MatinTavakoli/) <br>
- Many thanks to [Parnian Rad](https://github.com/Parnian-Rad)

My Partner for this Project: Maryam Shafiei
