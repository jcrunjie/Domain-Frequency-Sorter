#creating a dictionary that will map domain names to their occurance
counts = dict()

with open("domainOnly.txt", "r") as r:
    for i in r:

        #extracting domain.tdl from subdomains
        domain = i.rstrip().split('.')
        try:
            #for domains with subdomains
            domainTLD = domain[-2]+"."+domain[-1]
        except:
            #for domains without subdomains
            domainTLD = domain[-1]

        #counting domain occurances
        if domainTLD in counts:
            counts[domainTLD] = counts[domainTLD] + 1
        else:
            counts[domainTLD] = 1
            
#sorting the domain occurances from highest to lowest
sort = sorted(counts.items(), key=lambda x: x[1], reverse=True)
with open("sortedDomains.txt", "w") as w:
    for i in sort:
        w.write(f"{i[0]} showed up {i[1]} times" + "\n")