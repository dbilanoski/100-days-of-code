'''
 # CHALLENGE: Probability Calculator

 # DESCRIPTION
 
 Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

    hat: A hat object containing balls that should be copied inside the function.
    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The experiment function should return a probability.

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform N experiments, count how many times M we get at least 2 red balls and 1 green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

Since this is based on random draws, the probability will be slightly different each time the code is run.

Hint: Consider using the modules that are already imported at the top of prob_calculator.py. Do not initialize random seed within prob_calculator.py.

'''
import copy
import random

class Hat():
  def __init__(self, **kwargs):
    self.contents = []
    
    for key in kwargs.keys():
       for value in range(kwargs[key]):
         self.contents.append(key)

  def draw(self, num_of_balls):
    # If number of balls to draw from the hat is bigger than the hat, return the hat
    if int(num_of_balls) > len(self.contents):
      return self.contents
    hat = []
    for num in range(num_of_balls):
      hat.append(self.contents.pop(random.randrange(len(self.contents))))
    return hat

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # Expectance met counter
  m = 0
  
  for num in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)

    # Convert expected balls dict to a list
    balls_expected = list()
    for key in expected_balls.keys():
      for value in range(expected_balls[key]):
        balls_expected.append(key)

    # Current ball matched counter
    counter = 0

    for ball in balls_expected:
      # If the current expected ball is in the balls_drawn, add 1 to counter and remove that ball from balls_drawn
      if ball in balls_drawn:
        counter +=1
        balls_drawn.remove(ball)

    # If same numner of balls in counted as match as tgere are balls in the balls_expected, add to global counter
    if counter == len(balls_expected):
      m += 1
  
  return(m/num_experiments)



hat3 = Hat(red=5, orange=4, green=1, blue=0, pink=2, striped=9)


print(experiment(hat=hat3,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=1000))
