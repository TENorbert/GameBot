# GameBot
A game bot using OpenAI gym and Reinforcement Learning

## Overview

This code is inspired by Siraj Raval's video on [creating a Game Bot](https://www.youtube.com/watch?v=XI-I9i_GzIw). <br/>
It uses Reinforcement learning to determine 2 things, whethrer to turn or not and which direction to turn in. <br/>
the Bot starts off with no knowledge of the game and you can see it get better as it learns and understands how the game works.

## Universe
Install [Universe](https://github.com/openai/universe) 

## Usage
It requires docker so you need to run it in sudo for the first time or it will not pull the OpenAI repositories.
Run using 
```{python}
sudo python game.py
```
For more details of code, check the source file.
