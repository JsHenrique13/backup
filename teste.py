import sys, os
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

imap.CreateMailbox("BACKUP")
"""
sbMime = chilkat.CkStringBuilder()
arquivo = f"Inbox/b'131'.eml"
open(arquivo, "+rb")
sbMime.LoadFile(arquivo, "utf-8")

# Upload to the mailbox.
success = imap.AppendMime("INBOX/BACKUP" ,sbMime.getAsString())
if (success != True):
    print(imap.lastErrorText())
    sys.exit()
"""
imap.Disconnect()

print("OK.")