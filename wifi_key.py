import subprocess

subprocess.call(['netsh', 'wlan', 'show', 'profiles'])

profile = input("enter the ethernet name:")



subprocess.call(['netsh', 'wlan', 'show', 'profiles',profile, "key=clear"])

