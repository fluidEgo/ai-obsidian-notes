# AI-Powered Obsidian Note Automation

## 📋 Description

This project provides a script to automate the creation of well-structured, intelligently-linked notes within an Obsidian vault directly from clipboard content. It leverages Google's Gemini API to perform semantic analysis on the clipboard text, automatically generating Markdown-formatted notes with relevant wikilinks to existing concepts in your vault.

This tool is particularly beneficial for:

  * **Students** managing academic notes and Data Structures & Algorithms (DSA) problems.
  * **Researchers** organizing literature reviews and research papers.
  * **Developers** building technical documentation and personal knowledge bases.
  * **All Obsidian users** seeking to enhance their knowledge management workflow.

## 🚀 Core Features

  * **Clipboard Integration**: Captures content from any source via the system clipboard (Ctrl+C).
  * **Recursive Vault Scanning**: Indexes all existing notes across your vault's folders and subfolders to build a linking context.
  * **Semantic Linking**: The AI identifies conceptual relationships and links to related notes, moving beyond simple keyword matching.
  * **Model Fallback System**: Automatically cycles through a list of API models if a primary model's quota is exceeded, maximizing uptime.
  * **Markdown Formatting**: Generates properly structured notes with appropriate headers, lists, and code blocks.
  * **Efficient Performance**: Utilizes the cloud API for rapid note generation, typically within 2-5 seconds.
  * **Cross-Platform**: Fully compatible with Windows, macOS, and Linux.

## 🔧 Installation & Setup

### Prerequisites

  * Python 3.7 or later
  * A Google account (for generating a Gemini API key)
  * An existing Obsidian vault

### Step 1: Clone the Repository

```bash
git clone https://github.com/fluidEgo/ai-obsidian-notes.git
cd ai-obsidian-notes
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Obtain a Gemini API Key

1.  Navigate to [Google AI Studio](https://aistudio.google.com/).
2.  Sign in with your Google account.
3.  Select **"Get API Key"** and then **"Create API Key"**.
4.  Copy the generated API key to your clipboard.

### Step 4: Configure the Script

1.  Create a local configuration file from the template:
    ```bash
    cp config_template.py config.py
    ```
2.  Edit the new `config.py` file with your specific details:
    ```python
    VAULT_PATH = r"C:\Users\YourName\Documents\ObsidianVault"  # Example for Windows
    # VAULT_PATH = "/Users/yourname/Documents/ObsidianVault" # Example for macOS/Linux

    GEMINI_API_KEY = "your-actual-api-key-here"
    ```

**⚠️ Important:** Never commit your `config.py` file to version control. The repository's `.gitignore` file is already configured to exclude it.

## 📖 Usage

### Basic Operation

1.  **Copy content** you wish to convert into a note from any application (e.g., a web browser, IDE, or PDF).
2.  **Run the script** from your terminal:
    ```bash
    python make_gemini_note.py
    ```
3.  **Observe the output**. A new, contextually-linked note will be generated in your specified vault directory.

### Example Workflow

```bash
# User copies a LeetCode problem statement to the clipboard
# User runs the script in their terminal
$ python make_gemini_note.py

# Script output:
# Trying model: models/gemini-2.5-pro...
# ✓ Success with models/gemini-2.5-pro
# ✓ Note created: C:\Users\YourName\ObsidianVault\Two Sum Problem.md
```

The resulting note (`Two Sum Problem.md`) will feature:

  * A descriptive title.
  * Structured sections for the problem, solution, and analysis.
  * Automatic wikilinks to related notes, such as `[[Arrays]]`, `[[Hash Tables]]`, and `[[Time Complexity]]`.

## 🎯 Example Use Cases

### For Students

  * Convert DSA problems from platforms like LeetCode into organized notes.
  * Capture lecture content or slides and automatically link to core concepts.
  * Build an interconnected study guide where topics are linked semantically.

### For Researchers

  * Create literature notes from paper abstracts with automatic cross-referencing.
  * Link methodologies, findings, and authors across multiple studies.
  * Develop a comprehensive research knowledge graph.

### For Developers

  * Document code snippets and link them to relevant API documentation or libraries.
  * Organize technical articles and tutorials into a personal wiki.
  * Maintain interconnected notes on system architecture and design patterns.

## ⚙️ Configuration Details

### Vault Path

Ensure the `VAULT_PATH` in `config.py` uses the correct format for your operating system.

  * **Windows**: Use a raw string literal: `r"C:\Path\To\Vault"`
  * **macOS/Linux**: Use a standard string: `"/Users/yourname/Vault"`

### Model Priority List

The script attempts to use models in the order specified in `MODEL_LIST`. If a request fails (e.g., due to rate limiting), it automatically tries the next model.

```python
MODEL_LIST = [
    "models/gemini-2.5-pro",        # Highest quality, largest context
    "models/gemini-2.5-flash-lite", # Fast and efficient
    "models/gemini-2.5-flash",      # Balanced
    "models/gemini-2.0-flash-lite", # Lighter alternative
    "models/gemini-2.0-flash",      # Standard fallback
    "models/gemini-pro-latest"      # General availability
]
```

## 📊 API & Rate Limits (Free Tier)

The free tier for the Gemini API generally includes:

  * **25 requests per day** (per model)
  * **5 requests per minute**

The built-in model fallback system helps maximize this free quota by distributing requests across the different available models.

## 🛠️ Troubleshooting

### "Error: config.py not found\!"

You must create the `config.py` file from the template.

```bash
cp config_template.py config.py
```

Then, edit `config.py` to add your API key and vault path.

### "Error: Clipboard is empty\!"

  * Ensure you have successfully copied text to your clipboard before running the script.
  * Check your system's security settings to ensure Python has permission to access clipboard data.

### "All models failed"

  * Verify that your `GEMINI_API_KEY` in `config.py` is correct.
  * Check your [Google AI Studio dashboard](https://aistudio.google.com/) to see if you have exceeded your daily quota for all models.
  * You may need to wait 24 hours for the free quota to reset.

### "ModuleNotFoundError"

Ensure all required packages are installed.

```bash
pip install --upgrade google-generativeai pyperclip
```

### File Encoding Issues

  * The script defaults to UTF-8 encoding, which supports international characters and technical symbols.
  * Ensure your source text and Obsidian vault are also configured for UTF-8.

## 🏗️ Project Structure

```
ai-obsidian-notes/
├── make_gemini_note.py     # The main executable script
├── config_template.py      # Configuration template
├── requirements.txt        # Python dependencies
├── README.md               # This documentation file
├── LICENSE                 # Project license
└── .gitignore              # Ensures config.py and other files are not tracked
```

## 🔒 Privacy & Security

  * Your clipboard content is transmitted to Google's Gemini API for processing.
  * Your API key is stored locally in `config.py` and should **never** be shared or committed to version control.
  * The `.gitignore` file is pre-configured to prevent accidental uploading of `config.py`.
  * For highly sensitive information, consider using local, self-hosted LLM alternatives.

## 🚀 Advanced Customization

### Customizing the System Prompt

You can modify the AI's behavior by editing the `prompt` variable within `make_gemini_note.py`:

```python
prompt = f"""
You are an AI note-taking assistant for an Obsidian vault.
[Your custom instructions here, e.g., "Always include a 'Summary' section."]
"""
```

### Example Keyboard Shortcut Integration (Optional)

**Windows (using AutoHotkey):**
Create a `.ahk` script with the following:

```ahk
^!n:: ; Binds to Ctrl+Alt+N
Run, python C:\path\to\ai-obsidian-notes\make_gemini_note.py
return
```

**macOS (using Automator):**

1.  Open Automator and create a new "Quick Action".
2.  Set "Workflow receives" to "no input".
3.  Add a "Run Shell Script" action.
4.  Enter the following, updating the paths:
    ```bash
    cd /path/to/ai-obsidian-notes && python3 make_gemini_note.py
    ```
5.  Save the Quick Action (e.g., "Create Gemini Note") and assign it a keyboard shortcut in `System Settings > Keyboard > Keyboard Shortcuts > Services`.

## 🤝 Contributing

Contributions to this project are welcome. Please feel free to:

  * Report bugs or issues.
  * Suggest new features or enhancements.
  * Submit pull requests with improvements.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

## 🎓 Academic Project

This was developed as a **B.Tech (AI\&DS) Mini Project** for the **Computational Thinking** course (23AID101).

  * **Institution**: Amrita Vishwa Vidyapeetham, Nagercoil Campus
  * **Department**: Artificial Intelligence and Data Science
  * **Semester**: I

## 🙏 Acknowledgments

  * The Google Gemini API team for providing powerful semantic models.
  * The Obsidian community for its inspiration and robust platform.
  * The Python Software Foundation and community for essential libraries.

## 📧 Contact

Created by [fluidEgo](https://github.com/fluidEgo)

For questions, suggestions, or issues, please open an issue on the GitHub repository.

-----

**⭐ If this project proves useful, please consider giving it a star on GitHub\!**
