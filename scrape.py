import mechanicalsoup
import pandas as pd
import sqlite3

# scrape.py:
# Download the URL
# Parse the table entries into arrays
# Create a DataFrame
# Load into SQLite


# Download the URL #
url = "https://en.wikipedia.org/wiki/Mile_run_world_record_progression"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

tables = browser.page.find_all("table")
table = tables[4]

# Parse the table entries into arrays #
th = table.find_all("th")
progression = [value.text.replace("\n", "") for value in th]


td = table.find_all("td")
columns = [value.text.replace("\n", "") for value in td]

#print(columns)

# Create a DataFrame #
column_names = ["time",
                "auto",
                "athlete",
                "nationality", 
                "date", 
                "venue"]

# column[0:][::11]
# column[1:][::11]
# column[2:][::11]

dictionary = {}

for idx, key in enumerate(column_names):
    dictionary[key] = columns[idx:][::6]
print(dictionary)
df = pd.DataFrame(data = dictionary)
#print(df.head())
#print(df.tail())


# Load into SQLite #
connection = sqlite3.connect("progresso.db")
cursor = connection.cursor()
cursor.execute("create table progression (Progression, " + ",".join(column_names) + ")")
for i in range(len(df)):
    cursor.execute("insert into progression values (?,?,?,?,?,?)", df.iloc[i])

connection.commit()

connection.close()