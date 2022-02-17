from robomaster import robot
import time

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    ## Write your code here
    '''
    x=x-axis movement distance,(meters) [-5,5]
    y=y-axis movement distance, (meters) [-5,5]
    xy speed = xy axis movement speed,(unit meter/seconds) [0,5,2]
    '''
    ep_chassis.move(x=3,y=0,z=0,xy_speed=0.75).wait_for_completed()
    ep_chassis.move(x=0,y=0,z=45,xy_speed=0.25).wait_for_completed()
    ep_chassis.move(x=0,y=0.25,z=0,xy_speed=0.75).wait_for_completed()
    ep_chassis.move(x=3,y=0,z=0,xy_speed=0.75).wait_for_completed()

    ep_chassis.drive_speed(x=0.4,y=0,z=-20)
    time.sleep(12) 
    ep_chassis.move(x=2,y=0,z=0,xy_speed=0.75).wait_for_completed() 
    ep_chassis.drive_speed(x=0.4,y=0,z=-20)
    time.sleep(10) 
    ep_chassis.move(x=2,y=0,z=0,xy_speed=0.75).wait_for_completed() 
    
    ep_robot.close()