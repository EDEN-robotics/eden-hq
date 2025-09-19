# EDEN Meeting Notes App

A Word-like GUI application for taking meeting notes with AI-powered formatting and export capabilities.

## Features

- **Word-like Interface**: Familiar text editing experience with toolbar and menu
- **AI-Powered Formatting**: Uses Google's Gemini AI to improve and format your notes
- **Markdown Export**: Convert natural language notes to GitHub-ready markdown
- **Smart Features**:
  - Auto-formatting with AI
  - Meeting summaries
  - Action item extraction
  - Grammar improvement
- **Professional Output**: Generate clean, structured documents for documentation

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

1. Copy `env.template` to `.env`:
   ```bash
   copy env.template .env
   ```

2. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

3. Edit `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
python app.py
```

## Usage

### Basic Text Editing
- Type naturally in the main text area
- Use standard keyboard shortcuts (Ctrl+S to save, Ctrl+O to open, etc.)
- Word count is displayed in the status bar

### AI Features

#### Format Notes
Select "AI Assistant" → "Format Notes" to:
- Improve organization and structure
- Enhance clarity and grammar
- Maintain all original content

#### Export to Markdown
Select "File" → "Export to Markdown" to:
- Convert notes to GitHub-ready markdown
- Add proper headings and formatting
- Include action items and decisions

#### Generate Summary
Select "AI Assistant" → "Summarize" to:
- Create concise meeting summaries
- Focus on key decisions and outcomes
- Extract important information

#### Extract Action Items
Select "AI Assistant" → "Generate Action Items" to:
- Identify tasks and follow-ups
- Assign responsibilities
- Set priorities and due dates

#### Improve Grammar
Select "AI Assistant" → "Improve Grammar" to:
- Fix spelling and grammar errors
- Enhance language quality
- Maintain original meaning

## File Formats

- **Input**: Plain text files (.txt)
- **Output**: Markdown files (.md) for GitHub documentation
- **Auto-save**: Optional automatic saving every 5 minutes

## Keyboard Shortcuts

- `Ctrl+N` - New document
- `Ctrl+O` - Open document
- `Ctrl+S` - Save document
- `Ctrl+Shift+S` - Save as
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+X` - Cut
- `Ctrl+C` - Copy
- `Ctrl+V` - Paste
- `Ctrl+A` - Select all

## Configuration

Edit `.env` to customize:

```env
# AI Settings
GEMINI_API_KEY=your_key_here
AI_MODEL_NAME=gemini-2.0-flash-exp  # Options: gemini-2.0-flash-exp, gemini-pro, gemini-1.5-flash
AI_TEMPERATURE=0.7

# App Settings
DEFAULT_FONT_FAMILY=Arial
DEFAULT_FONT_SIZE=11
AUTO_SAVE_INTERVAL=300

# Export Settings
DEFAULT_EXPORT_FORMAT=markdown
INCLUDE_TIMESTAMP=true
INCLUDE_METADATA=true
```

### Available AI Models

- **`gemini-2.0-flash-exp`** (Default) - Latest experimental model, fastest and most cost-effective
- **`gemini-1.5-flash`** - Stable flash model, good balance of speed and quality
- **`gemini-pro`** - Higher quality but slower and more expensive

## Example Workflow

1. **Take Notes**: Type meeting notes naturally during the meeting
2. **Format**: Use "Format Notes" to clean up and organize
3. **Review**: Check the formatted version
4. **Export**: Export to markdown for GitHub documentation
5. **Share**: Commit the markdown file to your repository

## Troubleshooting

### AI Not Working
- Check that `GEMINI_API_KEY` is set in `.env`
- Verify your API key is valid at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Ensure you have internet connection

### Export Issues
- Make sure you have content in the document
- Check file permissions for the save location
- Verify the AI service is working

### Performance
- Large documents may take longer to process with AI
- Consider breaking very long meetings into sections
- Save frequently to avoid data loss

## Contributing

This app is part of the EDEN project. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

Part of the EDEN project. See main project license for details.
