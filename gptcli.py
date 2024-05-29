import os
import openai
import argparse
from dotenv import load_dotenv



def main() -> None:
    '''
    Ask ChatGPT a question and print the response to your terminal
    '''

    parser = argparse.ArgumentParser(usage=f'gptcli "prompt"', description="Ask ChatGPT a question and print the response to your terminal")
    parser.add_argument('prompt', metavar='prompt', type=str, help='Enter your prompt')
    args = parser.parse_args()
    prompt = args.prompt

    try:
        # Load environment variables from .env file
        load_dotenv()

        # Ensure your API key is loaded from the environment variable
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Choose the model
        model_choice = "gpt-4",

        # Send the prompt to the model
        response = openai.Completion.create(
            engine=model_choice,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=64,
            top_p=1
        )

        # Print the response
        print(response.choices[0].text.strip())
    except Exception as exc:
        print(f"Error: {exc.args}")

    return None


if __name__ == "__main__":
    main()