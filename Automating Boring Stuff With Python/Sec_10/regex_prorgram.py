#! Python 3
import re
import pyperclip

# Create a Regex for Phone Numbers

phoneRegex = re.compile(r'''
(
((\d\d\d) | (\( (\d\d\d)))? # area code (optional)
(\s|-)            # first separator
\d\d\d              # first 3 digits
-                   # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s) | x)) # extension word-part (optional)
  (\d{2, 5}))?          # extension the number part (optional)
)
''', re.VERBOSE)

# Create a Regex for emails

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@               # At Symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# TO DO: Extract the phone numbers and emails from the copied text

extracedPhone = phoneRegex.findall(text)
extracedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extracedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# TO DO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extracedEmail)
print(results)
