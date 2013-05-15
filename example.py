from forecast_io import *

apikey = '6161e86a8c982e4ee06b622146a826cc'



"""
EXAMPLE 1 

Ouput temperature time humidity windSpeed summary for list of cities

"""

def example1(apikey):
  locations = ['Amsterdam,NL', 'Philadelphia, PA', 'Kiyv,Ukraine', 'Rio de Janeiro, Brazil', 'Berlin, Germany', 'Sydney, Australia']

  weather = forecast_io(apikey, units = 'si')
   
  print("%-25s %s %s %s %s %s" % ('location', "temperature", "time", "humidity", "windSpeed", "summary"))
  for location in locations:
    weather.setLocation(location)
    weather_list = weather.getParameterizedWeather(['temperature', 'time', 'humidity', 'windSpeed', 'humidity', 'summary' ])
    print("%-25s" % location),
    for param in weather_list:
      print param,
    print ""



"""
Output:

location                  temperature time humidity windSpeed summary
Amsterdam,NL              12.01 1368643650 0.65 6.76 0.65 Overcast
Philadelphia, PA          21.28 1368643650 0.53 5.08 0.53 Sprinkling
Kiyv,Ukraine              19.91 1368643650 0.71 1.24 0.71 Sprinkling
Rio de Janeiro, Brazil    29.29 1368643650 0.62 3.07 0.62 Clear
Berlin, Germany           21.32 1368643650 0.49 6.21 0.49 Clear
Sydney, Australia         13.33 1368643650 0.61 4.68 0.61 Mostly Cloudy

"""

"""
EXAMPLE 2

Get daily values for New York City
"""

def example2(apikey):
  weather = forecast_io(apikey, units = 'si')
  weather.setLocation('New York, NY')
  weather.getWeather('daily')
  print json.dumps(weather.result)


"""
{"data": [{
   "humidity": 0.59, 
   "precipIntensityMaxTime": 1368655519, 
   "dewPoint": 5.52, 
   "precipType": "rain", 

   "temperatureMinTime": 1368601200, 
   "temperatureMaxTime": 1368648000, 
   "temperatureMax": 18.07, 
   "summary": "Light rain in the evening.", 
   "cloudCover": 0.74, 
   "sunsetTime": 1368662848, 
   "ozone": 357.8, 
   "pressure": 1015.62, 
   "windSpeed": 3.4, 
   "temperatureMin": 10.52, 
   "visibility": 15.62, 
   "time": 1368590400, 
   "windBearing": 179, 
   "precipIntensity": 0.047, 
   "precipIntensityMax": 0.021, 
   "sunriseTime": 1368610803, 
   "icon": "rain"}
]}"
 """

"""
EXAMPLE 3 
"""

def example3(apikey):

  city = 'Los Angeles, CA'
  weather = forecast_io(apikey, units = 'si')
  weather.setLocation(city)
  weather.getWeather("daily")

  data = weather.result

  print("Sunrise in %s was at %s. Day maximum: %.2fC. Day minimum %.2fC. Summary %s" % (
      city, 
      time.strftime("%H:%M:%S", time.localtime(int(data['sunriseTime']))), 
      data['temperatureMax'],
      data['temperatureMin'],
      data['summary']
      )
  )

if __name__ == "__main__":
  print('This is just example')
  print('Example1:')
  example1(apikey)
  print('Example2:')
  example2(apikey)
  print('Example3:')
  example3(apikey)