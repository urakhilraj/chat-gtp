import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")