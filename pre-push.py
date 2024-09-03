#!/usr/bin/env python

import sys
import subprocess

def get_current_branch():
    """Returns the name of the current branch."""
    branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    ).stdout.strip()
    return branch

def main():
    branch_name = get_current_branch()

    # Logging to a file for debugging
    with open("hook_debug.log", "a") as log_file:
        log_file.write(f"Branch: {branch_name}\n")

    # Check if the current branch is master or main
    if branch_name in ['master', 'main']:
        with open("hook_debug.log", "a") as log_file:
            log_file.write(f"Error: Push to '{branch_name}' branch is not allowed.\n")
        sys.exit(1)
    
    # Allow the push to proceed
    with open("hook_debug.log", "a") as log_file:
        log_file.write(f"Push to '{branch_name}' branch is allowed.\n")
    sys.exit(0)

if __name__ == "__main__":
    main()



# #!/usr/bin/env python

# import sys
# import subprocess

# def get_current_branch():
#     """Returns the name of the current branch."""
#     branch = subprocess.run(
#         ["git", "rev-parse", "--abbrev-ref", "HEAD"],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     ).stdout.strip()
#     return branch

# def main():
#     branch_name = get_current_branch()

#     # Check if the current branch is master or main
#     if branch_name in ['master', 'main']:
#         print(f"Error: Push to '{branch_name}' branch is not allowed.", file=sys.stderr)
#         sys.exit(1)
    
#     # Allow the push to proceed
#     print(f"Push to '{branch_name}' branch is allowed.")
#     sys.exit(0)

# if __name__ == "__main__":
#     main()
