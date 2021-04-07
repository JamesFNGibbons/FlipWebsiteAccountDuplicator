import csv
import os
import sys

from pymongo import MongoClient

class WebsiteDuplicationScript:
  
  def __init__(self):
    self.args = self.getCmdLineArguments()
    
    # attempt connection to core account database.


  def establishCoreDatabaseConnection(self):
    dbName = self.args['dbName']
    dbUser = self.args['dbUser']
    dbPass = self.args['dbPass']
    dbHost = self.args['dbHost']

    print "Attmepting connection to core MongoDB database"
    connectionString = ''
    if(dbUser and dbPass):
      connectionString = 'mongodb://' + str(dbUser) + ':' = str(dbPass) + str('@')
    else:
      connectionString = 'mongodb://'
    connectionString += str(dbHost) + '/' + str(dbName)

    # attempt connection
    try:
      self.database = MongoClient(connectionString)
    except(Exception):
      print("Could not connect to mongodb")
      print(Exception)
      exit()


  def getCmdLineArguments(self):
    arguments = {}

    # check the provided arguments are valid.
    if(len(sys.argv) >= 2):
      for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        argProperty = arg.split('=')[0].split('--')[1]
        value = arg.split('=')[1]
        
        arguments[argProperty] = value

      # apply default values if not provided through cmd line
      try:
        if(arguments['dbHost'] is None):
          arguments['dbHost'] = '127.0.0.1'
          print "Using default mongodb host 127.0.0.1"

      except(KeyError):
        arguments['dbHost'] = '127.0.0.1'
        print "Using default mongodb host 127.0.0.1"

      try:
        if(arguments['dbName'] is None):
          print "Please provie database name [--dbName=]"
          exit()
      except(KeyError):
        print "Please provie database name [--dbName=]"
        exit()

      try:
        if(arguments['dbUser'] is None):
          print "Using default mongodb user (NIL)"
          arguments['dbUser'] = ''

      except(KeyError):
        print "Using default mongodb user (NIL)"
        arguments['dbUser'] = ''

      try:
        if(arguments['dbPassword'] is None):
          print "Using default mongodb passsord (NIL)"
          arguments['dbPass'] = ''

      except(KeyError):
        print "Using default mongodb password (NIL)"
        arguments['dbPass'] = ''

      # return arguments dictionary
      return arguments
    else:
      print "Please provide database details [--dbName= --dbUser= --dbPass= --dbHost=]"
      exit()


  def getTaskCsvFileLocation(self): 
    csvPath = input('Enter CSV file location, then [enter] -> ')
    
    # check if the path is valid
    if(os.path.isFile(csvPath)):
      print("Found CSV file at path " + csvPath)
      return csvPath

    else:
      print("Invalid CSV path")


if(__name__ == '__main__'):
  websiteDuplication = WebsiteDuplicationScript()
  