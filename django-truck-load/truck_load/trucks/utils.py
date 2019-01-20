from math import sin, cos, sqrt, atan2, radians

def distance_between_coordinates(orig_lat, orig_lng, dest_lat, dest_lng):
	"""
		Calculates the approximate distance between two geographical coordinates using well known equations.
		There's a considerable error rate, but since it's only an approximation for performance reasons, there's no problem.
		
		Input:
			orig_lat: origin latitude. Ex: 36.876719
			orig_lng: origin longitude. Ex: -89.5878579
			dest_lat: destination latitude. Ex: 32.9342919
			dest_lng: destination longitude. Ex: -97.0780654	

		Returns the distance between the given coordinates in kilometers / km.
	"""

	# Checking if all the arguments were given.
	if not (orig_lat or orig_lng or dest_lat or dest_lng):
		raise Exception("All the following arguments should be given: orig_lat, orig_lng, dest_lat, dest_lng. At least one of them is missing.")

	# Approximate radius of earth in km
	R = 6373.0

	# Converting degrees to radians
	lat1 = radians(orig_lat)
	lng1 = radians(orig_lng)
	lat2 = radians(dest_lat)
	lng2 = radians(dest_lng)

	# Calculating the difference between latitudes (destination_latitude - origin_latitude) and longitudes (destination_longitude - origin_longitude).
	dlng = lng2 - lng1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c
	return distance