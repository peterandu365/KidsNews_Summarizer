# KidsNews Summarizer

![Build Status](https://img.shields.io/badge/build-passing-green.svg) ![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

`KidsNews Summarizer` is an automation tool that extracts and condenses articles from CBC Kids News. It rephrases the content to match the comprehension level of Grade 3 students and keeps the summaries within a 50-word limit, making them optimal for memorization exercises.

## Features

- **Automated News Extraction**: Extracts top articles directly from CBC Kids News.
- **Content Summarization**: Uses OpenAI's GPT to generate concise versions suitable for Grade 3 students.
- **Optimized for Memorization**: Each summary is kept within a 50-word limit.

## Setup and Usage

1. Clone this repository.
2. Install required Python packages: `pip install beautifulsoup4 requests openai`.
3. Add your OpenAI API key in the script.
4. Run the script to generate summaries: `python main.py`.

## Contribution

Suggestions, improvements, and fixes are always welcome!

## Citation

If you use this tool in your project or research, please cite:

```
Peter Xu, Kids News Summarizer, https://github.com/peterandu365/KidsNews_Summarizer, 2023
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
