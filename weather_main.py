# weather_main.py

import urllib2
import json
import requests


class Weather():

	def __init__(self, location):
		self.location = location
		self.city = None
		self.state = None
		self.master_json = None
		self.get_weather()
		self.get_location()

	def get_weather(self):
		url = 'http://api.wunderground.com/api/1a6f295e825c2af1/geolookup/conditions/forecast10day/q/{}.json'.format(self.location)
		response = requests.get(url)
		response_json = response.json()
		self.master_json = response_json
		print(url)

	def get_location(self):
		self.city = self.master_json['location']['city']
		self.state = self.master_json['location']['state']

	def get_full_location(self):
		print '{}, {}'.format(self.city,self.state)


class CurrentConditions(Weather):

	def __init__(self, location):
		Weather.__init__(self, location)
		self.current = None
		self.weather = None
		self.temp = None
		self.temp = None
		self.feelslike = None
		self.wind = None
		self.gust = None
		self.get_current_conditions()
		self.get_full_location()
		self.__str__()

	def get_current_conditions(self):
		self.current = self.master_json['current_observation']
		self.weather = self.current['weather']
		self.temp = self.current['temp_f']
		self.feelslike = self.current['feelslike_f']
		self.wind = self.current['wind_mph']
		self.gust = self.current['wind_gust_mph']
		self.precip = self.current['precip_today_in']

	def __str__(self):
		self.get_full_location
		print 'Weather: %s' % self.weather
		print 'Temp: %sF' % self.temp
		print 'Wind: %smph' % self.wind
		print 'Gust: %smph' %self.gust
		print 'Feels Like: %sF' % self.feelslike
		print 'Precip: %s"' % self.precip


class Forecast(Weather):

	def __init__(self, location, duration):
		Weather.__init__(self, location)
		self.duration = duration
		self.ten_day = None
		self.get_ten_day()
		self.__str__()

	def get_ten_day(self):
		self.ten_day = self.master_json['forecast']['simpleforecast']['forecastday']

	def get_date(self, period):
		day = self.ten_day[period]
		dates = day['date']
		date = dates['pretty']
		return date

	def __str__(self):
		for day in range(self.duration):
			day_weather = self.ten_day[day]
			date = self.get_date(day)
			conditions = day_weather['conditions']
			high = day_weather['high']['fahrenheit']
			low = day_weather['low']['fahrenheit']
			snow = day_weather['snow_allday']['in']
			snow_day = day_weather['snow_day']['in']
			snow_night = day_weather['snow_night']['in']
			self.get_full_location
			self.forecast_out = {'day':day
								,'day_weather':day_weather
								,'date':date
								,'conditions':conditions
								,'high':high
								,'low':low
								,'snow':snow
								,'snow_day':snow_day
								,'snow_night':snow_night
								}
			return self.forecast_out
