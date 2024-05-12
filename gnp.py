#!/usr/bin/python3

# Description: Simple password generator based on common password patterns

import argparse
import random
import string

def leet_convert(text):
    # Commented not commonly used
    leet_dict = {
        'A': '4',
        'B': '8',
        #'C': '<',
        'E': '3',
        #'G': '9',
        #'H': '#',
        'I': '1',
        'L': '|',
        'O': '0',
        'S': '$',
        #'T': '7',
        #'Z': '2',
        #'D': '|)',
        #'F': '|=',
        #'J': '_|',
        #'K': '|<',
        #'M': '|\\/|',
        #'N': '|\\|',
        #'P': '|>',
        #'Q': '(_,)',
        #'R': '|2',
        #'U': '|_|',
        #'V': '\\/',
        #'W': '\\/\\/',
        #'X': '><',
        #'Y': '`/',
        'A': '@',
    }

    converted_text = ""
    for char in text:
        if char.upper() in leet_dict:
            converted_text += leet_dict[char.upper()]
        else:
            converted_text += char

    return converted_text

def randomize_text(text):
    random_text = ""
    for char in text:
        if char.isupper():
            random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
            random_text += random_char
        else:
            random_text += char
    return random_text

def generate_all_passwords(company, season, start_year, end_year):
    placeholders = []
    for year in range(start_year, end_year + 1):
        placeholders.extend([
            f"{company}{year}",
            f"{season}{year}",
            f"{year}{company}",
            f"{year}{season}",
            f"{company}@{year}",
            f"{season}@{year}",
            f"{year}@{company}",
            f"{year}@{season}",
            f"{company}.{year}",
            f"{season}.{year}",
            f"{year}.{company}",
            f"{year}.{season}",
            leet_convert(f"{company}{year}"),
            leet_convert(f"{season}{year}"),
            leet_convert(f"{year}{company}"),
            leet_convert(f"{year}{season}"),
            leet_convert(f"{company}@{year}"),
            leet_convert(f"{season}@{year}"),
            leet_convert(f"{year}@{company}"),
            leet_convert(f"{year}@{season}"),
            leet_convert(f"{company}.{year}"),
            leet_convert(f"{season}.{year}"),
            leet_convert(f"{year}.{company}"),
            leet_convert(f"{year}.{season}"),
            randomize_text(f"{company}{year}"),
            randomize_text(f"{season}{year}"),
            randomize_text(f"{year}{company}"),
            randomize_text(f"{year}{season}"),
            randomize_text(f"{company}@{year}"),
            randomize_text(f"{season}@{year}"),
            randomize_text(f"{year}@{company}"),
            randomize_text(f"{year}@{season}"),
            randomize_text(f"{company}.{year}"),
            randomize_text(f"{season}.{year}"),
            randomize_text(f"{year}.{company}"),
            randomize_text(f"{year}.{season}"),
        ])
    return placeholders

def generate_company_passwords_years(company, start_year, end_year):
    placeholders = []
    for year in range(start_year, end_year + 1):
        placeholders.extend([
            f"{company}{year}",
            f"{year}{company}",
            f"{company}@{year}",
            f"{year}@{company}",
            f"{company}.{year}",
            f"{year}.{company}",
            leet_convert(f"{company}{year}"),
            leet_convert(f"{year}{company}"),
            leet_convert(f"{company}@{year}"),
            leet_convert(f"{year}@{company}"),
            leet_convert(f"{company}.{year}"),
            leet_convert(f"{year}.{company}"),
            randomize_text(f"{company}{year}"),
            randomize_text(f"{year}{company}"),
            randomize_text(f"{company}@{year}"),
            randomize_text(f"{year}@{company}"),
            randomize_text(f"{company}.{year}"),
            randomize_text(f"{year}.{company}"),
        ])
    return placeholders

def generate_season_passwords_years(season, start_year, end_year):
    placeholders = []
    for year in range(start_year, end_year + 1):
        placeholders.extend([
            f"{season}{year}",
            f"{year}{season}",
            f"{season}@{year}",
            f"{year}@{season}",
            f"{season}.{year}",
            f"{year}.{season}",
            leet_convert(f"{season}{year}"),
            leet_convert(f"{year}{season}"),
            leet_convert(f"{season}@{year}"),
            leet_convert(f"{year}@{season}"),
            leet_convert(f"{season}.{year}"),
            leet_convert(f"{year}.{season}"),
            randomize_text(f"{season}{year}"),
            randomize_text(f"{year}{season}"),
            randomize_text(f"{season}@{year}"),
            randomize_text(f"{year}@{season}"),
            randomize_text(f"{season}.{year}"),
            randomize_text(f"{year}.{season}"),
        ])
    return placeholders

def generate_common_passwords(company, season, year):
    placeholders = []
    placeholders.extend([
        f"{company}{year}",
        f"{season}{year}",
        f"{year}{company}",
        f"{year}{season}",
        f"{company}@{year}",
        f"{season}@{year}",
        f"{year}@{company}",
        f"{year}@{season}",
        f"{company}.{year}",
        f"{season}.{year}",
        f"{year}.{company}",
        f"{year}.{season}",
        leet_convert(f"{company}{year}"),
        leet_convert(f"{season}{year}"),
        leet_convert(f"{year}{company}"),
        leet_convert(f"{year}{season}"),
        leet_convert(f"{company}@{year}"),
        leet_convert(f"{season}@{year}"),
        leet_convert(f"{year}@{company}"),
        leet_convert(f"{year}@{season}"),
        leet_convert(f"{company}.{year}"),
        leet_convert(f"{season}.{year}"),
        leet_convert(f"{year}.{company}"),
        leet_convert(f"{year}.{season}"),
        randomize_text(f"{company}{year}"),
        randomize_text(f"{season}{year}"),
        randomize_text(f"{year}{company}"),
        randomize_text(f"{year}{season}"),
        randomize_text(f"{company}@{year}"),
        randomize_text(f"{season}@{year}"),
        randomize_text(f"{year}@{company}"),
        randomize_text(f"{year}@{season}"),
        randomize_text(f"{company}.{year}"),
        randomize_text(f"{season}.{year}"),
        randomize_text(f"{year}.{company}"),
        randomize_text(f"{year}.{season}"),
    ])
    return placeholders

def generate_company_passwords(company, year):
    placeholders = []
    placeholders.extend([
        f"{company}{year}",
        f"{year}{company}",
        f"{company}@{year}",
        f"{year}@{company}",
        f"{company}.{year}",
        f"{year}.{company}",
        leet_convert(f"{company}{year}"),
        leet_convert(f"{year}{company}"),
        leet_convert(f"{company}@{year}"),
        leet_convert(f"{year}@{company}"),
        leet_convert(f"{company}.{year}"),
        leet_convert(f"{year}.{company}"),
        randomize_text(f"{company}{year}"),
        randomize_text(f"{year}{company}"),
        randomize_text(f"{company}@{year}"),
        randomize_text(f"{year}@{company}"),
        randomize_text(f"{company}.{year}"),
        randomize_text(f"{year}.{company}"),
    ])
    return placeholders

def generate_season_passwords(season, year):
    placeholders = []
    placeholders.extend([
        f"{season}{year}",
        f"{year}{season}",
        f"{season}@{year}",
        f"{year}@{season}",
        f"{season}.{year}",
        f"{year}.{season}",
        leet_convert(f"{season}{year}"),
        leet_convert(f"{year}{season}"),
        leet_convert(f"{season}@{year}"),
        leet_convert(f"{year}@{season}"),
        leet_convert(f"{season}.{year}"),
        leet_convert(f"{year}.{season}"),
        randomize_text(f"{season}{year}"),
        randomize_text(f"{year}{season}"),
        randomize_text(f"{season}@{year}"),
        randomize_text(f"{year}@{season}"),
        randomize_text(f"{season}.{year}"),
        randomize_text(f"{year}.{season}"),
    ])
    return placeholders

def main():
    parser = argparse.ArgumentParser(description="Generate common passwords")
    parser.add_argument("-c", "--company", help="Company name")
    parser.add_argument("-s", "--season", help="Season name")
    parser.add_argument("-m", "--years", type=int, nargs=2, help="Start and end years")
    parser.add_argument("-y", "--year", type=int, help="Year number")
    args = parser.parse_args()

    if args.years is not None and args.year is not None:
        print("[-] Error: Cannot use -m/--years and -y/--year at the same time")
    elif args.years is None and args.year is None:
        print("[-] Error: Please specify a year with -y/--year or -m/--years")
    elif args.company and args.season and args.years is not None:
        start_year, end_year = args.years
        if start_year > end_year:
            print("[-] Error: Second year is lower than first year")
            exit
        placeholders = generate_all_passwords(args.company, args.season, start_year, end_year)
        for placeholder in placeholders:
            print(placeholder)
    elif args.company and args.years is not None:
        start_year, end_year = args.years
        if start_year > end_year:
            print("[-] Error: Second year is lower than first year")
            exit
        placeholders = generate_company_passwords_years(args.company, start_year, end_year)
        for placeholder in placeholders:
            print(placeholder)
    elif args.season and args.years is not None:
        start_year, end_year = args.years
        if start_year > end_year:
            print("[-] Error: Second year is lower than first year")
            exit
        placeholders = generate_season_passwords_years(args.season, start_year, end_year)
        for placeholder in placeholders:
            print(placeholder)
    elif args.company and args.season and args.year is not None:
        placeholders = generate_common_passwords(args.company, args.season, args.year)
        for placeholder in placeholders:
            print(placeholder)
    elif args.company is not None and args.season is None:
        placeholders = generate_company_passwords(args.company, args.year)
        for placeholder in placeholders:
            print(placeholder)
    elif args.company is None and args.season is not None:
        placeholders = generate_season_passwords(args.season, args.year)
        for placeholder in placeholders:
            print(placeholder)
    else:
        print("Usage:")
        print("Generate passwords all in one:")
        print("  gnp.py -c company_name -s season_name -m start_year end_year")
        print("Generate passwords based on company name and year range:")
        print("  gnp.py -c company_name -m start_year end_year")
        print("Generate passwords based on season name and year range:")
        print("  gnp.py -s season_name -m start_year end_year")
        print("Generate passwords based on company name and year:")
        print("  gnp.py -c company_name -y year")
        print("Generate passwords based on season name and year:")
        print("  gnp.py -s season_name -y year")

if __name__ == "__main__":
    main()