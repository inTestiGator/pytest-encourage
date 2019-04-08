import subprocess


def getpylint_output():
list = ["pipenv", "run", "pylint", "util", "-f", "json"]
try:
    automate = subprocess.check_output(list, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as automate:
    print (automate.output)
