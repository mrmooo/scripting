import openai
openai.api_key = "KEY"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Write me a creative and hilarious story about cow or moo related topics. Don't exceed 3 sentences"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)