class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdict = {}
        output = []
        for entry in cpdomains:
            count = int(entry.split(' ')[0])
            domains = []
            parts = entry.split(' ')[1].split('.')
            for i in range(len(parts)):
                domains.append(".".join(parts[i:]))
            for domain in domains:
                if domain in cpdict.keys():
                    cpdict[domain] += count
                else:
                    cpdict[domain] = count
        for domain, count in cpdict.items():
            output.append(" ".join([str(count), domain]))
        return output
