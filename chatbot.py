import requests

# Your OpenAI API key
API_KEY = 'replace with your Open AI API Key'

# Endpoint for the ChatGPT API
API_URL = "replace with open AI API chat completions url"

def get_chat_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()

    if response.status_code == 200:
        return response_data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response_data.get('error', {}).get('message', 'Unknown error')}"

def main():
    print("ChatGPT Bot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_chat_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
