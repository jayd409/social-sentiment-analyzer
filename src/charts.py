import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sentiment import sentiment_score, analyze_posts

def sentiment_by_platform(df):
    """Chart 1: Sentiment distribution by platform (stacked bar)."""
    pivot = pd.crosstab(df['platform'], df['sentiment'])
    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind='bar', stacked=True, ax=ax, color=['red', 'gray', 'green'])
    ax.set_title('Sentiment Distribution by Platform', fontsize=12, fontweight='bold')
    ax.set_xlabel('Platform')
    ax.set_ylabel('Post Count')
    ax.legend(title='Sentiment')
    ax.tick_params(axis='x', rotation=45)
    return fig

def sentiment_by_topic(df):
    """Chart 2: Average sentiment by topic (bar, colored)."""
    topic_sentiment = df.groupby('topic')['sentiment_score'].mean().sort_values()
    colors = ['red' if x < 0 else 'gray' if x == 0 else 'green' for x in topic_sentiment.values]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(topic_sentiment.index, topic_sentiment.values, color=colors)
    ax.set_title('Average Sentiment by Topic', fontsize=12, fontweight='bold')
    ax.set_xlabel('Topic')
    ax.set_ylabel('Sentiment Score')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    return fig

def engagement_vs_sentiment(df):
    """Chart 3: Engagement (likes+shares) vs sentiment scatter."""
    df_copy = df.copy()
    df_copy['engagement'] = df_copy['likes'] + df_copy['shares']
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df_copy['sentiment_score'], df_copy['engagement'], alpha=0.5, s=30, color='purple')
    ax.set_title('Engagement vs Sentiment', fontsize=12, fontweight='bold')
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Engagement (Likes + Shares)')
    return fig

def sentiment_trend(df):
    """Chart 4: Sentiment trend over time (monthly by platform)."""
    df_copy = df.copy()
    df_copy['date'] = pd.to_datetime(df_copy['date'])
    df_copy['month'] = df_copy['date'].dt.to_period('M').astype(str)
    monthly = df_copy.groupby(['month', 'platform'])['sentiment_score'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 5))
    for platform in df_copy['platform'].unique():
        platform_data = monthly[monthly['platform'] == platform]
        ax.plot(platform_data['month'], platform_data['sentiment_score'], marker='o', label=platform)
    ax.set_title('Sentiment Trend Over Time', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Avg Sentiment Score')
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    return fig

def sentiment_breakdown(df):
    """Chart 5: Overall sentiment breakdown (donut)."""
    sentiment_counts = df['sentiment'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['green', 'gray', 'red']
    wedges, texts, autotexts = ax.pie(sentiment_counts.values, labels=sentiment_counts.index,
                                        autopct='%1.1f%%', colors=colors[:len(sentiment_counts)],
                                        pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.set_title('Overall Sentiment Distribution', fontsize=12, fontweight='bold')
    return fig

def top_engaged_posts(df):
    """Chart 6: Top 10 most engaged posts (horizontal bar)."""
    df_copy = df.copy()
    df_copy['engagement'] = df_copy['likes'] + df_copy['shares']
    top_10 = df_copy.nlargest(10, 'engagement')

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['green' if s == 'Positive' else 'red' if s == 'Negative' else 'gray'
              for s in top_10['sentiment']]
    ax.barh(range(len(top_10)), top_10['engagement'], color=colors)
    ax.set_yticks(range(len(top_10)))
    ax.set_yticklabels([f"{pid[:12]}" for pid in top_10['post_id']], fontsize=8)
    ax.set_title('Top 10 Most Engaged Posts', fontsize=12, fontweight='bold')
    ax.set_xlabel('Engagement (Likes + Shares)')
    return fig
