# Birthday Email Automation Script

## Overview
This Python script automates the process of sending personalized birthday emails to recipients listed in a CSV file (`birthdays.csv`). The email content is generated using a random birthday letter template, and it supports multiple email providers such as Gmail, Yahoo, Hotmail, and Outlook.

## Features
- Reads recipient data (name, birthday, email) from a CSV file.
- Selects a random birthday letter template and personalizes it.
- Sends the personalized birthday email using SMTP with encryption.

## Requirements
- Python 3.x
- Required libraries: `pandas`, `smtplib`, `random`, `datetime`
- A valid email account for sending emails (Gmail, Yahoo, Hotmail, Outlook)

## Files
- `birthdays.csv`: A CSV file containing recipient details (name, birthday, email).
- `letter_templates/`: A folder containing text files with the birthday letter templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).

## Usage
1. Update `my_email` and `password` variables with your email credentials.
2. Ensure the `birthdays.csv` file is in the correct format with the columns: `name`, `email`, `month`, `day`.
3. Run the script on the day you want to send the birthday emails.

## Example CSV Format:
```csv
name,email,month,day
John Doe,john@example.com,9,17
Jane Smith,jane@example.com,10,5
