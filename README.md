# GitHub User Activity CLI

A simple Python CLI tool that fetches and displays recent public activity for any GitHub user.

## Challenge

This project is the [GitHub User Activity challenge](https://roadmap.sh/projects/github-user-activity) that I accomplished.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Create and activate a virtual environment:

   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

## How to Run

Pass any GitHub username as an argument:

```bash
python main.py <username>
```

**Example:**
```bash
python main.py octocat
```

**Output:**
```text
Fetching recent activity for 'octocat'...

- Pushed 1 commit(s) to octocat/Spoon-Knife
- Starred octocat/Hello-World
- Forked octocat/Hello-World
```
