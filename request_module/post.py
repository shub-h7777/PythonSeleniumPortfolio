import requests

import config

""" for add/post the users """

url = config.users()

# take the user input
name = input("Enter the name: ")
email = input("Enter the email: ")
gender = input("Enter the gender: ")
status = input("Enter the status: ")

# create data for the input
data = dict()
data['name'] = name
data['email'] = email
data['gender'] = gender
data['status'] = status

headers = dict()
headers['Authorization'] = 'Bearer ' + config.Access_Token

post = requests.post(url, data=data, headers=headers)
print(post.json())
