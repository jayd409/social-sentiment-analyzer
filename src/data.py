import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

TEMPLATES = {
    'positive': [
        "Really excited about the latest {topic} breakthrough! #Innovation",
        "Amazing experience with {topic} today, couldn't be happier! {hashtag}",
        "The future of {topic} is incredibly bright, loving the progress {hashtag}",
        "{topic} keeps exceeding my expectations, absolutely fantastic {hashtag}",
        "Just had the best {topic} experience of the year! Highly recommend {hashtag}",
        "Impressed by the recent {topic} improvements, great work! {hashtag}",
    ],
    'negative': [
        "Disappointed with recent {topic} changes, really frustrating {hashtag}",
        "The {topic} situation is getting worse, when will they fix this? {hashtag}",
        "Why does {topic} always have these issues? Needs serious improvement {hashtag}",
        "Terrible experience with {topic} today, switching platforms {hashtag}",
        "Can't believe how bad {topic} has become lately {hashtag}",
        "The {topic} leadership needs to do better, we deserve more {hashtag}",
    ],
    'neutral': [
        "Just read about the latest {topic} developments {hashtag}",
        "Interesting perspective on {topic} from various angles {hashtag}",
        "The {topic} discussion continues as expected, some good points raised {hashtag}",
        "Here's what I think about the {topic} situation {hashtag}",
        "{topic} seems to be trending everywhere, lots of opinions out there {hashtag}",
        "Mixed reactions to the new {topic} news, opinions vary {hashtag}",
    ]
}

TOPICS_WITH_HASHTAGS = {
    'AI Technology': '#AIRevolution #ChatGPT #MachineLearning',
    'Electric Vehicles': '#Tesla #EVs #ClimateAction',
    'Remote Work': '#WorkFromHome #FutureOfWork #Hybrid',
    'Stock Market': '#StockMarket #Investing #Bitcoin',
    'Climate Policy': '#ClimateChange #GreenEnergy #Sustainability',
    'NBA': '#NBA #Basketball #Lakers',
    'NFL': '#NFL #Football #SuperBowl',
    'Food Delivery': '#FoodDelivery #DoorDash #UberEats',
    'Streaming': '#Netflix #Disney #StreamingWars',
}

def generate_posts(n=3000):
    """Generate 3000 realistic social media posts across major platforms."""
    # Realistic platform distribution
    platforms = {
        'Twitter': 0.40,
        'LinkedIn': 0.25,
        'Instagram': 0.20,
        'Reddit': 0.15,
    }

    topics = list(TOPICS_WITH_HASHTAGS.keys())

    posts = []
    start_date = datetime(2024, 1, 1)

    for i in range(n):
        platform = np.random.choice(list(platforms.keys()), p=list(platforms.values()))
        topic = np.random.choice(topics)
        date = start_date + timedelta(days=np.random.randint(0, 90))

        # Realistic sentiment distribution: 42% positive, 35% neutral, 23% negative
        sentiment_type = np.random.choice(['positive', 'neutral', 'negative'],
                                         p=[0.42, 0.35, 0.23])
        template = np.random.choice(TEMPLATES[sentiment_type])
        hashtag = np.random.choice(TOPICS_WITH_HASHTAGS[topic].split())
        text = template.format(topic=topic, hashtag=hashtag)

        # Platform-based engagement patterns
        if platform == 'Twitter':
            likes = int(np.random.normal(45, 35))
            shares = int(np.random.normal(15, 12))
        elif platform == 'LinkedIn':
            likes = int(np.random.normal(120, 85))
            shares = int(np.random.normal(25, 18))
        elif platform == 'Instagram':
            likes = int(np.random.normal(380, 250))
            shares = int(np.random.normal(18, 14))
        else:  # Reddit
            likes = int(np.random.normal(85, 60))
            shares = int(np.random.normal(22, 16))

        likes = max(0, likes)
        shares = max(0, shares)

        # Sentiment affects engagement slightly
        if sentiment_type == 'positive':
            likes = int(likes * 1.15)
            shares = int(shares * 1.10)
        elif sentiment_type == 'negative':
            likes = int(likes * 0.90)
            shares = int(shares * 0.85)

        comments = int(likes * np.random.uniform(0.08, 0.25))
        reach = likes * np.random.randint(3, 12)

        posts.append({
            'post_id': f'POST{i+1:05d}',
            'platform': platform,
            'topic': topic,
            'date': date.strftime('%Y-%m-%d'),
            'text': text,
            'likes': max(0, likes),
            'shares': max(0, shares),
            'comments': max(0, comments),
            'reach': max(0, reach)
        })

    return pd.DataFrame(posts)
