"""
This module performs basic sentiment analysis on input text.
"""

def sentiment_analyzer(text):
    """
    Analyze sentiment of the given text.
    Returns sentiment label and score.
    """
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be string")

        if text.strip() == "":
            raise ValueError("Input text cannot be empty")

        text = text.lower()

        positive_words = ["good", "great", "excellent", "happy", "love", "amazing"]
        negative_words = ["bad", "worst", "terrible", "sad", "hate", "awful"]

        score = 0

        for word in positive_words:
            if word in text:
                score += 1

        for word in negative_words:
            if word in text:
                score -= 1

        if score > 0:
            sentiment = "Positive"
            confidence = "high"
        elif score < 0:
            sentiment = "Negative"
            confidence = "medium"
        else:
            sentiment = "Neutral"
            confidence = "low"

        return {
            "sentiment": sentiment,
            "confidence": confidence,
            "score": score
        }

    except Exception as e:      # pylint: disable=broad-exception-caught
        # Business logic error
        return {
            "sentiment": "Unknown",
            "score": 0,
            "confidence": 0,
            "error": str(e)
        }
