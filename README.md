# Sentiment Analyzer

An AI-based sentiment analyzer for product reviews and social media posts.

## Features
- Analyzes text as Positive / Negative / Neutral
- Shows confidence score
- Saves results to MongoDB
- Pie chart showing sentiment breakdown
- Recent analysis history table

## Technologies
- Python, Flask, Transformers (HuggingFace), MongoDB

## Setup

### 1. Install MongoDB
Download from: https://www.mongodb.com/try/download/community
Install and start MongoDB (it runs on port 27017 by default)

### 2. Clone the repo
```bash
git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
Go to: http://localhost:5000
