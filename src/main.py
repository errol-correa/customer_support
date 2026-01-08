import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import prompts  # Importing our prompt library

# Load environment variables
load_dotenv()


def run_support_generator():
    # Configuration
    # Note: API Version is hardcoded here instead of .env as requested
    API_VERSION = "2024-02-01"

    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=API_VERSION
    )

    # Part 2: Define dynamic inputs
    inputs = {
        "product_name": "LaraTech Cloud",
        "issue_type": "Billing Discrepancy",
        "tone": "formal and empathetic",
        "customer_query": "I noticed a $50 charge on my account that I didn't authorize. I want a refund immediately!"
    }

    # Inject variables into the prompt template
    formatted_prompt = prompts.SUPPORT_TEMPLATE_1.format(**inputs)

    print("--- Sending Prompt to Azure OpenAI ---")

    try:
        # Part 3: API Call
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system",
                 "content": "You are an enterprise AI component that follows strict formatting constraints."},
                {"role": "user", "content": formatted_prompt}
            ],
            temperature=0.3,  # Low temperature for professional consistency
            max_tokens=200
        )

        # Print the response
        print("\nGenerated Response:\n")
        print(response.choices[0].message.content.strip())
        print("\n--- End of Response ---")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_support_generator()