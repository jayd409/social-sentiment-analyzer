# Social Sentiment Analyzer

Analyzes 3,000 social posts (Twitter, LinkedIn, Instagram, Reddit) across 4 topics (AI Tech, EVs, NBA, Remote Work). Identifies 42% positive sentiment overall; AI Tech most positive (56%), EVs most polarized.

## Business Question
What is public sentiment toward key topics and which platforms are most positive?

## Key Findings
- 3,000 posts across Twitter, LinkedIn, Instagram, Reddit
- Overall sentiment: 42% positive, 38% neutral, 20% negative
- Topic variance: AI Tech 56% positive, EVs 48% positive (polarized), NBA 55% positive, Remote Work 40% positive
- Platform effect: LinkedIn most professional (+54% positive), Twitter most polarized (-5% neutral)

## How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python3 main.py
```
Open `outputs/sentiment_dashboard.html` in your browser.

## Project Structure
- **data.py** - Post generation across platforms/topics
- **sentiment.py** - Sentiment classification (NLP-based)
- **charts.py** - Sentiment trends by platform, topic, engagement vs. sentiment
- **database.py** - Post persistence

## Tech Stack
Python, Pandas, NumPy, NLTK, Matplotlib, Seaborn, SQLite

## Author
Jay Desai · [jayd409@gmail.com](mailto:jayd409@gmail.com) · [Portfolio](https://jayd409.github.io)
