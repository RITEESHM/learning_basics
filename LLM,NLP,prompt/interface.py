'''from textblob import TextBlob

text = """Horrible product. They charged me twice the price and it broke after a week. I will never buy from them again."""

# Create a TextBlob object
blob = TextBlob(text)

# Get the sentiment polarity
sentiment = blob.sentiment.polarity

# Determine the sentiment label
sentiment_label = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

print(sentiment_label)'''

'''from textblob import TextBlob

text = """I am so happy with this product. It is the best thing I have ever bought. I will definitely buy from them again."""

# Create a TextBlob object
blob = TextBlob(text)

# Get the sentiment polarity
sentiment = blob.sentiment.polarity

# Determine the sentiment label
sentiment_label = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

# Get the emotions
emotions = blob.sentiment_assessments.assessments

# Extract emotion words
emotion_words = [emotion[0] for emotion in emotions]

print(sentiment_label)
print(emotion_words)'''
import random

def generate_madlib(prepositions, verbs, nouns):
    # Choose random words from each array
    preposition = random.choice(prepositions)
    verb = random.choice(verbs)
    noun = random.choice(nouns)

    # Construct and return the madlib sentence
    madlib = f"The {noun} {verb} {preposition} the {noun}."
    return madlib

# Arrays of prepositions, verbs, and nouns
prepositions = ["on", "under", "beside", "inside", "outside", "above"]
verbs = ["jumped", "ran", "slept", "laughed", "cried", "danced"]
nouns = ["dog", "cat", "house", "tree", "car", "ball"]

# Generate and print madlibs
for _ in range(5):  # Generate 5 madlibs
    madlib = generate_madlib(prepositions, verbs, nouns)
    print(madlib)





