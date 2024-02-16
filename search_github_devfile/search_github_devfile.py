import os
import yaml
import requests
from github import Github
from github import Auth


def parse_devfile_url(url):
    
   response = requests.get(url, allow_redirects=True)
   content = response.content.decode("utf-8")
   data = yaml.safe_load(content)
   
   if "schemaVersion" in data:
      schemaVersion = data["schemaVersion"]
      if schemaVersion == "2.0.0" or schemaVersion == "2.1.0" or schemaVersion == "2.2.0":
         print("devfile has schemaVersion ", schemaVersion, " and will be chosen for training the model")

def search_github():
    
   access_token = os.environ["ACCESS_TOKEN"]
   
   # using an access token
   auth = Auth.Token(access_token)
   
   # pygithub object
   g = Github(auth=auth)
   
   codes = g.search_code(query="filename:devfile.yaml")
   
   print("Total number of files titled devfile.yaml after search: ", codes.totalCount, end="\n")
   print("-----")
   
   x = 0
   for code in codes:
       x += 1
       print("Repo: ",  code.repository)
       print("File URL: ", code.html_url)
       print("Download URL: ", code.download_url)
       parse_devfile_url(code.download_url)
       print("-----")
       if x == 24:
           break

search_github()