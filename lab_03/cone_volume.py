"""
WRITE YOUR FUNCTION DEFINITION BELOW
"""



"""
WRITE YOUR FUNCTION DEFINITION ABOVE
"""
def print_cone_volume():
    radius = 3
    height = 4.5
    pi = 3.1415
    if radius < 0 or height < 0:
        print("The values of the radius and the height must be positive.")
    else:
        volume= pi*radius**2*(height/3)
        print(volume)



def main():
    """
    Just some sample behavior.
    """
    print_cone_volume()




### DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
