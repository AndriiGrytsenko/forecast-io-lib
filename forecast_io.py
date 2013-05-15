import urllib2
import json
import time
from sys import exit
 
class forecast_io(object):
 
  def __init__(self, apikey, units = 'auto', url = 'https://api.forecast.io/forecast'):
    """
    This function initializes class.
    Accept:
    apikey: I will get it after registration at developer.forecast.io
    url: api url
    units: us, si, ca, uk, auto ( default is auto)
    """
    self.apikey = apikey
    self.url = url
    self.units = units

 
  def setLocation(self, place, time = time.time()):
    """
    This function is taking human readable geographic name and resolve 
    through the google maps API into latitude and longitude and set as class objects
    """
    place = place.replace(' ', '%20')
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % place
    try:
      data = json.load(urllib2.urlopen(url))
    except:
      print('Could not get location')
      exit()

    self.lat = data['results'][0]['geometry']['location']['lat']
    self.long = data['results'][0]['geometry']['location']['lng']
    self.time = time

 
  def setExcept(self, timespan):
    """
    This function creates filter list based on accepted value
    """
    exception = []

    for exp in ('currently', 'minutely', 'hourly', 'daily'):
      if timespan != exp:
        exception.append(exp)

    self.exception = exception

 
  def getWeather(self, timespan = 'full'):
    """ 
    This function returns the weather data for location in self.(lat,long)
    timespan: could be minutely,currently,hourly,daily,alerts,flags 
    """

    self.setExcept(timespan)
    url = '%s/%s/%f,%f,%i?units=%s&except=%s' % (self.url, self.apikey, self.lat, self.long, self.time, self.units, ','.join(self.exception))


    try:
      json_data = urllib2.urlopen(url)
    except:
      print('Could not get url')
      exit()

    data = json.load(json_data)
    if timespan in ('minutely', 'hourly', 'daily'):
      self.result = data[timespan]['data'][0]
    elif timespan == "currently":
      self.result = data[timespan]
    else:
      self.result = data

  def getParameterizedWeather(self, params, timespan = 'currently'):
    """
    This function returns specified paramters for current location
    Accept:
    params: full list find here  https://developer.forecast.io/docs/v2
    timespan: could be minutely,currently,hourly,daily,alerts,flags 
    """
    result = []
    self.getWeather(timespan = 'currently')
    for param in params:
      if type(self.result[param]) == float:
        self.result[param] = '%.2f' % self.result[param]
      elif type(self.result[param]) == unicode:
        self.result[param] = str(self.result[param])
      
      result.append(self.result[param])

    return result
