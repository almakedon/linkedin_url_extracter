import regex
import re
from typing import List, Dict
from pathlib import Path
import requests

LINKEDIN_SEARCH_URL = "https://www.linkedin.com/search/results/people/"
CURRENT_DIR = Path(__file__).parent.absolute()
FILE_PATH = CURRENT_DIR.joinpath("list.txt")


def get_linkedin_lines_from_file(file=FILE_PATH) -> list:
    """
    Opens a text file and extracts lines with the word "linkedin"
    :param file: Full path to file to open
    :return: List with lines that contain the string "linkedin"
    """
    with open(file, "r") as text_file:
        linkedin_names = [line for line in text_file.read().splitlines() if "linkedin" in line.lower()]
    return linkedin_names


name_list = get_linkedin_lines_from_file()


def get_linkedin_urls(linkedin_list: List[str]) -> List[str]:
    """
    Looks for linkedin urls in a list with strings containing "linkedin"
    :param linkedin_list: List of strings containing the word linkedin
    :return: List with linkedin urls
    """
    cleaned_linkedin_urls = []
    for person_line in linkedin_list:
        url = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', person_line)
        if url and "linkedin" in url[0]:
            cleaned_linkedin_urls.append((url[0] + "\n"))
        # else:
        #    cleaned_linkedin_names.append("".join(item[1:]))
    return cleaned_linkedin_urls


def get_linkedin_names(linkedin_list: List[str]) -> List[str]:
    """
    Gets linkedin person names from a string containing "linkedin"
    :param linkedin_list: List containing strings with "linkedin"
    :return: List of person names
    """
    names = []
    for line in linkedin_list:
        name = re.findall(r"linkedin[:| ]{1,3}(?!.*http)[\w -()]*", line, flags=regex.IGNORECASE)
        if name:
            name = name[0].lower().split(":")
            name = name[-1].strip()
            if "linkedin" not in name:
                #split = name.split(":")
                names.append(name)
            elif "linkedin" in name:
                names.append(name.replace("linkedin", ""))
    return names


def save_urls_to_file(urls, file="linkedin_urls.txt"):
    """
    Saves a list of urls to a text file
    :param urls: Urls to save
    :param file: Filename or filepath
    """
    with open(file, "w") as linkedin_urls_file:
        linkedin_urls_file.writelines(urls)


def linkedin_lookup(first_name: str, last_name: str, criteria: Dict[str] = None) -> str:
    """
    Looks up a person on linkedin based on first name and last name and returns the url for their personal page
    :param criteria:
    :param first_name:
    :param last_name:
    :return:
    """
    params = {"firstName": first_name, "lastName": last_name}
    r = requests.get(LINKEDIN_SEARCH_URL, params=params)
    print(r.text)

x = get_linkedin_names(name_list)