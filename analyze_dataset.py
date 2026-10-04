import csv
from app.llm_service import analyze_call

with open("data/sample_calls.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        result = analyze_call(row["conversation"])

        print("\n" + "=" * 70)
        print(f"Ticket #{row['call_id']}")
        print(f"Conversation: {row['conversation']}")
        print(f"Intent:      {result['intent']}")
        print(f"Sentiment:   {result['sentiment']}")
        print(f"Priority:    {result['priority']}")
        print(f"Summary:     {result['summary']}")
        print(f"Recommendation: {result['recommendation']}")
        print(f"Queue:          {result['queue']}")

