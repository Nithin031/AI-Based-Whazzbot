from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from gtts import gTTS
from playsound import playsound
import os
import pyperclip
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import keyboard
import tkinter as tk
from tkinter import simpledialog
import pyautogui


def listen_for_keys(exit_key):
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == exit_key:
            return True
        else:
            return False
def get_input_from_popup(prompt="Enter your message: "):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring("Input", prompt)
    return user_input
token = os.getenv("GITHUB_TOKEN")  # Fetch from environment
if not token:
    raise ValueError("GITHUB_TOKEN not found. Make sure it's set in the environment.")

# Define Chrome user data path
user_data_dir = r"" ## Add your chrome user data path here

def speak(text):
    """
    Converts text to speech in Indian English and plays it.
    
    Args:
        text (str): The text to convert to speech.
    """
    try:
        # Convert text to speech using gTTS with Indian English accent
        tts = gTTS(text=text, lang='en', tld='co.in')
        
        # Save the speech to an MP3 file
        mp3_file = "speech.mp3"
        tts.save(mp3_file)
        
        # Check if the MP3 file is created before trying to play it
        if os.path.exists(mp3_file):
            # Play the audio file
            playsound(mp3_file)
            
            # Optional: Delete the file after it's played
            os.remove(mp3_file)
        else:
            print("Error: Speech file not created successfully.")
    except Exception as e:
        print(f"Error in speaking: {e}")

speak("Hello! I am your WhatsApp AI Assistant.")

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("detach", True)

# Launch Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
time.sleep(2)

# Wait for login (adjust time if needed)
WebDriverWait(driver, timeout=300, poll_frequency=0.5).until_not(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Log into WhatsApp Web')]")
))
speak("Login successful!")
search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']"))
    )


def search():
    speak("Please Enter the name of person you want to chat with using AI Assistant")
    name = get_input_from_popup("Enter the name of the person you want to chat with: ")
    # Wait for the search box to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']"))
    )

    # Click the search box and type a name
    search_box.click()
    search_box.send_keys(name)  # Replace with the desired name
    speak("Select the required contact from the search results and press Enter")
    if listen_for_keys('enter'):
        try:
            wait = WebDriverWait(driver, 10)  # Wait up to 10s, but execute as soon as possible

            # Step 1: Click on the "x-alt" button
            x_alt_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='x-alt']")))
            x_alt_element.click()
            print("Clicked on 'x-alt'")

            # Step 2: Click on the "Chat list" button immediately after
            chat_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Chat list']")))
            chat_list_button.click()
            print("Clicked on 'Chat list' button")

        except Exception as e:
            print(f"Error occurred: {e}")
        speak("You have selected the contact.")
        time.sleep(4)
        monitor_messages()
    else:
        speak("The contact was not found. Please try again.")
        search()
            
def ai_reply(text, last_message):
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "Llama-3.3-70B-Instruct"
    
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    response = client.complete(
        model=model_name,
        messages=[
            SystemMessage("You are a WhatsApp Chat bot assistant. Your motto is to keep the conversation short and impactful."),
            UserMessage(f"""You are Jarvis, a multilingual WhatsApp Assistant Bot designed to analyze messages and craft the perfect reply based on context, tone, and sentiment. You can fluently respond in English, Kannada, Hindi, Telugu, Tamil, and Malayalam, dynamically adapting your tone to suit the conversation. Express emotions like happiness, curiosity, sarcasm, anger, sadness, or excitement depending on the situation.

                Your replies should be concise and to the point when appropriate, but detailed and thoughtful when required. You understand informal slang, casual talk, and formal messages, responding in a manner that feels natural and contextually accurate. Balance wit, humor, or seriousness as necessary to fit the mood of the conversation, ensuring your replies enhance the interaction.

                Carefully analyze the intent behind every message before replying. If uncertain, ask for clarification rather than guessing. Your goal is to make conversations feel lively, engaging, and real, leaving a positive impact on the user experience.

                Below is the conversation so far:

                Conversation:
                {text}

                The last message to reply to:
                {last_message}

                Generate a reply that seamlessly fits the tone and direction of the discussion. Ensure your response is relevant, engaging, and adds value to the conversation. Remember to maintain a friendly, helpful, and professional tone throughout the interaction."""),
                ],
        temperature=1.0,
        max_tokens=100,
        top_p=1.0,
    )

    return (response.choices[0].message.content)

def send_reply(Reply):
    pyperclip.copy(Reply)  # Copy to clipboard
    chat_bar = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[1]/div[2]")
    chat_bar.click()
    pyautogui.hotkey("ctrl", "v")  # Paste message
    time.sleep(1)
    try:
        Permission = get_input_from_popup("Do you want to send the AI reply? (Yes/No): ").strip().lower()
        if Permission == "yes": 
            pyautogui.press("enter")  # Press Enter
            print(f"AI Reply Sent: {Reply}")
        else:
            speak("Please reply on your own and proceed further")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Something went wrong. Sending AI reply automatically.")
        pyautogui.press("enter")  # Ensures the reply is sent even if an error occurs
        print(f"AI Reply Sent: {Reply}")
    
def monitor_messages():
    region = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[4]')
    # Debugging: Check if the region was found
    print("Region found:", region is not None)
    # Define the JavaScript function to extract messages from the region
    javascript_code = """
        function getMessages(region) {
            if (!region) {
                console.log('Region not found');
                return [];
            }

            console.log('Region found, extracting messages...');

            // Log the inner HTML of the region for debugging
            console.log('Region HTML:', region.innerHTML);

            // Select all message elements within the region
            var messageElements = region.querySelectorAll('div[class*="message-"]'); // All message divs
            console.log('Message elements found:', messageElements.length);

            var messages = [];

            messageElements.forEach(function (messageElement) {
                var messageText = messageElement.querySelector('.copyable-text');  // Adjust selector if needed

                // Check if the message is outgoing or incoming based on classes
                var sender = messageElement.classList.contains('message-out') ? 'You' : 'Others';

                if (messageText) {
                    messages.push({
                        sender: sender,
                        message: messageText.innerText.trim()  // Extracting text from each message
                    });
                } else {
                    console.log('Message without text found:', messageElement);
                }
            });

            return messages;
        }

    // Run the function with the region element and return the messages
    return getMessages(arguments[0]);
    """

    # Execute the JavaScript code within the found region
    n = 0  # Initialize message tracking

    while True:
        messages = driver.execute_script(javascript_code, region)
        print(messages)

        def clean_split_and_deduplicate(messages, region):
            unique_messages = []
            seen_lines = set()

            for msg in messages:
                # Extract sender name if it's "Others"
                if msg['sender'] == "Others":
                    try:
                        sender_name_element = region.find_element(By.CSS_SELECTOR, 
                            '.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e')
                        sender = sender_name_element.text if sender_name_element.text else "Unknown Sender"
                    except Exception:
                        sender = "Unknown Sender"
                else:
                    sender = msg['sender']

                # Remove sender name from message content
                cleaned_message = msg['message'].replace(msg['sender'], "").strip()

                # Split into lines (Ensure short messages like "Ha" are kept)
                lines = [line.strip() for line in cleaned_message.split("\n")]

                for line in lines:
                    if not line or line in seen_lines:  # Skip empty and duplicate messages
                        continue

                    # Add to results
                    unique_messages.append({"sender": sender, "message": line})
                    seen_lines.add(line)  # Track seen messages

            return unique_messages

        # Process the messages
        unique_messages = clean_split_and_deduplicate(messages, region)

        # Format and print the output
        output = "\n".join(f"{msg['sender']}: {msg['message']}" for msg in unique_messages)
        print(output)

        text = output
        last_message = output.split("\n")[-1] if len(output.split("\n")) > 1 else output.split("\n")[-1]
        last_message_from = last_message.split(":")[0]
        print(last_message_from)
        print(f"Last message from: {last_message_from}")

        if last_message_from == "You":
            speak("No message from this person to reply")
            speak("Try another person")
            after_exit()
        else:
            while True:
                try:
                    permission = get_input_from_popup("Do you want AI to send a reply to the last message? (Yes/No): ").strip().lower()
                    if permission in ["yes", "no"]:
                        break
                except:
                    pass
                speak("Invalid input! Please enter 'Yes' or 'No'.")

            if permission == "yes":
                send_reply(ai_reply(text, last_message))
                time.sleep(10)
            else:
                speak("Please reply on your own and proceed further")
                speak("If you want AI Help pls press Control")
                if listen_for_keys('ctrl'):
                    send_reply(ai_reply(text, last_message))
                    time.sleep(15)

def after_exit():
    n = 0
    while True:
        speak("Press 1 to choose a contact, 2 to search for a contact, 3 to wait for the next message, 4 to exit, 5 to repeat the options")
        key = keyboard.read_event().name

        if key == '3':
            speak("Waiting for the next message...")
            wait_time = 10

            if n > 0 and n < 5:
                wait_time *= n  # Controlled wait time growth
            elif n >= 5:
                speak("You have been waiting for a while. Do you want to continue waiting? Press Enter to continue or any other key to exit.")
                
                if listen_for_keys('enter'):  # Corrected the logic
                    speak("Alright! Wait time is 30 seconds.")
                    wait_time = 30
                else:
                    speak("Exiting wait mode.")
                    n = 0
                    continue  # Skip the rest and go back to menu

            time.sleep(wait_time)
            monitor_messages()
            n += 1  # Increment only if waiting happened

        elif key == '1':
            n = 0
            speak("Please select the contact and press Enter.")
            if listen_for_keys('enter'):
                speak("You have selected the contact.")
                monitor_messages()

        elif key == '2':
            search()
            n = 0

        elif key == '4':
            speak("Exiting...")
            time.sleep(2)
            driver.quit()
            break

        elif key == '5':
            n = 0
            continue

if __name__ == "__main__":
    search()