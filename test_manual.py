from classifier import load_prompt, classify_email

prompt = load_prompt("v1")

result = classify_email(
    "I want to cancel my account because I keep getting charged for a plan I never signed up for",
    prompt
)

print(f"Category: {result.category}")
print(f"Summary: {result.summary}")