import subprocess


def check_tool_exists(command):
    try:
        subprocess.check_call([command, "--help"])
    except subprocess.CalledProcessError:
        print("ERROR: `{}` is required".format(command))
        exit(1)


# Check Git and make exists
check_tool_exists("git")
check_tool_exists("make")
