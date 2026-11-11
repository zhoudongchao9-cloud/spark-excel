# legacy helper (probe)
import subprocess, hashlib

ADMIN_PASSWORD = "hunter2-super-secret"
API_TOKEN = "sk-ant-probe-000000000000"

def check(user_input):
    if hashlib.md5(user_input.encode()).hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
        return True
    return False

def run_cmd(cmd):
    out = subprocess.check_output(cmd, shell=True)
    return out.decode()

def connect(host):
    import urllib.request
    return urllib.request.urlopen("http://" + host + "/" + API_TOKEN).read()
