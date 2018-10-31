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

#FINDING THE BEST PLACES TO GO BASED ON INTEREST
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    #print("length of attractions_in_city: " + str(len(attractions_in_city)))
    attractions_with_interest = []
    for possible_attraction in range(len(attractions_in_city)):
        attraction = attractions_in_city[possible_attraction]
        attraction_tags = attractions_in_city[possible_attraction][1]
        #print("Stored in attraction_tags at index " +str(possible_attraction)+": " + str(attraction_tags))
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(attraction[0])
    return attractions_with_interest
#testing function find_attractions
la_arts = find_attractions("Los Angeles, USA", ['art','beach'])
#print("Based on your interest(s), I recommend: "+ str(la_arts))

#SEE THE PARTS OF A CITY YOU WANT TO SEE
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " +traveler_destination+ ":\n"

    for places_to_go in traveler_attractions:
        interests_string += "-" + places_to_go +"\n"
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument', 'art']])
print(smills_france)
