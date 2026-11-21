#the goal of this code is to simulate the movement of a robot and updating its position every second till it reaches 20m

in_pos = int(input("Enter the initial position of the robot in meters: "))
velocity = int(input("what is the velocity of the robot : "))
time = 0
time_rn = int(input("for how much time will the simulation going to be running : "))

for i in range(time_rn):
    in_pos = in_pos + velocity
    time=time+1
    print("the posistion of the robot after: ",time,"s is", in_pos,"m")
    if (in_pos == 20):
        print("the robot successfully travelled 20m")
        print("SIMULATION DONE :) !!")
        break

#my next step is to actually graph this code like showing the "robot" moving