# import imapclient
import imapclient
# import pyzmail for parsing fetch
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('Your Email', 'Your App Pasword')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2018'])
# Watch the video again for how to fetch the email from UIDs
message = pyzmail.PyzMessage.factory(rawMessage['replace it with UID'] ['replace it byte value'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
# watch the rest of the video later.
