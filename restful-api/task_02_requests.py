#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status code: {resp.status_code}")
    
    if resp.status_code == 200:
        posts = resp.json()
        
        for post in posts:
            print(post['title'])
    else:
        print("Eror")

def fetch_and_save_posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if posts.status_code == 200:
        datos = posts.json()
    else:
        return

    estruct_list = []

    for post in datos:
        new_estruct = {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        }
    estruct_list.append(new_estruct)

    with open('posts.cvs', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(estruct_list)
