import sys
sys.path.insert(0, 'src')

from data import generate_posts
from sentiment import analyze_posts
from charts import (sentiment_by_platform, sentiment_by_topic, engagement_vs_sentiment,
                    sentiment_trend, sentiment_breakdown, top_engaged_posts)
from utils import save_html

df = generate_posts(3000)
df = analyze_posts(df)

total = len(df)
positive_pct = (df['sentiment'] == 'Positive').sum() / total * 100
negative_pct = (df['sentiment'] == 'Negative').sum() / total * 100
neutral_pct = (df['sentiment'] == 'Neutral').sum() / total * 100

charts = [
    ('Sentiment by Platform', sentiment_by_platform(df)),
    ('Sentiment by Topic', sentiment_by_topic(df)),
    ('Engagement vs Sentiment', engagement_vs_sentiment(df)),
    ('Sentiment Trend', sentiment_trend(df)),
    ('Overall Sentiment', sentiment_breakdown(df)),
    ('Top Engaged Posts', top_engaged_posts(df))
]

kpis = [
    ('Posts Analyzed', str(total)),
    ('Positive', f"{positive_pct:.1f}%"),
    ('Negative', f"{negative_pct:.1f}%"),
]

save_html(charts, 'Social Sentiment Analysis', kpis, 'outputs/sentiment_dashboard.html')

print(f"Posts analyzed: {total} | Positive: {positive_pct:.1f}% | Negative: {negative_pct:.1f}% | Neutral: {neutral_pct:.1f}%")
