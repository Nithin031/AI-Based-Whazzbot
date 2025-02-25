## Prerequisites

Before working on this project, ensure you have the following:

- **VS Code** installed on your system.
- **Python** installed (latest stable version recommended).
- At least **1GB of free storage** for dependencies and execution.

## Setting Up Git

You'll need Git installed to clone and contribute to this project. Follow this tutorial to install Git:  
🔗 [Git Installation Guide](https://youtu.be/JgOs70Y7jew?si=RihQAaJQiYkAoxnb)

If you're new to Git and GitHub, check out these videos to get started:  

- 📌 [Git & GitHub Basics](https://youtu.be/HkdAHXoRtos?si=JMK7J6WVxL5bQNK9)  
- 📌 [Git Commands & Workflow](https://youtu.be/mJ-qvsxPHpY?si=IkgX_lTHcQjt696Q)

## To Clone the Repository into Your PC

Run the following command by opening a terminal in the required directory:

```sh
git clone <https://github.com/Nithin031/AI-Based-Whazzbot>
```

To open a terminal in a required directory, first navigate to the directory, then perform a right-click and click on **Open in Terminal**.

## Setting Up the Virtual Environment  

1. Open **VS Code**.  
2. Click on **File → Open Folder** and select the folder where you cloned the repository.  
3. Click on the `Assistant.py` file.
4. Open the **Terminal** in VS Code (**View → Terminal** or press ``Ctrl + ` ``).  
5. Run the following command to create a virtual environment:

```
py -m venv venv
venv\Scripts\activate
```
## Select a Python Interpreter

### Select the Right Python Interpreter in VS Code

1. Press `Ctrl+Shift+P` (Command Palette)
2. Search for **"Python: Select Interpreter"**
3. Choose the one with **venv** (recommended)

This ensures all required packages are installed inside the virtual environment, avoiding global Python issues.

---

## Set Execution Policy (Windows Only)
If you're using PowerShell, you may need to allow script execution:

Run the following command in the VS Code terminal:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
If prompted, type **Y** and press Enter.

---

## Troubleshooting pip Installation Issues

If `pip install` fails, try the following:

- **Disable any external antivirus** (like Avast or McAfee) temporarily, as it may block installations.
- Ensure you are running the terminal **as Administrator** (Windows users).
- Try upgrading `pip` before installing packages:
  ```bash
  py -m pip install --upgrade pip
  ```

---

## Install Dependencies
Run the following command:
```bash
pip install -r requirements.txt
```

---

## Get Chrome User Data Path and Paste in Code

### Why is this necessary?
Since you will be using **WhatsApp Web**, logging in manually every time can be time-consuming. By using the **Chrome User Data Path**, Selenium will open Chrome with your existing login session, so you won’t need to scan the QR code each time.

### Step 1: Find Your Chrome User Data Path
1. Open Google Chrome.
2. In the address bar, type:
   ```
   chrome://version/
   ```
   and press **Enter**.
3. Look for **Profile Path**.
   - It will look something like this: `C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data`
   - Copy this path and update the blank **User Data Path** in your code.

---

## Setting Up LLaMA 3-70B Instruct

### Why LLaMA 3?
- **High-Performance AI**: LLaMA 3-70B is one of the most powerful open-source models, optimized for chat-based applications.
- **Enhanced Context Retention**: Provides better long-term memory, ensuring continuity in conversations.
- **Cost-Efficient**: Eliminates reliance on expensive third-party APIs. *(But you can process up to 50 free requests a day!)*
- **Customizability**: Can be fine-tuned for specific use cases and industries.

### Steps to Set Up LLaMA 3-70B Instruct

1. **Access the Model on GitHub Marketplace**
   - Meta provides LLaMA models via GitHub. Get it from:
     🔗 [GitHub Marketplace - LLaMA 3](https://github.com/marketplace/models/azureml-meta/Llama-3-3-70B-Instruct)

2. **Get an API Key**
   - Click on **"Get API Key"** on the page.
   - Click on **"Get Developer Key"**.
   - You will be redirected to a page where you need to click **"Generate New Token"** → **"Generate New Token (Classic)"**.
   - Give a name to the token and generate it.

⚠️ **Important:** Copy the token immediately, as it will only be shown once!

✅ **No special permissions needed**—just generate and use it.

---

## Setting the API Token in VS Code Terminal

To store your API token securely, follow these steps in the VS Code terminal (inside the project directory):

### **Permanently Store the API Token in Windows (PowerShell & VS Code Terminal)**
Run the following command in PowerShell:
```powershell
[System.Environment]::SetEnvironmentVariable("LLAMA3_API_KEY", "your-token-here", "User")
```
⚠️ Replace `"your-token-here"` with your actual API key.

### **Verify the Token is Set**
Restart VS Code and run:
```bash
py LLAMA_KEY.py
```
If the token appears, it’s successfully stored. 🎉

If this does not work, try this alternative method:

#### **Alternative Method (PowerShell in VS Code)**
```powershell
$env:LLAMA3_API_KEY="your-token-here"
```
Again, replace `"your-token-here"` with your actual token.

Restart VS Code and check again.

📌 **Note:** If none of these methods work, try searching on the web for your OS-specific solution.

---

## 🎉 You're All Set!
If you've followed all the steps correctly, you can now run your code without any issues. 

Happy coding! 😃🚀

---

## 💡 We Value Your Feedback!
Your input matters! Once the `Feedback.py` script is released, make sure to share your thoughts and suggestions. 📢

Stay tuned for updates, and thank you for being a part of this journey! 🚀😊
