# Wordlists_Generator
A Python-based tool for penetration testing, designed to generate custom wordlists by scraping words from a specified URL. The tool supports flexible configuration for word length limits and output file naming.

#Features
Fetch words directly from a given URL.
Filter words based on a specified minimum and maximum length.
Save the generated wordlist to a text file.
Simple command-line interface for customization.

#Installation
Prerequisites
Ensure you have Python 3.x installed on your system. Additionally, install the required Python libraries:

```
pip install requests beautifulsoup4
```

#Usage
Run the tool directly from the command line. Below are the available options:

```
python wordlist_generator.py <URL> [--min <min_length>] [--max <max_length>] [--o <output_file>]
```

#Arguments
<URL>: The URL to scrape words from (required).
--min: Minimum word length (default: 4).
--max: Maximum word length (default: 12).
--o: Output file for the wordlist (default: wordlist.txt).

#Example

```
python wordlist_generator.py https://example.com --min 5 --max 15 --o my_wordlist.txt
```

This command will:
Scrape words from https://example.com
Include words with lengths between 5 and 15 characters.
Save the wordlist to my_wordlist.txt.

#Output
The generated wordlist will contain unique, lowercase words sorted alphabetically.

#File Structure
```.
├── wordlist_generator.py  # The main script file
├── requirements.txt       # Dependencies required to run the script
```

#Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for new features or bug fixes.

#License

This project is licensed under the MIT License. See the LICENSE file for details.

#Contact
If you have any questions or suggestions, feel free to contact me:
GitHub: Nulish
