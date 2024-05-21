import random
import requests

adjectives_url = "https://raw.githubusercontent.com/myalt2335/Dictionary/main/Adjectives.txt"
verbs_url = "https://raw.githubusercontent.com/myalt2335/Dictionary/main/Verbs.txt"
nouns_url = "https://raw.githubusercontent.com/myalt2335/Dictionary/main/Nouns.txt"


def fetch_words(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

adjectives = fetch_words(adjectives_url)
nouns = fetch_words(nouns_url)
verbs = fetch_words(verbs_url)

def generate_username():
    word_type = random.choice(['adjective', 'verb'])
    if word_type == 'adjective':
        word = random.choice(adjectives)
    else:
        word = random.choice(verbs)
    noun = random.choice(nouns)
    number = random.randint(1, 9)
    username = f"{word}{noun}{number}"
    return username

def main():
    version = "1.0.3"
    print(f"UserGen - Version {version}")
    print("Here's your usernames now:")
    
    while True:
        for _ in range(10):
            print(generate_username())
        user_input = input("Do you want to generate 10 more usernames? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Exiting.")
            break

if __name__ == "__main__":
    main()
