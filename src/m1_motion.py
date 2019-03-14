"""
An opportunity to explore how to make an EV3 Robot move.

Authors: Dave Fisher, David Mutchler, Vibha Alangar,
their colleagues, and Maddie Sorensen.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# Done: 2.
#   Follow along with the lecture to run this program:
#    - Using SSH from your computer
#   When you have successfully run this program, change this _TODO_ to DONE.
# -----------------------------------------------------------------------------

import simple_rosebotics as rb
import time



def main():
    """ Calls the other functions to test/demo them. """
    print("Running main on the robot.")
    robot=rb.RoseBot()
    #done: 2. Construct a RoseBot.  Send it as an argument to other functions.
    run_test_spin(robot)
    run_test_go(robot)
    challenge1(robot)
    challenge2(robot)


def run_test_spin(robot):
    """
    Tests the   spin   function, by making the robot spin several times,
    for different amounts of time and with different speeds,
    with   time.sleep(2)   between each run.
      :type robot:  rb.RoseBot
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this.
    # -------------------------------------------------------------------------
    spin(robot,2,50)

def spin(robot, seconds, speed):
    robot.drive_system.left_motor.turn_on(speed)
    robot.drive_system.right_motor.turn_on(-speed)
    time.sleep(seconds)
    robot.drive_system.left_motor.turn_off()
    robot.drive_system.right_motor.turn_off()

    """ :type robot: rb.RoseBot """
    # -------------------------------------------------------------------------
    # Done: 4.
    #   Makes the robot move, by using this pattern:
    #    1. Turn on the wheel motors at the given speed but with:
    #        -- LEFT wheel POSITIVE speed
    #        -- RIGHT wheel NEGATIVE speed
    #    2. time.sleep(seconds)  # Pause here, let other processes run
    #    3. Turn off the wheel motors.
    #
    # Use the DOT trick to figure out how to turn on and turn off motors.
    # -------------------------------------------------------------------------


def run_test_go(robot):
    """
    Tests the   go   function, by making the robot go several times,
    for different amounts of time and with different speeds,
    with   time.sleep(2)   between each run.
      :type robot:  rb.RoseBot
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this.
    # -------------------------------------------------------------------------
    go(robot, 5, 45,80)


def go(robot, seconds, left_wheel_speed, right_wheel_speed):
    """ :type robot: rb.RoseBot """
    robot.drive_system.left_motor.turn_on(left_wheel_speed)
    robot.drive_system.right_motor.turn_on(right_wheel_speed)
    time.sleep(seconds)
    robot.drive_system.right_motor.turn_off()
    robot.drive_system.left_motor.turn_off()
    # -------------------------------------------------------------------------
    # Done: 6.
    #   Make the robot go, by using the pattern from SPIN function, except
    #   using the given speeds for the left and right wheels, respectively.
    # -------------------------------------------------------------------------


def challenge1(robot):
    """ Your instructor will tell you this challenge. """


def challenge2(robot):
    """ Your instructor will tell you this challenge. """


main()
