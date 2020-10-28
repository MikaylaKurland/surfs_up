import datetime as dt
import numpy as np
import pandas as pd
#import SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#setting up the database engine for the flask app
#access the sqlite database
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)


#create a Flask application called "app."
app = Flask(__name__)
#define the welcome route
@app.route('/')

#function to add the routing information for each of the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    '''
    )

#adding a route for the precipitatin analysis
@app.route("/api/v1.0/precipitation")

#create the precipitation function
#retrieve the last 12 months of precipitation data and plot the results starting from the last data point in the database. 
def precipitation():
    ## Calculate the date one year from the last date in data set.
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   ## Perform a query to retrieve the data and precipitation scores
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   ## ccreate a dictionary with the date as the key and the precipitation as the value
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


#adding a route for the stations analysis
@app.route("/api/v1.0/stations")
#create the stations function

def stations():
    #unraveling our results into a one-dimensional array
    results = session.query(Station.station).all()
    #convert our unraveled results into a list
    stations = list(np.ravel(results))
    ##  jsonify our stations list, and then return it
    return jsonify(stations=stations)


#adding route for the temperature observations from the previous year
@app.route("/api/v1.0/tobs")
#create the temp_monthly function
def temp_monthly():
    #Calculate the date one year from the last date in the data set
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    ## perform a query to retrieve the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
        ## unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    ##  jsonify our temps list, and then return it
    return jsonify(temps=temps)

#adding route for the statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#create the stats function
def stats(start=None, end=None):
    #create a query to select the max, min, and avg temperatures from the sqlite database, adding them to a list called 'sel'
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    ##determine the starting and ending date
    ###ake note of the asterisk in the query next to the set list. Here the asterisk is used to indicate there will be multiple results for our query
    if not end: 
        results = session.query(*sel).\
            filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)