import math

class CalculateTime():

	def calTime(text):
		length = len(text.split())
		time = length/200
		minutes = math.floor(time)
		seconds = (time-minutes)*60
		seconds = math.ceil(seconds) if math.ceil(seconds)-seconds < 0.5 else math.floor(seconds)
		return str(minutes) + " minutes " + str(seconds) + " seconds "