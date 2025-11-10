import os
import pyperclip
import google.generativeai as genai

# Import configuration from config.py
try:
    from config import VAULT_PATH, GEMINI_API_KEY, MODEL_LIST
except ImportError:
    print("Error: config.py not found!")
    print("Please copy config_template.py to config.py and fill in your details.")
    exit()

genai.configure(api_key=GEMINI_API_KEY)

# 1. Get the clipboard content
clipboard_text = pyperclip.paste()
if not clipboard_text.strip():
    print("Error: Clipboard is empty!")
    exit()

# 2. Scan vault for note titles & create links list (recursive)
existing_titles = []
for root, dirs, files in os.walk(VAULT_PATH):
    for file in files:
        if file.endswith('.md'):
            existing_titles.append(file[:-3])  # Remove .md extension

note_links_str = ", ".join([f"[[{title}]]" for title in existing_titles])

# 3. Build the smart mega-prompt
prompt = f"""
You are an AI note assistant for Obsidian.
Here are the current notes in my vault (for backlinking): {note_links_str}

Take this clipboard text:
---
{clipboard_text}
---

Create a new, well-linked markdown note for Obsidian. Use [[ ]] for any relevant links.
Output the note in markdown, starting with a title (as a markdown header).
"""

# 4. Attempt generation with fallback models
def try_models(prompt, model_names):
    for model_name in model_names:
        try:
            print(f"Trying model: {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if hasattr(response, 'text') and response.text.strip():
                print(f"✓ Success with {model_name}")
                return response.text
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"✗ Quota exceeded for {model_name}, trying next model...")
                continue
            else:
                print(f"✗ Error with {model_name}: {e}")
                break
    return None

note_md = try_models(prompt, MODEL_LIST)
if note_md is None:
    print("ERROR: All models failed. Check your API key or try again later.")
    exit()

# 5. Extract note title
first_line = note_md.splitlines()[0]
note_title = first_line.lstrip('#').strip()
safe_filename = "".join(c for c in note_title if c.isalnum() or c in " _-").strip() + ".md"
note_path = os.path.join(VAULT_PATH, safe_filename)

# 6. Save to vault
with open(note_path, "w", encoding="utf-8") as f:
    f.write(note_md)

print(f"Note created: {note_path}")
