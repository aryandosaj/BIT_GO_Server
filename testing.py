import requests 
  
# from flask import jsonify

import scrap
scrap.get_detail('BE/10080/17','Gudda@1999')
  

data = {'Roll':'BE/10080/17','Password':'1234'}
  
# # sending post request and saving response as response object 
r = requests.post(url = 'https://eae455bb.ngrok.io', data = data) 


# print(r.json())
  