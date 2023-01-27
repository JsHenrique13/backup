import imaplib
import email




m = imaplib.IMAP4("mail.ita.locaweb.com.br", 993)
m.login("teste@camarapedrabranca.ce.gov.br","Teste@ssesi00")
m.select("Inbox")

result, data = m.uid('search', None, "ALL") # search all email and return uids
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            email_message = email.message_from_string(data[0][1])    # raw email text including headers
            print ('From:' + email_message['subject'] )

m.close()
m.logout()



"""import sys, os
import chilkat


imap = chilkat.CkImap()

imap.put_Ssl(False)
imap.put_Port(993)
success = imap.Connect("mail.ita.locaweb.com.br")
if (success != True):
    print(imap.lastErrorText())
    sys.exit()

# Login
success = imap.Login("teste@camarapedrabranca.ce.gov.br", "Teste@ssesi00")
if (success != True):
    print(imap.lastErrorText())
    sys.exit()



sbMime = chilkat.CkStringBuilder()
arquivo = "Inbox/b_141_.eml"
open(arquivo, "+rb")
sbMime.LoadFile(arquivo, "utf-8")

# Upload to the mailbox.
success = imap.AppendMime("INBOX" ,sbMime.getAsString())
if (success != True):
    print(imap.lastErrorText())
    sys.exit()

imap.Disconnect()

print("OK.")"""