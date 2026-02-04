import requests
import time


def clean_url(url: str) -> str:  # removing the "/" at the end from user input.
    return url[:-1] if url.endswith("/") else url


def target_list(base_url: str, directory: list[str]) -> list[str]:
    return [f"{base_url}/{dir_name}/" for dir_name in directory]


def scan(targets: list[str]) -> None:
    for target in targets:
        try:
            response = requests.get(target, timeout=5)
            if response.status_code == 200:
                print(f"[✓] {target} Found!")
            else:
                print(f"[x] {target} Not Found")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error Accessing {target}: {e}")


def main():
    with open("art.txt", "r") as art:
        content = art.read()
    print(content)
    time.sleep(2)
    url = input("Enter the full url : ")
    cleaned_url = clean_url(url)

    with open("sd.txt", "r") as sd:
        dir_list = set(sd.readlines())

    targets = target_list(cleaned_url, dir_list)
    scan(targets)


if __name__ == "__main__":
    main()
