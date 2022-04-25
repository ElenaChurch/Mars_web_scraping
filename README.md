# web-scraping-challenge

Mars Web Scraping project

Created a web page to show information about mars from 4 different sources. Extracted Mars  content from three different websites utilizing HTML Parsers Splinter and BeautifulSoup. Then created a flask application to route to content a new HTML webpage to display all the aggregated Mars information.  

•	Role: Sole author

•	Tools: flash, python, pandas, jupyter notebook, beatifulSoup, Browser, HTML 

###Summary of web page
At the top is a button the user presses to call the scrape route which in turn call the scrape.py  to scrape the 4 webpages that contain the information that needs to be displayed. Then the page will display the latest mars news at the top. Then to the right a table of mars facts will then display. At the bottom of the page you will see pictures that are clickable and take you to a larger image of each hemispheres as well as some facts. 

###How the Mars Scraping web scraping app works
In the mars_scrape.py are functions that can scrape the 4 differnt sites. Then a flask app was created with routes that call those fuctions and routes that information to the HTML page.
