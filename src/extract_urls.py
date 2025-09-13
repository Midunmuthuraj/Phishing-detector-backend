import re

def extract_urls_from_text(text):
    pattern = r'(https?://\S+)'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = "Visit https://phishing.com and https://google.com"
    print(extract_urls_from_text(sample))
