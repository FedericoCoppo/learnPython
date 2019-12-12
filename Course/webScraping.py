#
# author: F.Coppo from Edx course
# description: web scraping example
#
import bs4			#  Python library for pulling data out of HTML and XML files
import requests		#  Python module that you can use to send all kinds of HTTP requests.
import pandas as pd
import numpy as np
import boto3        # Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2

link='https://en.wikipedia.org/wiki/Michael_Jordan'
response = requests.get(link) # read the webpage 
soup = bs4.BeautifulSoup(response.text, 'html.parser') # library that scrape information from web pages -> create a BeautifulSoup object to parse the HTML  

# the player statistics are defined  with the attribute CSS class set to 'wikitable sortable'; 
# therefore we create a tag object "table"
table = soup.find(class_='wikitable sortable') # find() -> Extracting attributes from a tag
"""
table class="wikitable sortable" style="font-size:95%; text-align:right;">
<tbody><tr>
<th>Year
</th>
<th>Team
</th>
<th><abbr title="Games played">GP</abbr>
</th>
<th><abbr title="Games started">GS</abbr>
</th>
<th><abbr title="Minutes per game">MPG</abbr>
</th>
<th><abbr title="Field goal percentage">FG%</abbr>
</th>
<th><abbr title="3-point field-goal percentage">3P%</abbr>
.
.
"""

headers=table.tr   # the headers of the table are the first table row (tr) we create a tag object that has the first row  

titles=headers.find_all("abbr")     # the table column names are displayed  as an abbreviation; therefore we find all the abbr tags and returs an Iterator
"""
[<abbr title="Games played">GP</abbr>, <abbr title="Games started">GS</abbr>, <abbr title="Minutes per game">MPG</abbr>, 
<abbr title="Field goal percentage">FG%</abbr>, <abbr title="3-point field-goal percentage">3P%</abbr>, <abbr title="Free-throw percentage">FT%</abbr>, <abbr title="Rebounds per game">RPG</abbr>, 
<abbr title="Assists per game">APG</abbr>, <abbr title="Steals per game">SPG</abbr>, <abbr title="Blocks per game">BPG</abbr>, <abbr title="Points per game">PPG</abbr>]]
"""	

for title in titles:
	print(title['title'])
"""	
Games played
Games started
Minutes per game
Field goal percentage
3-point field-goal percentage
Free-throw percentage
Rebounds per game
Assists per game
Steals per game
Blocks per game
Points per game
"""
data = {title['title']:[] for title in titles} # create a dictionary  and pass the table headers as the keys 

"""
data:
{'Games played': [], 'Games started': [], 'Minutes per game': [], 'Field goal percentage': [], 
'3-point field-goal percentage': [], 'Free-throw percentage': [], 'Rebounds per game': [], 
'Assists per game': [], 'Steals per game': [], 'Blocks per game': [], 'Points per game': []}
"""

# we will store each column as a list in a dictionary, the header of the column will be the dictionary key 
#we iterate over each table row by fining each table tag tr and assign it to the objed
for row in table.find_all('tr')[1:]:
    
    #we iterate over each cell in the table, as each cell corresponds to a different column we all obtain the correspondin key corresponding the column n 
    for key,a in zip(data.keys(),row.find_all("td")[2:]):
        # we append each elment and strip any extra HTML contnet 
        data[key].append(''.join(c for c in a.text if (c.isdigit() or c == ".")))

# we remove extra rows by finding the smallest list     
Min=min([len(x)  for x in data.values()])
#we convert the elements in the key to floats 
for key in data.keys():
    data[key]=list(map(lambda x: float(x), data[key][:Min]))
    

# PLOT
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
dictio = data
print(dictio)
pd_michael = pd.DataFrame(dictio)
plt.plot(pd_michael[['Points per game']],label='Jordan')
plt.legend()
plt.xlabel('years')
plt.ylabel('Points per game')
plt.show()
