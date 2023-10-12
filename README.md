# KidsNews_Summarizer

This repository contains an automated script to fetch top articles from the CBC Kids News website, and then summarizes them using OpenAI's API.

## Changelog

### Latest Update (Version 2.0):
- **Web Scraping Enhancement**: Previously, we used BeautifulSoup for static web scraping. This version introduces Selenium, which allows us to handle dynamic web pages where content might load asynchronously.
  
- **Summarization Upgrade**: The script now uses `openai.ChatCompletion` for a more refined and context-aware summarization.

- **Rate Limit Handling**: To avoid OpenAI's API rate limits, a delay is added between successive API calls.

- **Code Organization**: The structure of the code has been revised to be more readable and maintainable.

### Initial Release (Version 1.0):
- The script was capable of fetching top articles and summarizing them using OpenAI's Completion API.
- Used BeautifulSoup for web scraping.

## Setup

1. Make sure you have Selenium and the necessary WebDriver (e.g., ChromeDriver) installed.
2. Update the `openai.api_key` in the script with your OpenAI API key.
3. Run the script and the summaries will be saved in the current directory with the date as a prefix.

## Usage

Simply run the script:

```
python kidsnews_summarizer.py
```

After execution, the script will fetch the top three articles, summarize them, and save each summary as a `.txt` file in the current directory.

## Future Improvements

- Enhance error handling to cater for possible web scraping issues.
- Introduce flexibility to summarize more than three articles if needed.

## Contribution

Suggestions, improvements, and fixes are always welcome!

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, Kids News Summarizer, https://github.com/peterandu365/KidsNews_Summarizer, 2023
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.





