from app.recommender import get_recommendation


INTENT_KEYWORDS = {
    "Hardware Issue": [
        "laptop",
        "desktop",
        "screen",
        "monitor",
        "printer",
        "restarting"
    ],
    "Password / Account Access": [
        "password",
        "account is locked",
        "login",
        "locked"
    ],
    "Email / Outlook": [
        "outlook",
        "email",
        "corporate email"
    ],
    "VPN Issue": [
        "vpn",
        "authentication failed",
        "disconnecting"
    ],
    "Network / Wi-Fi": [
        "wi-fi",
        "wifi",
        "network"
    ],
    "Access / Permissions": [
        "permission",
        "permissions",
        "shared drive"
    ],
    "Software Installation": [
        "install",
        "installed",
        "microsoft teams"
    ],
    "MFA / Authentication": [
        "mfa",
        "authentication"
    ],
    "Performance Issue": [
        "slow",
        "taking several minutes",
        "performance"
    ]
}


def detect_intent(text):
    text_lower = text.lower()
    scores = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = 0

        for keyword in keywords:
            if keyword in text_lower:
                score += 1

        scores[intent] = score

    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return "General IT Support"

    return best_intent


def detect_sentiment(text):
    negative_words = [
        "not working",
        "cannot",
        "can't",
        "error",
        "failed",
        "slow",
        "problem",
        "issue",
        "unable",
        "disconnecting",
        "locked"
    ]

    text_lower = text.lower()

    negative_count = sum(
        word in text_lower
        for word in negative_words
    )

    if negative_count >= 2:
        return "Very Negative"

    if negative_count == 1:
        return "Negative"

    return "Neutral"


def determine_priority(intent, text):
    text_lower = text.lower()

    high_priority_keywords = [
        "important meeting",
        "cannot access",
        "account is locked",
        "authentication failed",
        "cannot work",
        "not working"
    ]

    for keyword in high_priority_keywords:
        if keyword in text_lower:
            return "High"

    if intent in [
        "VPN Issue",
        "MFA / Authentication",
        "Password / Account Access",
        "Access / Permissions"
    ]:
        return "High"

    return "Medium"


def generate_summary(text):
    return "Employee reported an IT issue: " + text


def analyze_call(text):
    intent = detect_intent(text)
    sentiment = detect_sentiment(text)
    priority = determine_priority(intent, text)
    summary = generate_summary(text)
    recommendation = get_recommendation(intent)

    return {
        "summary": summary,
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "recommendation": recommendation["action"],
        "queue": recommendation["queue"]
    }