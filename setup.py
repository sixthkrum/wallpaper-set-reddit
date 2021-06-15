import os

wd = os.path.dirname(os.path.realpath(__file__))

print("Setting paths in scripts to the current folder:" + wd)
print("Input subreddit to get wallpapers from.")
print("There are no checks for allowed subs;")
sub_name = input("if the script does not work recheck the name and replace it in 'wallpaper-script.py' directly: ")

files = [
"wallpaper-cron-script",
"wallpaper-script.py"
]


for file in files:
    with open(file, "r+") as script:
        set_script = script.read().replace("$__PATH__", wd)
        set_script = set_script.replace("$__SUBREDDIT__", sub_name)
        script.seek(0)
        script.write(set_script)
        script.truncate()

print("Setting wallpaper-cron-script to be executable")
os.system("chmod +x wallpaper-cron-script")
