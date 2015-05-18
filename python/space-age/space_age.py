class SpaceAge(object):
	def __init__(self, seconds):
		self.seconds = seconds
		self.earth_year = 31557600
	def on_earth(self):
		return round(self.seconds / self.earth_year, 2)
	def on_mercury(self):
		mercury_year = self.earth_year * 0.2408467
		return round(self.seconds / mercury_year,2)
	def on_venus(self):
		venus_year = self.earth_year * 0.61519726
		return round(self.seconds / venus_year, 2)
	def on_mars(self):
		mars_year = self.earth_year * 1.8808158
		return round(self.seconds / mars_year, 2)
	def on_jupiter(self):
		jupiter_year = self.earth_year * 11.862615
		return round(self.seconds / jupiter_year, 2)
	def on_saturn(self):
		saturn_year = self.earth_year * 29.447498
		return round(self.seconds / saturn_year,2)
	def on_uranus(self):
		uranus_year = self.earth_year * 84.01682615
		return round(self.seconds / uranus_year,2)
	def on_neptune(self):
		neptune_year = self.earth_year * 164.79132
		return round(self.seconds / neptune_year,2)

		
