class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        PROBLEM STATEMENT:
        We are given a list cpdomains of count-paired domains. 
        We would like a list of count-paired domains, (in the same format as the input, and in any order),
        that explicitly counts the number of visits to each subdomain.
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        count = collections.Counter()
        for cpdomain in cpdomains:
            count_pair, domain = cpdomain.split()
            count_pair = int(count_pair)
            frags = domain.split('.')
            for i in range(len(frags)):
                count[".".join(frags[i:])] += count_pair

        return ["{} {}".format(cp, domain) for domain, cp in count.items()]
