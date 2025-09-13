# 📸 Visual Guide - How to Edit on GitHub

> **Step-by-step with pictures!** Perfect for visual learners.

## 🎯 What You'll Learn
- How to edit files directly on GitHub
- How to mark tasks as complete
- How to add new tasks
- How to update the roadmap

## 📋 Editing TODO.md

### Step 1: Open the File
1. Go to the repository on GitHub
2. Click on `TODO.md` in the file list
3. You'll see the file contents

### Step 2: Start Editing
1. **Click the pencil icon** ✏️ (top right corner)
2. The file will open in edit mode
3. You can now make changes

### Step 3: Mark Tasks Complete
1. **Find a task** you want to mark as done
2. **Change `[ ]` to `[x]`** (add an x inside the brackets)
3. Example:
   ```
   # Before
   - [ ] Set up ROS 2 Humble workspace
   
   # After
   - [x] Set up ROS 2 Humble workspace
   ```

### Step 4: Add New Tasks
1. **Find a section** like "Software Tasks"
2. **Add a new line** like this:
   ```
   - [ ] Your new task here
   ```
3. **Be specific** about what needs to be done

### Step 5: Save Changes
1. **Scroll to the bottom** of the page
2. **Type a message** like "Updated TODO list"
3. **Click "Commit changes"** (green button)
4. **Done!** ✅

## 📊 Editing ROADMAP.md

### Step 1: Open the File
1. Click on `ROADMAP.md` in the file list
2. You'll see the roadmap with a Gantt chart

### Step 2: Start Editing
1. **Click the pencil icon** ✏️
2. The file will open in edit mode

### Step 3: Find the Mermaid Code
1. **Look for this text**: ```mermaid
2. **Find a section** like "Software Development"
3. **You'll see lines** like this:
   ```
   ROS 2 Workspace Setup       :done, ros2-ws, 2025-01-01, 2025-02-15
   ```

### Step 4: Add New Tasks
1. **Add a new line** in the appropriate section
2. **Use this format**:
   ```
   Your Task Name        :active, task-id, 2025-03-01, 2025-04-30
   ```
3. **Example**:
   ```
   New Feature Development  :active, new-feat, 2025-03-15, 2025-05-15
   ```

### Step 5: Change Task Status
1. **Find the task** you want to update
2. **Change the status**:
   - `:done` = Task is finished
   - `:active` = Task is currently being worked on
   - `:crit` = Task is critical/urgent

### Step 6: Save Changes
1. **Scroll to the bottom**
2. **Type a message** like "Updated roadmap"
3. **Click "Commit changes"**
4. **Done!** ✅

## 🎨 Understanding the Format

### TODO.md Format:
```
- [ ] Task not started
- [x] Task completed
```

### ROADMAP.md Format:
```
Task Name        :status, id, start-date, end-date
```

**Status Options:**
- `:done` = Finished
- `:active` = In progress
- `:crit` = Critical/urgent
- `:milestone` = Important milestone

## 🆘 Troubleshooting

### **I can't find the pencil icon!**
- Make sure you're logged into GitHub
- Check if you have permission to edit the repository
- Try refreshing the page

### **The changes don't look right!**
- Check the format carefully
- Make sure you're using the right symbols
- Don't worry - you can always edit again!

### **I made a mistake!**
- No problem! Just edit the file again
- You can always fix mistakes
- The worst that can happen is you need to edit again

## 🎉 You're All Set!

Now you know how to:
- ✅ Edit files on GitHub
- ✅ Mark tasks as complete
- ✅ Add new tasks
- ✅ Update the roadmap
- ✅ Fix mistakes

**Welcome to the Eden project!** 🤖✨
