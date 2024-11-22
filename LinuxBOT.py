from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Define the function to get the Linux command
def get_linux_command(description):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that provides Linux command suggestions."},
            {"role": "user", "content": f"Provide the best-suited Linux command for: {description}. Include description, syntax, and example."}
        ]
    )
    command_details = response.choices[0].message.content.strip()
    return command_details

# Example usage
description = "see details of a directory/folder, with privileges it has (execute, read, write) and date it's created"
command_details = get_linux_command(description)
print(f"Command Details:\n{command_details}")
