# weather_email.py


import smtplib
from weather_main import CurrentConditions, Forecast


location = {'eldora':'q/zmw:80466.4.99999'
		   ,'home':'q/zmw:80303.1.99999'
		   ,'hwy72_ward':'q/zmw:80481.1.99999'
		   ,'allenspark':'q/zmw:80510.1.99999'}

forecast = Forecast(location['home'],1)
snow = [forecast.forecast_out['snow']
	   ,forecast.forecast_out['snow_day']
	   ,forecast.forecast_out['snow_night']]
date = forecast.forecast_out['date']
snow_total = sum(snow)

if snow_total > 6:
	msg = 'The forecast as of %s calls for %.1f" of snow!' % (date, snow_total)
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('USERNAME','PASSWORD') #OMMITTED IN THIS VERSION OF CODE
		server.sendmail("luke.reed.vt@gmail.com", "luke.reed.vt@gmail.com", msg)
		server.quit()
	except smtlib.SMTPException:
	   print "Error: unable to send email"
