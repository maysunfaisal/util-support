import os
import yaml
import requests
from github import Github
from github import Auth


def parse_devfile_url(url):
    
   response = requests.get(url, allow_redirects=True)
   content = response.content.decode("utf-8")
   try:
      data = yaml.safe_load(content)
   except:
      return None
   
   if "schemaVersion" in data:
      schemaVersion = data["schemaVersion"]
      if schemaVersion == "2.0.0" or schemaVersion == "2.1.0" or schemaVersion == "2.2.0":
         print("devfile has schemaVersion ", schemaVersion, " and will be chosen for training the model")
         return data
   return None

def search_github():
    
   access_token = os.environ["ACCESS_TOKEN"]
   
   # using an access token
   auth = Auth.Token(access_token)
   
   # pygithub object
   g = Github(auth=auth)
   
   codes = g.search_code(query="filename:devfile.yaml schemaVersion")
   
   print("Total number of files titled devfile.yaml after search: ", codes.totalCount, end="\n")
   print("-----")
   
   x = 0
   devfile_data_list = []
   for code in codes:
       x += 1
       print("Repo: ",  code.repository)
       print("File URL: ", code.html_url)
       print("Download URL: ", code.download_url)
       parsed_data = parse_devfile_url(code.download_url)
       if parsed_data is not None:
          print("devfile content has been downloaded")
          devfile_data_list.append(devfile_data_list)
       print("-----")
       if x == 24:
           break

search_github()