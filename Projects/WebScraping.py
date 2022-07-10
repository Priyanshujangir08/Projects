import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github UserName: ")

# Send the request to url 
# url = github url with the Username

url ='https://github.com/'+github_user           
r = requests.get(url)

# we're going to get all HTML code og that page 

soup = bs(r.content,'html.parser')
profile_image = soup.find('img',{'alt':'Avatar'})['src']    #  find the tag of image with atribute of Avatar and get src
print(profile_image)