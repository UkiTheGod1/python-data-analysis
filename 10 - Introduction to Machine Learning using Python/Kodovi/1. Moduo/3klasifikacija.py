import pandas as pd
 
positive_words = ["great", "excellent", "amazing", "love", "perfect", "good", "fantastic", "happy", "recommend"]
negative_words = ["bad", "terrible", "worst", "broken", "poor", "disappointed", "awful", "hate", "slow"]
 
def classify_sentiment(text):
    text = str(text).lower()
    pos_hits = sum(word in text for word in positive_words)
    neg_hits = sum(word in text for word in negative_words)
 
    if pos_hits >= neg_hits:
        return "positive"
    else:
        return "negative"
    
df = pd.read_csv("reviews_labeled_cleaned.csv")

df['predicted_sentiment'] = df['review'].apply(classify_sentiment)
 
df.to_csv("reviews_with_predicted_sentiment.csv", index=False)

print(df[['review', 'sentiment', 'predicted_sentiment']].head(20))