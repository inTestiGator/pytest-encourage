import subprocess


def getpylint_output():
    list = ["pipenv", "run", "pylint", "util", "-f", "json"]
    try:
        automate = subprocess.check_output(list, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as automate:
        output = automate.output
        print (automate.output)
        return automate.output