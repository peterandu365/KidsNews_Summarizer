import requests
from bs4 import BeautifulSoup
import openai
import datetime

# Parameters
URL = "https://www.cbc.ca/kidsnews/"
openai.api_key = 'YOUR_OPENAI_API_KEY'
grade_number = 3
word_count = 50

# Fetch the top three article links from Kids News homepage
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
article_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("/kidsnews/post/")]
top_three_links = list(set(article_links[:3]))  # Use set to remove duplicates and then get the top three

# Extract content from each article link
articles = []
for link in top_three_links:
    response = requests.get("https://www.cbc.ca" + link)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_content = soup.find('div', {'class': 'story'}).text
    articles.append(article_content)

# Use OpenAI API to rewrite article content
shortened_articles = []
for article in articles:
    prompt = f"Please summarize the following news article for a grade {grade_number} student. Keep it under {word_count} words:\n\n{article}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=word_count
    )
    shortened_articles.append(response.choices[0].text.strip())

# Save to a file with date as prefix
today_date = datetime.date.today().strftime('%Y%m%d')
for idx, summary in enumerate(shortened_articles):
    title = summary.split('.')[0].replace(' ', '_').replace(',', '')  # Use the first sentence of the summary as filename
    with open(f"{today_date}_{title}.txt", "w") as file:
        file.write(summary)

print("Summaries generated and saved!")
