# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

# Define the app
app = FastAPI()

# Define the data format we expect (Input)
class Sentence(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Mood Detector API is running!"}

@app.post("/predict")
def predict_sentiment(data: Sentence):
    # ML Logic: Analyze the text
    analysis = TextBlob(data.text)
    polarity = analysis.sentiment.polarity

    # determine label
    if polarity > 0:
        mood = "Positive"
    elif polarity < 0:
        mood = "Negative"
    else:
        mood = "Neutral"

    return {
        "text": data.text,
        "score": polarity,
        "mood": mood
    }