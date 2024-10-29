def format_itineraries(itineraries):
    formatted_string = ""
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_string += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_string.strip() 
