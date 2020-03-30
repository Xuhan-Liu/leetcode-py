from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        _map = dict()
        for i in range(len(cpdomains)):
            [count, domains] = cpdomains[i].split(' ')
            domains = domains.split('.')
            while len(domains) > 0:
                domain = '.'.join(domains)
                _map[domain] = _map.get(domain, 0) + int(count)
                domains = domains[1:]
        result = []
        for k, v in _map.items():
            result.append(f'{v} {k}')
        return result
