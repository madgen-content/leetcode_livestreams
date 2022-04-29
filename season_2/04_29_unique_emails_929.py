from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        canon_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            canon_email = '@'.join([local, domain])
            canon_emails.add(canon_email)
        
        return len(canon_emails)