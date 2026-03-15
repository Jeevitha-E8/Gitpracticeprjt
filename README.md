# 🚀 Flask Git Practice Tracker

A simple task tracker app built to practice **Git commands**, **GitHub workflows**, and **CI/CD pipelines**.

---

## Setup

```bash
# Clone the repo (after you push it to GitHub)
git clone https://github.com/Jeevitha-E8/flask-git-practice.git
cd flask-git-practice

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
# Visit http://localhost:5000
```

---

## 📘 Git Commands Cheat Sheet

### 🟢 PHASE 1: Getting Started

```bash
# Initialize a new repo
git init

# Check status (use this ALL the time)
git status

# Connect to your GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/flask-git-practice.git

# Verify remote
git remote -v
```

### 🔵 PHASE 2: Daily Workflow (The Bread & Butter)

```bash
# Check what changed
git status
git diff                         # See exact line changes

# Stage files for commit
git add app.py                   # Stage one file
git add .                        # Stage ALL changes
git add templates/               # Stage a folder

# Commit (save a snapshot)
git commit -m "fix: update task status logic"

# Pull latest changes from remote BEFORE pushing
git pull origin main

# Push your commits to GitHub
git push origin main
```

### 🟡 PHASE 3: Branching (For Support Work)

```bash
# Create and switch to a new branch
git checkout -b fix/task-delete-bug

# List all branches
git branch -a

# Switch between branches
git checkout main
git checkout fix/task-delete-bug

# After fixing, merge back to main
git checkout main
git merge fix/task-delete-bug

# Delete branch after merge
git branch -d fix/task-delete-bug
```

### 🟠 PHASE 4: When New Code Comes (Pulling Updates)

```bash
# Fetch changes without merging (just check)
git fetch origin

# See what's new
git log origin/main --oneline -5

# Pull and merge the new changes
git pull origin main

# If there are conflicts:
# 1. Open the conflicted file
# 2. Look for <<<<<<< HEAD and >>>>>>> markers
# 3. Fix the code manually
# 4. Then:
git add .
git commit -m "fix: resolve merge conflict in app.py"
```

### 🔴 PHASE 5: Undo & Fix Mistakes

```bash
# Undo changes in a file (before staging)
git checkout -- app.py

# Unstage a file
git reset HEAD app.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️ CAREFUL
git reset --hard HEAD~1

# See commit history
git log --oneline -10
git log --oneline --graph --all   # Visual branch graph
```

### 🟣 PHASE 6: Stashing (Pause Your Work)

```bash
# Save current work temporarily
git stash

# See stashed items
git stash list

# Get your work back
git stash pop

# Useful when: you're mid-fix and need to pull urgent changes
```

---

## 🔄 CI/CD Pipeline

This project includes a GitHub Actions pipeline (`.github/workflows/ci.yml`) that runs automatically:

- **On every push** to `main` or `develop`
- **On every pull request** to `main`

### What it does:

1. **Runs all tests** via `pytest`
2. **Health check** — verifies `/health` endpoint works
3. **Linting** — checks code style with `flake8`

### Practice CI/CD:

```bash
# Step 1: Make a change (e.g., add a new route in app.py)
# Step 2: Run tests locally first
pytest tests/ -v

# Step 3: Push to GitHub
git add .
git commit -m "feat: add new endpoint"
git push origin main

# Step 4: Go to GitHub → Actions tab → Watch pipeline run!
```

---

## 🛠 Practice Exercises

1. **Add a feature**: Add a `/about` page → commit → push → check CI
2. **Fix a bug**: Break something on purpose → fix it → commit with `fix:` prefix
3. **Branch workflow**: Create `feature/priority-field` → add a priority field to tasks → merge via Pull Request
4. **Handle conflicts**: Edit the same line in two branches → merge → resolve conflict
5. **CI failure**: Make a test fail → push → see CI fail → fix → push again

---

## Project Structure

```
flask-git-practice/
├── app.py                      # Main Flask app
├── requirements.txt            # Dependencies
├── .gitignore                  # Files Git should ignore
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline
├── templates/
│   └── index.html              # Web UI
└── tests/
    └── test_app.py             # Unit tests
```
