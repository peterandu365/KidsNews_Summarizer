from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import openai
import os

URL = "https://www.cbc.ca/kidsnews/"

# Set up Selenium, using Chrome as an example here
driver = webdriver.Chrome()

# Open the webpage
driver.get(URL)

# Wait for the page to load
sleep(5)

# Find the article links
article_links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/kidsnews/post/']")

# Get the first three links
top_three_links = [link.get_attribute('href') for link in article_links[:3]]

# Extract content from each article link
articles = []

for link in top_three_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Search for the correct div containing the article content
    article_content = soup.find('div', {'class': 'content'})
    
    if article_content:
        articles.append(article_content.text)

# Close the Selenium browser
driver.close()

# OpenAI API setup
openai.api_key = 'YOUR_OPENAI_API_KEY'

import time

# Summarize articles using openai.ChatCompletion
summarized_articles = []

for article in articles:
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {"role": "system", "content": "Summarize the following article for a Grade 3 student in 50 words:"},
            {"role": "user", "content": article}
        ]
    )
    summarized_articles.append(response['choices'][0]['message']['content'].strip())
    
    # Wait for 20 seconds before processing the next article to avoid rate limits
    time.sleep(20)

# Save to a file
date_str = datetime.now().strftime("%Y%m%d")
for i, summary in enumerate(summarized_articles):
    with open(f"{date_str}_Article_{i + 1}.txt", 'w') as f:
        f.write(summary)
