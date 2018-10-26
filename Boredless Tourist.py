#SET UP
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#TRAVELLING TO FARAWAY LANDS
#to know where a traveller is, we need the index of destination
def get_destination_index(destination):
  #find the index of destination
  for x in range(len(destinations)):
    if destination == destinations[x]:
      destination_index = x
  return destination_index
#test get_destination_index
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Battambang, Cambodia"))

def get_traveler_location(traveler):
  #access traveler's destination string and save it
  traveler_destination = test_traveler[1]
  #retrieve index of the destination where the traveler is and save it
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#test get_traveler_location
#print(get_traveler_location('Erin Wilkes'))

#VISITING INTERESTING PLACES
#attractions to be an empty list for every destination in destinations
attractions = [[] for i in range(len(destinations))]
#test that list comprehension attractions is correct
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions

  except UnboundLocalError:
    return

#adding attractions
add_attraction("Los Angeles",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#FINDING THE BEST PLACES TO GO
