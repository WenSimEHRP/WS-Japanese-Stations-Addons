# this program gets datetime
# and prints it to the console
import datetime
import subprocess

def get_commit_number():
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

# get the current date and time in UTC
current_date = datetime.datetime.utcnow()

# convert current_date to string and append "UTC"
current_date_str = current_date.strftime("%Y-%m-%d %H:%M") + " UTC"

# read the file content
with open("custom_tags.txt", "r") as f:
    content = f.readlines()

# replace "%date" with current_date_str in the content
for index,item in enumerate(content):
    if "DATE" in item:
        content[index] = 'DATE    :' + current_date_str + "\n"
    if "COMMIT" in item:
        content[index] = 'COMMIT  :c' + get_commit_number() + "\n"

# write the new content back to the file
with open("custom_tags.txt", "w") as f:
    f.write("".join(content))

print("Date and time updated in custom_tags.txt")

with open("src/header.pnml.template", "r") as f:
    content = f.readlines()

for index,item in enumerate(content):
    if "${version}" in item:
        content[index] = f"    version:    {get_commit_number()};\n"
    if "${min_version}" in item:
        content[index] = f"    min_compatible_version:{get_commit_number()};\n"

with open("src/header.pnml", "w") as f:
    f.write("".join(content))