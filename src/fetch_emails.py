import imaplib, email

IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "testprojectx22x26@gmail.com"
EMAIL_PASSWORD = "test_test*44"

def fetch_unread_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select("inbox")
    status, messages = mail.search(None, '(UNSEEN)')
    email_ids = messages[0].split()

    emails = []
    for eid in email_ids:
        status, data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        emails.append({
            "subject": msg["subject"],
            "from": msg["from"],
            "body": get_body(msg)
        })
    return emails

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

if __name__ == "__main__":
    print(fetch_unread_emails())
