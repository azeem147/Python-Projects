import re
namesRegex = re.compile(r'Agent \w+')
message = 'Agent Alice gave a secret document to Agent Bob'
print(namesRegex.findall(message))
# sub method will not only find but also replace whatever is found
print(namesRegex.sub('REDACTED', message))
