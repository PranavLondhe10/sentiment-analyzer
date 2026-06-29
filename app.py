from flask import Flask, render_template, request
from transformers import pipeline
from datetime import datetime

app = Flask(__name__)

# in-memory storage
history = []

# load model
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    result = analyzer(text[:512])[0]
    label = result["label"]
    score = round(result["score"] * 100, 2)
    if label == "POSITIVE":
        return "Positive", score
    elif label == "NEGATIVE":
        return "Negative", score
    else:
        return "Neutral", score

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("review")
        if text:
            sentiment, score = get_sentiment(text)
            entry = {
                "text": text,
                "sentiment": sentiment,
                "score": score,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            history.append(entry)
            result = entry

    pos = sum(1 for h in history if h["sentiment"] == "Positive")
    neg = sum(1 for h in history if h["sentiment"] == "Negative")
    neu = sum(1 for h in history if h["sentiment"] == "Neutral")

    return render_template("index.html", result=result, history=history[-10:][::-1], pos=pos, neg=neg, neu=neu)

if __name__ == "__main__":
    app.run(debug=True)
