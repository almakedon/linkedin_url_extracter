import re
from pathlib import Path
from typing import List

CURRENT_DIR = Path(__file__).parent.absolute()
FILE_PATH = CURRENT_DIR.joinpath("list.txt")


def get_linkedin_lines_from_file(file=FILE_PATH) -> list:
    """
    Opens a text file and extracts lines with the word "linkedin"
    :param file: Full path to file to open
    :return: List with lines that contain the string "linkedin"
    """
    try:
        with open(file, "r") as text_file:
            linkedin_names = [line for line in text_file.read().splitlines() if "linkedin" in line.lower()]

        print(f"Finished reading {file}")
        return linkedin_names
    except (TypeError, FileNotFoundError):
        print("No valid file found. Did you specify the file argument or add list.txt to the folder the script is "
              "run from?")
        exit()


def get_linkedin_urls(linkedin_list: List[str]) -> List[str]:
    """
    Looks for linkedin urls in a list with strings containing "linkedin"
    :param linkedin_list: List of strings containing the word linkedin
    :return: List with linkedin urls
    """
    print("Looking for linkedin urls:")
    cleaned_linkedin_urls = []
    for person_line in linkedin_list:
        url = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', person_line, flags=re.IGNORECASE)
        if url and "linkedin" in url[0]:
            cleaned_linkedin_urls.append((url[0]))
        # else:
        #    cleaned_linkedin_names.append("".join(item[1:]))
    print(f"Found {len(cleaned_linkedin_urls)} urls")
    return cleaned_linkedin_urls


def get_linkedin_names(linkedin_list: List[str]) -> List[str]:
    """
    Gets linkedin person names from a string containing "linkedin"
    :param linkedin_list: List containing strings with "linkedin"
    :return: List of person names
    """
    print("Looking for linkedin names:")
    names = []
    for line in linkedin_list:
        name = re.findall(r"linkedin[:| ]{1,3}(?!.*http)[\w -()]*", line, flags=re.IGNORECASE)
        if name:
            name = name[0].lower().split(":")
            name = name[-1].strip()
            if "linkedin" not in name:
                # split = name.split(":")
                names.append(name)
            elif "linkedin" in name:
                names.append(name.replace("linkedin", ""))
    print(f"Found {len(names)} names")
    return names


def save_urls_to_file(urls: List[str], file: str = "linkedin_urls.txt"):
    """
    Saves a list of urls to a text file
    :param urls: Urls to save
    :param file: Filename or filepath
    """
    with open(file, "w") as linkedin_urls_file:
        urls = [url + "\n" for url in urls]
        linkedin_urls_file.writelines(urls)
        print(f"Saved {len(urls)} to {file}")


def save_names_to_file(names: List[str], file: str = "linkedin_names.txt"):
    """
    Saves a list of names to provided filename. Default filename is "linkedin_names.txt"
    :param names: Linkedin names
    :param file: Filename
    """
    with open(file, "w") as linkedin_name_file:
        linkedin_name_file.writelines(["Names of people without posted linkedin url \n"])
        names = [name + "\n" for name in names]
        linkedin_name_file.writelines(names)
        print(f"Saved {len(names)} to {file}")


def main():
    """
    Gets linkedin names and urls from a text file and saves to separate files for url and names
    :return:
    """
    linkedin_lines = get_linkedin_lines_from_file()
    linkedin_urls = get_linkedin_urls(linkedin_lines)
    linkedin_names = get_linkedin_names(linkedin_lines)

    save_urls_to_file(linkedin_urls)
    save_names_to_file(linkedin_names)


main()
