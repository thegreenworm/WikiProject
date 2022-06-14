import mysql.connector
from mysql.connector import errorcode
import pandas as pd

# Obtain connection string information from the portal
config = {
  'host':'wikiproject.mysql.database.azure.com',
  'user':'admins@wikiproject',
  'password':'Wikiproject335',
  'database':'newschema',
#   'client_flags': [ClientFlag.SSL],
#   'ssl_cert': '/var/wwww/html/DigiCertGlobalRootG2.crt.pem'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  dfcols = ["GeoId","Latitude","Longtitude"]
  dfrows = []
  cursor.execute("SELECT * FROM geo_tags limit 2;")
  rows = cursor.fetchall()
  for row in rows:
    #   print("data = (%s, %s)" %(str(row[4]), str(row[5])))
      dfrows.append({"GeoId":str(row[0]),"Latitude":str(row[4]), "Longtitude": str(row[5])})

  df = pd.DataFrame(dfrows,columns=dfcols)
  print(df)

