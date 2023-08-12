import openai  # You need to install the OpenAI Python package
from fastapi import FastAPI

app = FastAPI()

# Set your OpenAI API key
openai.api_key = "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"


@app.get("/")
def read_root():
    return {"message": "Welcome to Dish Suggestion API"}


@app.get("/suggest_dishes/")
def suggest_dishes(ingredients: str):
    prompt = f"Given the ingredients: {ingredients}, suggest a dish."

    # Use the OpenAI model for dish prediction
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the relevant GPT-3 engine
        prompt=prompt,
        max_tokens=50  # Adjust the response length as needed
    )

    suggested_dish = response.choices[0].text.strip()

    return {"suggested_dish": suggested_dish}
