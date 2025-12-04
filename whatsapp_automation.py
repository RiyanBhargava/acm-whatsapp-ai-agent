import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WhatsAppAutomation:
    """Handles WhatsApp Web automation using Selenium"""
    
    def __init__(self):
        """Initialize the Chrome WebDriver"""
        self.driver = None
        
    def initialize_driver(self):
        """Set up Chrome WebDriver with options"""
        chrome_options = Options()
        
        # Create absolute path for user data directory
        import os
        user_data_dir = os.path.abspath("./chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        
        # Additional options to prevent crashes
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        
    def open_whatsapp(self):
        """Open WhatsApp Web and wait for QR scan"""
        print("Opening WhatsApp Web...")
        self.driver.get("https://web.whatsapp.com/")
        
        print("Please scan the QR code to log in...")
        print("Waiting for WhatsApp to load...")
        
        try:
            # Wait for the main chat interface to load (indicating successful login)
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            print("WhatsApp loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading WhatsApp: {e}")
            return False
    
    def send_message(self, contact_name, message):
        """
        Send a message to a specific contact on WhatsApp
        
        Args:
            contact_name (str): Name of the contact
            message (str): Message to send
            
        Returns:
            bool: True if message sent successfully, False otherwise
        """
        try:
            # Search for contact
            print(f"Searching for contact: {contact_name}")
            
            # Click on search box
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.click()
            time.sleep(0.5)
            
            # Type contact name
            search_box.send_keys(contact_name)
            time.sleep(1)
            
            # Click on the contact
            contact = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]'))
            )
            contact.click()
            time.sleep(1)
            
            # Find message input box
            message_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            
            # Type and send message
            print(f"Sending message: {message}")
            message_box.click()
            message_box.send_keys(message)
            time.sleep(0.5)
            message_box.send_keys(Keys.RETURN)
            
            print("Message sent successfully!")
            return True
            
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            print("Browser closed.")


if __name__ == "__main__":
    # Test the automation
    wa = WhatsAppAutomation()
    wa.initialize_driver()
    
    if wa.open_whatsapp():
        input("\nPress Enter after WhatsApp is loaded to test sending a message...")
        
        # Test sending a message
        contact = input("Enter contact name: ")
        message = input("Enter message: ")
        
        wa.send_message(contact, message)
        
        input("\nPress Enter to close the browser...")
    
    wa.close()
