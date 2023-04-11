# Week One Practical

# Question one
def distance(velocity, time):
    distance_travelled = velocity * time
    return distance_travelled


def kinetic_energy(mass, velocity):
    kenegry = (0.5 * mass) * velocity * velocity
    return kenegry


# ask user to input mass in kilograms
user_input_mass = int(input('please enter mass in kilograms: '))

# ask user to input velocity in meters per second
user_input_velocity = int(input("please enter velocity in meters per second: "))

print(kinetic_energy(user_input_mass, user_input_velocity))
