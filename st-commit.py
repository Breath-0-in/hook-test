#!/usr/bin/env python3

import sys
import subprocess

#현재 HEAD인 브랜치의 이름 가져옴
def get_current_branch():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        branch_name = result.stdout.strip()
        return branch_name
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    branch_name = get_current_branch()

    # Check if the current branch is master
    if (branch_name == 'master' or branch_name == 'main'):
        print(f"Error: Commits to the 'master/main' branch are not allowed.", file=sys.stderr)
        sys.exit(1)  # Non-zero exit code to abort the commit

    # Allow the commit to proceed
    print(f"Branch '{branch_name}' is allowed for commit.")
    sys.exit(0)  # Zero exit code to proceed with the commit

if __name__ == "__main__":
    main()
