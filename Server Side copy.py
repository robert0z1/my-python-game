import openai
openai.api_key = "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"
while True:
    prompt = input("You: ")
    model = "GPT-3"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024)

    print("AI: " + response.choices[0].text)
