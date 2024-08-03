import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "diskription about pengwin "}])
print(completion.choices[0].message.content)