from time import sleep


def do_config():
    step(1)
    sleep(0.5)
    step(2)
    sleep(0.5)
    return "everything done"


def step(number):
    return "something done %s" % number

import subprocess

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print(line)
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)