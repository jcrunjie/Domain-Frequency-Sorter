import re
import socket

socket.setdefaulttimeout(1.0)

#pulling out ips and saving it to new_ips.txt
regex = re.compile("(\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})")
with open("new_ips.txt", "w") as w:
    with open("ips.txt", "r") as r:
        for line in r:
            result = regex.findall(line)
            for ip in result:
                    w.write(ip + "\n")

#resolving ips in new_ips.txt to hostnames
with open("resolved_hostnames.txt", "w") as w:
    with open("unresolved_ips.txt", "w") as w2:
        with open("domainOnly.txt", "w") as w3:
            with open("new_ips.txt", "r") as r:
                for line in r:
                    ip = line.rstrip()
                    try:
                        # removing leading zeros in ip
                        ip = ".".join([str(int(i)) for i in ip.split(".")])

                        #saving both IPs and their resolved domains to a file
                        w.write(f"{ip} resolves to {socket.gethostbyaddr(ip)[0]}" + "\n")

                        #saving only domains to a file 
                        w3.write(socket.gethostbyaddr(ip)[0] + "\n")
                    except:
                        #saving unresolved IPs to a file
                        w2.write(ip + "\n")