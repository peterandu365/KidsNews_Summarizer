# KidsNews_Summarizer

This repository contains an automated script designed to fetch top articles from a fictional Kids News website and then summarize them using OpenAI's API. This tool serves solely as a demonstration of how to employ Python libraries and the OpenAI API, without any operational intent.

## Changelog

### Latest Update (Version 2.0):
- **Web Scraping Enhancement**: Transitioned from BeautifulSoup (used for static web scraping) to Selenium, enabling handling of dynamic web pages where content loads asynchronously.
  
- **Summarization Upgrade**: Now incorporates `openai.ChatCompletion` to achieve a more refined and contextually aware summarization.

- **Rate Limit Handling**: Implemented a delay mechanism between consecutive API calls to avoid hitting OpenAI's API rate limits.

- **Code Organization**: Revamped code structure to enhance readability and maintainability.

### Initial Release (Version 1.0):
- Originally capable of fetching top articles and summarizing them via the OpenAI Completion API.
- Utilized BeautifulSoup for web scraping.

## Setup

1. Ensure Selenium is installed along with the necessary WebDriver (e.g., ChromeDriver).
2. Update the `openai.api_key` in the script to your OpenAI API key.
3. Execute the script. Summaries will be saved in the current directory with a date as the prefix.

## Usage

Execute the script as follows:

```
python kidsnews_summarizer.py
```

Post-execution, the script fetches the top three articles, summarizes them, and saves each summary as a `.txt` file in the directory.

## Future Improvements

- Augment error handling to address potential web scraping complications.
- Modify to allow summarization of more than just three articles if required.

## Contribution

Open to suggestions, improvements, and bug fixes!

## Citation

For referencing this tool in projects or research:

```
Peter Xu, Kids News Summarizer, https://github.com/peterandu365/KidsNews_Summarizer, 2023
```

## License

This project comes under the MIT License. For comprehensive details, refer to the [LICENSE](LICENSE) document.

---

**Disclaimer**: This project is purely for demonstration purposes on how to use Python libraries and the OpenAI API and is not intended for any operational use. It is not associated with or representative of any real news site; all mentioned news sources are fictional. Any actions taken using this project are at the user's own risk.

---