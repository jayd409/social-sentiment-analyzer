import numpy as np
import re

POS_WORDS = {'love', 'great', 'amazing', 'fantastic', 'best', 'excellent',
             'wonderful', 'happy', 'awesome', 'good', 'perfect', 'highly',
             'recommend', 'brilliant', 'outstanding'}
NEG_WORDS = {'hate', 'terrible', 'awful', 'horrible', 'worst', 'disappointed',
             'frustrating', 'bad', 'poor', 'useless', 'broken', 'mess',
             'worse', 'problem', 'issue'}
NEGATORS = {'not', 'never', 'no', 'hardly', 'barely', 'doesnt', 'isnt',
            'wasnt', 'dont'}

def sentiment_score(text):
    """Score sentiment of text (-1 to 1), return score and label."""
    if not text:
        return 0.0, 'Neutral'
    words = re.sub(r'[^\w\s]', '', text.lower()).split()
    score = 0
    for i, w in enumerate(words):
        mod = -1 if (i > 0 and words[i-1] in NEGATORS) else 1
        if w in POS_WORDS:
            score += mod
        elif w in NEG_WORDS:
            score -= mod
    n = max(len(words), 1)
    normalized = round(score / n, 4)
    label = 'Positive' if normalized > 0.01 else 'Negative' if normalized < -0.01 else 'Neutral'
    return normalized, label

def analyze_posts(df):
    """Add sentiment score and label to posts."""
    df = df.copy()
    results = [sentiment_score(t) for t in df['text']]
    df['sentiment_score'] = [r[0] for r in results]
    df['sentiment'] = [r[1] for r in results]
    return df
