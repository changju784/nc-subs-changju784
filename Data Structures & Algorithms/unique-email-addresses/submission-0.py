"""
Input: emails with local and domain names 
output: number of unique email after cleansing 
Cleansing 
split by domain and local names 
For local name 
    Skip dots 
    Ignore anything after + 
Assemble and push to set 
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set() 
        for email in emails: 
            address = email.split('@')
            local, domain = address[0], address[1]
            filtered_local = ''
            for c in local: 
                if c == '.':
                    continue 
                if c == '+':
                    break 
                filtered_local += c 
            result.add(filtered_local + '@' + domain)
        return len(result)
        