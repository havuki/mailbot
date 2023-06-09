
import openai
import requests
import os
from googleapiclient.discovery import build
from datetime import datetime, timedelta


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

GOOGLE_SEARCH_API_KEY = open_file('googleapikey.txt')

openai.api_key = open_file('openaiapikey.txt')

conversation = []

def fetch_ai_news():
    # Load Google Search API key and cx from files
    GOOGLE_SEARCH_API_KEY = open_file('googleapikey.txt')
   
    # Build the Google Search service
    search_service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_API_KEY)

    # Define the search query
    query = "AI"

    # Execute the search
    results = search_service.cse().list(q=query,  num=6).execute()

    # Extract relevant information from the search results
    news_items = [{'title': result['title'], 'snippet': result['snippet'], 'url': result['link']} for result in results['items']]

    return news_items

