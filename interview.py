# Traffic light abstraction in Python3
# Kendall Jackson, Winter Park FL, 12/04/2018
def traffic_light(color):
    x = color

    # If statements handling all 3 possible cases, changes from G -> Y -> R
    if(x == "green"):
        x = "yellow"
        print("Light changed to: {}\n--------------".format(x))

    if(x == "yellow"):
        x = "red"
        print("Light changed to: {}\n--------------".format(x))

    else:
        x = "green"
        print("Light changed to: {}\n--------------".format(x))

# Must be lowercase
traffic_light(input("Please type 'green', 'red', or 'yellow' to see the traffic light cycle through: \n"))
