import sys
sys.path.append('/home/vishal/.conda/envs/coding/lib/python3.5/site-packages')
#^ Uncomment this if gym is not in path

import gym
import universe
import random

def ifTurn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    '''
    Does the learning by reinforcement technique
    For every 15 epochs calculate the average of total observations
    if avg is less than 0, then the turn direction should be reversed
    if we get a reward for every iteration, then the direction could be right 
    '''
    
    if j>=15:
        turn = True if total_sum / j == 0.0 else False
        total_sum, j, prev_total_sum = 0, 0, total_sum
    else:
        turn = False
    if observation_n != None:
        # We have done something right so we have to give the reward
        total_sum += reward_n
        j += 1
    return(turn, j, total_sum, prev_total_sum)

def main():   
    n, j = 0, 0
    # ^ Iteration variables
    
    env = gym.make('flashgames.CoasterRacer-v0')
    env.configure(remotes = 1)
    # ^ Intitlaising the environment as Coaster racer from gym
    observation_n = env.reset()
    total_sum = 0
    prev_total_sum = 0
    # ^ Observations sum
    
    left = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
    right = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
    Forward = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]
    # ^ Defining the keyboard buttons to press during the actions
    
    event  = left

    turn = False
    # ^ Variable to flip the steering
    while True:
        # Main game loop
        n += 1
        
        if n > 1:
            # Game has run for at least one iteration, i.e. game isn't just starting
            # Check if it already turning to a side or not
            if observation_n[0] != None:
                prev_score = reward_n[0]
                
                if (turn):
                    # If we should turn, event decides where to turn
                    event = random.choice([left, right])
                    action_n = [event for _ in observation_n]
                    # ^ Perform the turn
                    turn = False
        elif turn == False:
            # Go without turning
            action_n = [Forward for _ in observation_n]
        
        if observation_n[0] != None:
            # if the game has already started check to see if turn is needed
            turn, j, total_sum, prev_total_sum = ifTurn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])
        
        observation_n, reward_n, done_n, info = env.step(action_n)
        # ^ perform the action and save the data for new iteration
        
        env.render()
        # ^ Render the environment


#RUN THE GAME!!!

if __name__ == "__main__":
    main()
