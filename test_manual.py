from classifier import load_prompt, classify_email

prompt = load_prompt("v1")

result = classify_email(
    "Hi, I was charged twice for my subscription last month and need a refund.",
    prompt
)

print(f"Category: {result.category}")
print(f"Summary: {result.summary}")