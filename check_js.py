#!/usr/bin/env python3
"""
check_js.py — Real JavaScript syntax checker for nowm.tech.

The previous shim only balanced parentheses per line. This version uses Node's
own parser ("node --check") which performs a full syntax check of every inline
<script> block in index.html. Exits 0 on success, 1 on any parse error.

Usage:
    python3 check_js.py            # check index.html (default)
    python3 check_js.py <file>     # check a specific HTML file
    python3 check_js.py --watch    # watch mode (re-checks on change)

CI note: wired into .github/workflows/azure-webapps-node.yml via `npm run test`
if a test script is present (see package.json or the workflow).
"""

import os
import subprocess
import sys
import tempfile

DEFAULT_HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
NODE = "node"
NODE_CHECK = ["node", "--check"]
TIMEOUT = 60  # seconds


def read_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def extract_scripts(html, html_path):
    """Return a list of inline <script> bodies (external src scripts skipped)."""
    scripts = []
    # Match <script>...</script> where the opening tag has NO src attribute.
    import re
    pattern = re.compile(r"<script(?![^>]*\bsrc\s*=\s*['\"][^'\"]*['\"])[^>]*>(.*?)</script>",
                        re.S)
    for match in pattern.finditer(html):
        body = match.group(1)
        # Strip HTML entities / comments that leak in
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        body = re.sub(r"&\w+;", " ", body)
        if body.strip():
            scripts.append((match.start(), body))
    return scripts


def main(argv):
    html_path = DEFAULT_HTML
    if argv and argv[0] == "--watch":
        print("Watching " + html_path + " for changes...")
        return watch(html_path)
    if argv and argv[0] != "--watch":
        html_path = argv[0]

    if not os.path.exists(html_path):
        print(f"ERROR: {html_path} not found", file=sys.stderr)
        return 1

    try:
        html = read_file(html_path)
    except Exception as exc:
        print(f"ERROR reading {html_path}: {exc}", file=sys.stderr)
        return 1

    scripts = extract_scripts(html, html_path)
    if not scripts:
        print(f"No inline JavaScript found in {html_path}")
        return 0

    # Write all inline scripts to a temp file, one per line, wrapped safely.
    fd, tmp_path = tempfile.mkstemp(suffix=".js", prefix="nowm_check_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write("\n// --- script block ---\n")
            for _, body in scripts:
                fh.write(body.strip() + "\n\n")

        cmd = NODE_CHECK + [tmp_path]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=TIMEOUT
            )
        except subprocess.TimeoutExpired:
            print(f"ERROR: `node --check` timed out on {html_path}", file=sys.stderr)
            return 1

        if proc.stdout:
            print(proc.stdout)
        if proc.stderr:
            print(proc.stderr, file=sys.stderr)

        if proc.returncode == 0:
            print(f"✅ JavaScript syntax OK in {html_path} ({len(scripts)} inline block(s))")
            return 0
        else:
            print(f"❌ JavaScript syntax errors in {html_path}", file=sys.stderr)
            return 1
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def watch(html_path):
    import time
    print(f"Watching {html_path} (Ctrl+C to stop).")
    last_mtime = 0
    while True:
        try:
            mtime = os.path.getmtime(html_path)
            if mtime != last_mtime:
                last_mtime = mtime
                sys.exit(main([html_path]))
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nStopped watching.")
            break
        except Exception as exc:
            print(f"watch error: {exc}", file=sys.stderr)
            time.sleep(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
