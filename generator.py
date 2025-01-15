import requests
from bs4 import BeautifulSoup
import re
import argparse

class WordlistGenerator:
    def __init__(self, url, min_length=4, max_length=12, output_file="wordlist.txt"):
        # Initialize the generator with URL, word length limits, and output file
        self.url = url
        self.min_length = min_length
        self.max_length = max_length
        self.output_file = output_file

    def fetch_content(self):
        # Fetch HTML content from the given URL
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for HTTP issues
            return response.text
        except requests.exceptions.RequestException as e:
            # Return None if there is an error during the request
            return None

    def extract_words(self, html_content):
        # Extract words from the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')  # Parse HTML content
        text = soup.get_text()  # Extract text from the HTML
        words = re.findall(r"\b\w+\b", text)  # Find all words using regex
        # Filter words based on the defined length range and convert to lowercase
        filtered_words = [word.lower() for word in words if self.min_length <= len(word) <= self.max_length]
        return set(filtered_words)  # Return unique words

    def save_wordlist(self, words):
        # Save the generated wordlist to a file
        try:
            with open(self.output_file, 'w') as f:
                for word in sorted(words):  # Sort words alphabetically
                    f.write(word + '\n')  # Write each word to a new line
            print(f"Wordlist created at: {self.output_file}")  # Inform the user of success
        except IOError:
            pass  # Ignore errors during file writing

    def generate(self):
        # Main method to generate the wordlist
        html_content = self.fetch_content()  # Fetch HTML content from the URL
        if html_content:  # Proceed if content was fetched successfully
            words = self.extract_words(html_content)  # Extract words from content
            if words:  # Save the wordlist if any words were extracted
                self.save_wordlist(words)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Wordlist Generator for Penetration Testing")
    parser.add_argument("url", help="The URL to scrape words from")  # URL to scrape
    parser.add_argument("--min", type=int, default=4, help="Minimum word length (default: 4)")  # Minimum word length
    parser.add_argument("--max", type=int, default=12, help="Maximum word length (default: 12)")  # Maximum word length
    parser.add_argument("--o", default="wordlist.txt", help="Output file for the wordlist (default: wordlist.txt)")  # Output file

    args = parser.parse_args()

    # Create and run the wordlist generator
    generator = WordlistGenerator(
        url=args.url,
        min_length=args.min,
        max_length=args.max,
        output_file=args.o
    )
    generator.generate()
