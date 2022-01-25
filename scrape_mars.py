from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# import pymongo

def scrape_fn():
# Set up Splinter
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# Visit redplanet.com
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape Redplanet page into Soup
    
    html = browser.html
    soup = bs(html, "html.parser")

    # Collect and store latest News Title and Paragraph Text 
    
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
# Visit spaceimages-mars.com.com
    
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape Redplanet page into Soup
    
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the image url for the current Featured Mars Image
    # And assign the url string to a variable called `featured_image_url
    
    featured_image_url = soup.find('img', class_='headerimage')['src']
    featured_image_full_url = url + featured_image_url

# Visit galaxyfacts-mars.com

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url) 
    df = tables[0]

# Visit marshemispheres.com/
    # cerberus
    browser = Browser('chrome', **executable_path, headless=False) 
    url = 'https://marshemispheres.com/cerberus.html' 
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser') 

    href = soup.find('img', class_='wide-image')['src'] # soup.find_all('a')[4]['href'] 
    cerberusimg = 'https://marshemispheres.com/' + href
    cerberustitle=soup.find('h2',class_='title').text
    
    # schiaparelli
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/schiaparelli.html' 
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')

    href = soup.find('img', class_='wide-image')['src'] # soup.find_all('a')[4]['href'] 
    schiaparelliimg = 'https://marshemispheres.com/' + href
    schiaparellititle=soup.find('h2',class_='title').text
    
    # syrtis
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/syrtis.html' 
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser') # https://marshemispheres.com/

    href = soup.find('img', class_='wide-image')['src'] # soup.find_all('a')[4]['href'] 
    syrtisimg = 'https://marshemispheres.com/' + href
    syrtistitle=soup.find('h2',class_='title').text
    
    # Valles
    browser = Browser('chrome', **executable_path, headless=False) # opens a browser window
    url = 'https://marshemispheres.com/valles.html' 
    browser.visit(url) 

    html = browser.html
    soup = bs(html, 'html.parser') # https://marshemispheres.com/

    href = soup.find('img', class_='wide-image')['src'] # soup.find_all('a')[4]['href'] 
    vallesimg = 'https://marshemispheres.com/' + href
    vallestitle=soup.find('h2',class_='title').text

# Return a Python dictionary containing all scraped data
    mars_dict = {"News_Title":news_title,
    "Text":news_p,
    "Featured_Image":featured_image_full_url,
    # "Mars_Facts":df,
    "Cerberus_Img":cerberusimg,
    "Cerberus_Title":cerberustitle,
    "Schiaparelli_Img":schiaparelliimg,
    "Schiaparelli_Title":schiaparellititle,
    "Syrtis_Img":syrtisimg,
    "Syrtis_Title":syrtistitle,
    "Valles_Img":vallesimg,
    "Valles_Title":vallestitle  
}
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_dict

