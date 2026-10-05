import ollama

from app.rag_service import retrieve_knowledge


def generate_ai_recommendation(conversation, intent, priority):

    knowledge = retrieve_knowledge(
        conversation,
        n_results=2
    )

    context = "\n\n".join(knowledge)

    prompt = f"""
You are an enterprise IT support intelligence assistant.

Analyze the employee IT support request using the provided
enterprise IT knowledge base.

Employee request:
{conversation}

Detected issue category:
{intent}

Priority:
{priority}

Relevant knowledge base:
{context}

Return ONLY the following format:

Recommendation:
<2-3 concise sentences describing practical troubleshooting steps based primarily on the knowledge base>

Support Team:
<the most appropriate IT support team based on the knowledge base>

Rules:
- Use the provided knowledge base as the primary source.
- Do not write an email.
- Do not use greetings or sign-offs.
- Do not include a subject line.
- Do not use placeholders.
- Do not invent company-specific policies.
- Keep the recommendation professional and actionable.
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
