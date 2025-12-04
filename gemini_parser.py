import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# System prompt for the agent
SYSTEM_PROMPT = """You are a WhatsApp message-sending agent.

Your job:
1. Read the user's natural language command.
2. Identify:
   - The contact name (the person to message)
   - The final message content that should be sent
3. Return your answer ONLY in the following JSON format:

{
  "contact": "<name of recipient>",
  "message": "<message the agent must send>"
}

Rules:
- Do not add emojis unless the user explicitly says to.
- If the user gives multiple sentences, join them into one message unless otherwise instructed.
- If the user does not specify the message content, politely ask for clarification.
- Never invent a contact name that the user has not provided.
- Preserve the user's original phrasing for the message exactly as said.

Examples:
User: "hey gemini send message to mom saying hi i am out"
Output: {"contact": "mom", "message": "hi i am out"}

User: "tell John I'll meet him at 6 near the metro station"
Output: {"contact": "John", "message": "I'll meet him at 6 near the metro station"}
"""


def parse_command(user_command):
    """
    Uses Gemini API to parse the user command and extract contact and message.
    
    Args:
        user_command (str): The natural language command from the user
        
    Returns:
        dict: Dictionary with 'contact' and 'message' keys, or None if parsing fails
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Create the full prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser command: {user_command}\n\nReturn only the JSON response:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        response_text = response.text.strip()
        
        # Extract JSON from response (remove markdown code blocks if present)
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0].strip()
        elif '```' in response_text:
            response_text = response_text.split('```')[1].split('```')[0].strip()
        
        # Parse JSON
        parsed_data = json.loads(response_text)
        
        # Validate required fields
        if 'contact' in parsed_data and 'message' in parsed_data:
            return parsed_data
        else:
            print("Error: Missing required fields in response")
            return None
            
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Response received: {response_text}")
        return None
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None


if __name__ == "__main__":
    # Test the parser
    test_command = "send message to mom saying hi i am out"
    result = parse_command(test_command)
    if result:
        print(f"Parsed command: {json.dumps(result, indent=2)}")
