#!/usr/bin/env python3
"""
Nowm.tech Website Monitor
Checks every 5 minutes for improvements and pushes changes to GitHub.
"""

import subprocess
import sys
import os
import time
from datetime import datetime

REPO_DIR = '/opt/data/nowm.tech'
SITE_URL = 'https://selimpbn-collab.github.io/nowm.tech/'

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}', flush=True)

def check_site():
    """Check if the site is live and accessible."""
    import urllib.request
    try:
        with urllib.request.urlopen(SITE_URL, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        log(f'Site check failed: {e}')
        return False

def check_git_status():
    """Check if there are uncommitted changes."""
    result = subprocess.run(
        ['git', 'status', '--porcelain'],
        capture_output=True,
        text=True,
        cwd=REPO_DIR
    )
    return result.stdout.strip() != ''

def push_to_github():
    """Push changes to GitHub."""
    # Stage all changes
    subprocess.run(['git', 'add', '-A'], cwd=REPO_DIR, capture_output=True)
    
    # Commit if there are changes
    if check_git_status():
        commit_msg = f"Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        result = subprocess.run(
            ['git', 'commit', '-m', commit_msg],
            capture_output=True,
            text=True,
            cwd=REPO_DIR
        )
        log(f'Commit: {result.stdout.strip() or result.stderr.strip()}')
    
    # Push to origin
    push_result = subprocess.run(
        ['git', 'push', 'origin', 'main'],
        capture_output=True,
        text=True,
        cwd=REPO_DIR
    )
    if push_result.returncode == 0:
        log('Successfully pushed to GitHub')
        return True
    else:
        log(f'Push failed: {push_result.stderr.strip()}')
        log('Credentials not configured. Site is still live on GitHub Pages.')
        return False

def main():
    """Main monitoring loop."""
    log('Starting Nowm.tech website monitor...')
    
    # First check
    log(f'Checking site: {SITE_URL}')
    site_ok = check_site()
    log(f'Site status: {"OK" if site_ok else "FAIL"}')
    
    # Check git status
    if check_git_status():
        log('Uncommitted changes detected. Pushing to GitHub...')
        push_to_github()
    else:
        log('No uncommitted changes. Nothing to push.')
    
    log('Monitoring complete. Waiting 5 minutes for next check...')
    
    # Schedule next check in 5 minutes
    for i in range(300):
        time.sleep(60)
        log(f'Next check in {300 - i} seconds...')

if __name__ == '__main__':
    main()
