'''
------Instructions------

Generate user links
Your task is to create userlinks for the url, you will be given a username and must return a valid link.

Example
generate_link('matt c')
http://www.codewars.com/users/matt%20c
reference
use this as a reference https://www.w3schools.com/tags/ref_urlencode.asp




------Test Cases------'
  'matt c', 'http://www.codewars.com/users/matt%20c'
  'g964', 'http://www.codewars.com/users/g964'
  'GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi'
  'ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra'
  'colbydauph', 'http://www.codewars.com/users/colbydauph'

  
------Solution------
'''
import urllib.parse

def generate_link(user):
    return f"http://www.codewars.com/users/{urllib.parse.quote(user)}"


