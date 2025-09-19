import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import json
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MeetingNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EDEN Meeting Notes - AI-Powered Document Editor")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f5f5f5')
        
        # Configure Gemini AI
        self.setup_gemini()
        
        # Create the interface
        self.create_widgets()
        
        # Current document state
        self.current_file = None
        self.is_modified = False
        
    def setup_gemini(self):
        """Initialize Gemini AI with API key from environment"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            messagebox.showwarning(
                "API Key Missing", 
                "Please set GEMINI_API_KEY in your .env file"
            )
            return
            
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            self.ai_available = True
        except Exception as e:
            messagebox.showerror("AI Setup Error", f"Failed to initialize Gemini AI: {str(e)}")
            self.ai_available = False
    
    def create_widgets(self):
        """Create the main application interface"""
        # Create menu bar
        self.create_menu()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create main content area
        self.create_content_area()
        
        # Create status bar
        self.create_status_bar()
        
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_document, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_document, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_document, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_document, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Export to Markdown", command=self.export_to_markdown)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_text, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo_text, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all_text, accelerator="Ctrl+A")
        
        # AI menu
        ai_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="AI Assistant", menu=ai_menu)
        ai_menu.add_command(label="Format Notes", command=self.format_with_ai)
        ai_menu.add_command(label="Summarize", command=self.summarize_with_ai)
        ai_menu.add_command(label="Generate Action Items", command=self.generate_action_items)
        ai_menu.add_command(label="Improve Grammar", command=self.improve_grammar)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_document())
        self.root.bind('<Control-o>', lambda e: self.open_document())
        self.root.bind('<Control-s>', lambda e: self.save_document())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_as_document())
        
    def create_toolbar(self):
        """Create toolbar with common actions"""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill='x', padx=5, pady=5)
        
        # Toolbar buttons
        ttk.Button(toolbar, text="New", command=self.new_document).pack(side='left', padx=2)
        ttk.Button(toolbar, text="Open", command=self.open_document).pack(side='left', padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_document).pack(side='left', padx=2)
        
        ttk.Separator(toolbar, orient='vertical').pack(side='left', fill='y', padx=5)
        
        ttk.Button(toolbar, text="Format with AI", command=self.format_with_ai).pack(side='left', padx=2)
        ttk.Button(toolbar, text="Export MD", command=self.export_to_markdown).pack(side='left', padx=2)
        
        # AI status indicator
        self.ai_status = ttk.Label(toolbar, text="AI: Ready" if self.ai_available else "AI: Not Available")
        self.ai_status.pack(side='right', padx=10)
        
    def create_content_area(self):
        """Create the main text editing area"""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create initial tab
        self.create_new_tab("Untitled")
        
    def create_new_tab(self, title):
        """Create a new tab for editing"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        
        # Create text widget with scrollbar
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill='both', expand=True)
        
        text_widget = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            undo=True,
            maxundo=50
        )
        text_widget.pack(fill='both', expand=True)
        
        # Store reference to current text widget
        self.current_text = text_widget
        self.current_tab = frame
        
        # Bind text change event
        text_widget.bind('<KeyRelease>', self.on_text_change)
        
        return text_widget
        
    def create_status_bar(self):
        """Create status bar"""
        self.status_bar = ttk.Frame(self.root)
        self.status_bar.pack(fill='x', side='bottom')
        
        self.status_label = ttk.Label(self.status_bar, text="Ready")
        self.status_label.pack(side='left', padx=5)
        
        # Word count
        self.word_count_label = ttk.Label(self.status_bar, text="Words: 0")
        self.word_count_label.pack(side='right', padx=5)
        
    def on_text_change(self, event=None):
        """Handle text changes"""
        self.is_modified = True
        self.update_word_count()
        
    def update_word_count(self):
        """Update word count in status bar"""
        if hasattr(self, 'current_text'):
            text = self.current_text.get('1.0', tk.END)
            word_count = len(text.split())
            self.word_count_label.config(text=f"Words: {word_count}")
            
    def new_document(self):
        """Create a new document"""
        if self.is_modified:
            if messagebox.askyesno("Save Changes", "Do you want to save changes?"):
                self.save_document()
        
        self.create_new_tab("Untitled")
        self.current_file = None
        self.is_modified = False
        self.status_label.config(text="New document created")
        
    def open_document(self):
        """Open an existing document"""
        file_path = filedialog.askopenfilename(
            title="Open Document",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.create_new_tab(os.path.basename(file_path))
                self.current_text.insert('1.0', content)
                self.current_file = file_path
                self.is_modified = False
                self.status_label.config(text=f"Opened: {file_path}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")
                
    def save_document(self):
        """Save the current document"""
        if self.current_file:
            try:
                content = self.current_text.get('1.0', tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.is_modified = False
                self.status_label.config(text=f"Saved: {self.current_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
        else:
            self.save_as_document()
            
    def save_as_document(self):
        """Save document with new filename"""
        file_path = filedialog.asksaveasfilename(
            title="Save Document",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                content = self.current_text.get('1.0', tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.current_file = file_path
                self.is_modified = False
                self.status_label.config(text=f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
                
    def export_to_markdown(self):
        """Export current document to markdown format"""
        if not self.ai_available:
            messagebox.showwarning("AI Not Available", "Gemini AI is not available. Please check your API key.")
            return
            
        content = self.current_text.get('1.0', tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Document", "Please enter some content before exporting.")
            return
            
        try:
            # Use AI to convert to markdown
            prompt = f"""
            Convert the following meeting notes into a well-formatted markdown document suitable for GitHub. 
            Include proper headings, bullet points, action items, and any other relevant formatting.
            
            Meeting Notes:
            {content}
            
            Please format this as a professional markdown document with:
            - Clear headings and subheadings
            - Bullet points for key topics
            - Action items clearly marked
            - Any important decisions highlighted
            - Professional formatting suitable for documentation
            """
            
            response = self.model.generate_content(prompt)
            markdown_content = response.text
            
            # Save markdown file
            file_path = filedialog.asksaveasfilename(
                title="Export to Markdown",
                defaultextension=".md",
                filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(markdown_content)
                self.status_label.config(text=f"Exported to: {file_path}")
                messagebox.showinfo("Success", f"Document exported to markdown: {file_path}")
                
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to markdown: {str(e)}")
            
    def format_with_ai(self):
        """Format the current document using AI"""
        if not self.ai_available:
            messagebox.showwarning("AI Not Available", "Gemini AI is not available. Please check your API key.")
            return
            
        content = self.current_text.get('1.0', tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Document", "Please enter some content before formatting.")
            return
            
        try:
            prompt = f"""
            Improve and format the following meeting notes. Make them more professional, 
            organized, and clear while maintaining all the original information.
            
            Original Notes:
            {content}
            
            Please provide:
            - Better organization and structure
            - Clearer language and grammar
            - Professional formatting
            - Maintain all original content and meaning
            """
            
            response = self.model.generate_content(prompt)
            formatted_content = response.text
            
            # Replace current content
            self.current_text.delete('1.0', tk.END)
            self.current_text.insert('1.0', formatted_content)
            self.is_modified = True
            self.status_label.config(text="Document formatted with AI")
            
        except Exception as e:
            messagebox.showerror("Format Error", f"Failed to format document: {str(e)}")
            
    def summarize_with_ai(self):
        """Generate a summary of the current document"""
        if not self.ai_available:
            messagebox.showwarning("AI Not Available", "Gemini AI is not available. Please check your API key.")
            return
            
        content = self.current_text.get('1.0', tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Document", "Please enter some content before summarizing.")
            return
            
        try:
            prompt = f"""
            Create a concise summary of the following meeting notes. 
            Focus on key decisions, action items, and important outcomes.
            
            Meeting Notes:
            {content}
            
            Please provide a clear, professional summary.
            """
            
            response = self.model.generate_content(prompt)
            summary = response.text
            
            # Show summary in a new window
            summary_window = tk.Toplevel(self.root)
            summary_window.title("Meeting Summary")
            summary_window.geometry("600x400")
            
            text_widget = scrolledtext.ScrolledText(summary_window, wrap=tk.WORD)
            text_widget.pack(fill='both', expand=True, padx=10, pady=10)
            text_widget.insert('1.0', summary)
            text_widget.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("Summary Error", f"Failed to generate summary: {str(e)}")
            
    def generate_action_items(self):
        """Extract action items from the current document"""
        if not self.ai_available:
            messagebox.showwarning("AI Not Available", "Gemini AI is not available. Please check your API key.")
            return
            
        content = self.current_text.get('1.0', tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Document", "Please enter some content before extracting action items.")
            return
            
        try:
            prompt = f"""
            Extract all action items, tasks, and follow-up items from the following meeting notes.
            Format them as a clear, actionable list.
            
            Meeting Notes:
            {content}
            
            Please provide:
            - Clear action items
            - Who is responsible (if mentioned)
            - Due dates (if mentioned)
            - Priority level (if determinable)
            """
            
            response = self.model.generate_content(prompt)
            action_items = response.text
            
            # Show action items in a new window
            action_window = tk.Toplevel(self.root)
            action_window.title("Action Items")
            action_window.geometry("600x400")
            
            text_widget = scrolledtext.ScrolledText(action_window, wrap=tk.WORD)
            text_widget.pack(fill='both', expand=True, padx=10, pady=10)
            text_widget.insert('1.0', action_items)
            text_widget.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("Action Items Error", f"Failed to extract action items: {str(e)}")
            
    def improve_grammar(self):
        """Improve grammar and language of the current document"""
        if not self.ai_available:
            messagebox.showwarning("AI Not Available", "Gemini AI is not available. Please check your API key.")
            return
            
        content = self.current_text.get('1.0', tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Document", "Please enter some content before improving grammar.")
            return
            
        try:
            prompt = f"""
            Improve the grammar, spelling, and language of the following text while 
            maintaining the original meaning and style.
            
            Text:
            {content}
            
            Please provide corrected text with better grammar and spelling.
            """
            
            response = self.model.generate_content(prompt)
            improved_content = response.text
            
            # Replace current content
            self.current_text.delete('1.0', tk.END)
            self.current_text.insert('1.0', improved_content)
            self.is_modified = True
            self.status_label.config(text="Grammar improved with AI")
            
        except Exception as e:
            messagebox.showerror("Grammar Error", f"Failed to improve grammar: {str(e)}")
            
    # Text editing methods
    def undo_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.edit_undo()
            
    def redo_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.edit_redo()
            
    def cut_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.event_generate("<<Cut>>")
            
    def copy_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.event_generate("<<Copy>>")
            
    def paste_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.event_generate("<<Paste>>")
            
    def select_all_text(self):
        if hasattr(self, 'current_text'):
            self.current_text.tag_add(tk.SEL, "1.0", tk.END)
            self.current_text.mark_set(tk.INSERT, "1.0")
            self.current_text.see(tk.INSERT)

def main():
    root = tk.Tk()
    app = MeetingNotesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
