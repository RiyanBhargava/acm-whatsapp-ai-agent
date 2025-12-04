import os
from gemini_parser import parse_command
from whatsapp_automation import WhatsAppAutomation


def main():
    """Main application loop"""
    print("=" * 60)
    print("WhatsApp AI Agent - Powered by Gemini & Selenium")
    print("=" * 60)
    print()
    
    # Check if API key is configured
    if not os.getenv('GEMINI_API_KEY'):
        print("ERROR: GEMINI_API_KEY not found in environment variables!")
        print("Please create a .env file with your API key.")
        print("See .env.example for reference.")
        return
    
    # Initialize WhatsApp automation
    print("Initializing WhatsApp automation...")
    wa = WhatsAppAutomation()
    wa.initialize_driver()
    
    # Open WhatsApp and wait for login
    if not wa.open_whatsapp():
        print("Failed to load WhatsApp Web. Exiting...")
        wa.close()
        return
    
    print()
    print("=" * 60)
    print("Agent is ready! You can now send messages.")
    print("Type your command in natural language.")
    print("Type 'quit' or 'exit' to stop the agent.")
    print("=" * 60)
    print()
    
    # Main command loop
    try:
        while True:
            # Get user command
            user_command = input("\nYou: ").strip()
            
            # Check for exit commands
            if user_command.lower() in ['quit', 'exit', 'q']:
                print("Shutting down agent...")
                break
            
            if not user_command:
                continue
            
            # Parse the command using Gemini
            print("Processing command...")
            parsed = parse_command(user_command)
            
            if not parsed:
                print("Could not understand the command. Please try again.")
                continue
            
            # Display what was understood
            print(f"\n→ Contact: {parsed['contact']}")
            print(f"→ Message: {parsed['message']}")
            
            # Ask for confirmation
            confirm = input("\nSend this message? (y/n): ").strip().lower()
            
            if confirm == 'y':
                # Send the message
                success = wa.send_message(parsed['contact'], parsed['message'])
                
                if success:
                    print("✓ Message sent successfully!")
                else:
                    print("✗ Failed to send message. Please check if the contact exists.")
            else:
                print("Message cancelled.")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Shutting down...")
    
    finally:
        # Clean up
        wa.close()
        print("Agent stopped. Goodbye!")


if __name__ == "__main__":
    main()
