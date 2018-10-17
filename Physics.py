#PROJECT: Physics

#Global variables
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#takes a temperature in Fahrenheit and converts it to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
#test function f_to_c with value of 100
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#takes a temperature in Celsius and converts it to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
#test function c_to_f with value of 0
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#takes mass and acceleration and calculates force
def get_force(mass, acceleration):
	return mass*acceleration
#test function get_force
train_force = get_force(train_mass, train_acceleration)
#displaying train_force
print("The GE train supplies " +str(train_force)+ " Newtons of force.")

#takes mass and a constant to calculate energy
def get_energy(mass, c=3*10**8):
  return mass * c
#test function get_energy
bomb_energy = get_energy(bomb_mass)
#displaying bomb energy
print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

#takes mass, acceleration, and distance to calculate work
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work
#test function get_work
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")