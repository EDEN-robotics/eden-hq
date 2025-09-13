#!/usr/bin/env python3
"""
Eden HQ - TODO and Roadmap Management Script
Helps easily update checkboxes and roadmap items
"""

import re
import os
from datetime import datetime

def update_todo_item(file_path, item_text, completed=True):
    """Update a TODO item to completed or incomplete"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the item and update its checkbox
    pattern = rf'(- \[ \] {re.escape(item_text)})'
    replacement = f'- [{"x" if completed else " "}] {item_text}'
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated: {item_text} - {'Completed' if completed else 'Incomplete'}")

def add_roadmap_item(file_path, title, status, start_date, end_date, section="Software Development"):
    """Add a new item to the roadmap"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the section and add the new item
    section_pattern = rf'(section {section}.*?)(\n    section|\n```|\n##)'
    
    new_item = f"    {title:<30} :{status}, {title.lower().replace(' ', '-')}, {start_date}, {end_date}\n"
    
    def replace_section(match):
        section_content = match.group(1)
        return section_content + new_item + match.group(2)
    
    new_content = re.sub(section_pattern, replace_section, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Added to roadmap: {title}")

def list_todo_items(file_path):
    """List all TODO items with their status"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all checkbox items
    pattern = r'- \[([ x])\] (.+)'
    matches = re.findall(pattern, content)
    
    print("\n📋 TODO Items:")
    for i, (status, item) in enumerate(matches, 1):
        status_icon = "✅" if status == "x" else "⏳"
        print(f"{i:2d}. {status_icon} {item}")

def main():
    """Main function with interactive menu"""
    print("🌱 Eden HQ - Project Management Tool")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. List TODO items")
        print("2. Mark TODO item as complete")
        print("3. Mark TODO item as incomplete")
        print("4. Add roadmap item")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            list_todo_items("TODO.md")
        
        elif choice == "2":
            list_todo_items("TODO.md")
            item_num = input("\nEnter item number to mark complete: ").strip()
            try:
                # This would need more complex logic to find the specific item
                print("Feature coming soon! For now, edit TODO.md directly.")
            except:
                print("Invalid item number")
        
        elif choice == "3":
            print("Feature coming soon! For now, edit TODO.md directly.")
        
        elif choice == "4":
            title = input("Enter item title: ").strip()
            status = input("Enter status (active/done/crit): ").strip()
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            section = input("Enter section (default: Software Development): ").strip() or "Software Development"
            
            add_roadmap_item("ROADMAP.md", title, status, start_date, end_date, section)
        
        elif choice == "5":
            print("👋 Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
