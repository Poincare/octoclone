import requests
import json
import sys
import subprocess

try:
  from termcolor import colored, cprint
  termcolor_loaded = True
except ImportError:
  termcolor_loaded = False

if __name__ == "__main__":
  r = requests.get('https://api.github.com/users/' + sys.argv[1] + '/repos')

  if(r.ok):
    repos = json.loads(r.text or r.content)
    for repo in repos: 
      repo_url = "git@github.com:" + repo['full_name'] + ".git"
      subprocess.call(["git", "clone", repo_url])

      pretext = "cloned: " + repo_url
      if termcolor_loaded:
        text = colored("cloned: " + repo_url, 'green');
      else:
        text = "cloned: " + repo_url

      print text 
       
