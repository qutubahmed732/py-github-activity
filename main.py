import sys
import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Error: User '{username}' not found.")
        sys.exit(1)
    elif response.status_code != 200:
        print(f"Error: Failed to fetch data (Status code: {response.status_code})")
        sys.exit(1)
        
    return response.json()

def display_activity(events):
    if not events:
        print("No recent public activity found for this user.")
        return

    for event in events:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name")
        payload = event.get("payload", {})
        

        if event_type == "PushEvent":
            commit_count = len(payload.get("commits", []))
            print(f"- Pushed {commit_count} commit(s) to {repo_name}")
            
        elif event_type == "IssuesEvent":
            action = payload.get("action")
            print(f"- {action.capitalize()} an issue in {repo_name}")
            
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
            
        elif event_type == "PullRequestEvent":
            action = payload.get("action")
            print(f"- {action.capitalize()} a pull request in {repo_name}")
            
        elif event_type == "ForkEvent":
            print(f"- Forked {repo_name}")
            
        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type")
            print(f"- Created a new {ref_type} in {repo_name}")
            
        else:
            print(f"- Performed {event_type} in {repo_name}")

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <github-username>")
        sys.exit(1)
        
    username = sys.argv[1]
    print(f"Fetching recent activity for '{username}'...\n")
    
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()