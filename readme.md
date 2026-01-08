# Customer Support Response Generator

Enterprise prompt-based AI system designed to generate professional, safe, and structured customer support responses using Azure OpenAI.

## Project Structure
* `src/main.py`: Main application logic and API integration.
* `src/prompts.py`: Reusable, parameterized prompt templates.
* `.env`: Environment variables for API security.

## Setup
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Create a `.env` file in the root directory:
   ```env
   AZURE_OPENAI_KEY="your_api_key"
   AZURE_OPENAI_ENDPOINT="your_endpoint"
   AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name"
   ```

## Usage
Run the generator using Python:
```bash
python src/main.py
```

## Features
* **Constraint Enforcement:** Ensures responses are professional, calm, and avoid legal/financial advice.
* **Parameterized Prompts:** Supports dynamic inputs for product name, issue type, tone, and customer query.
* **Enterprise Design:** Built as a reusable component rather than a casual chatbot.