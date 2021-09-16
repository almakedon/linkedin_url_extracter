import re
from pathlib import Path


current_dir = Path(__file__).parent.absolute()
file_path = current_dir.joinpath("list.txt")
url_pattern = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")


with open(file_path, "r") as text_file:
    linkedin_names = [line for line in text_file.read().splitlines() if "linkedin" in line.lower()]

cleaned_linkedin_urls = []
for person_line in linkedin_names:
        url = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', person_line)
        if url and "linkedin" in url[0]:
            cleaned_linkedin_urls.append((url[0] + "\n"))
        #else:
        #    cleaned_linkedin_names.append("".join(item[1:]))


with open("linkedin_urls.txt", "w") as linkedin_urls_file:
    linkedin_urls_file.writelines(cleaned_linkedin_urls)
