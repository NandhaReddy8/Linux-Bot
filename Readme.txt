Step 1: Install python-dotenv
First, make sure you have the python-dotenv library installed. In your Colab environment, run:

Step 2: Create a .env File
In your project directory (for example, in Google Colab), you can create a .env file with the following content:

OPENAI_API_KEY=your-openai-api-key
Replace your-openai-api-key with your actual OpenAI API key.

Step 3: Update the Python Script to Load the API Key from .env

Summary:
Create a .env file with your OpenAI API key.

Install python-dotenv to load environment variables from the .env file.

Update your script to use the API key from the .env file.