import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=10,
    )["choices"][0]["text"]

