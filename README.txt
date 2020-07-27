Description:
This is a python CTF challenge project done during my internship

Tool Summary:
This is a tool that takes in a file with IPv4 addresses, resolves the IPs to hostnames or domains, 
and sorts and displays the occurrence of the domains from most frequent to least frequent

Usage:
- First, run the ipChallenge.py to resolve a list of IPs to hostnames/domains. 
(the IP list is currently built into the script and if you wish to run the script on a different list you need to change that in the code)

- Once the ipChallenge.py script finishes running, run the domainSort.py to sort the hostnames/domains by their occurrence frequency

- Check the sortedDomains.txt for the end result

Note:
- The reason why I made two separate scripts instead of one is because the ipChallenge.py can take hours to run depending on the number of IP inputs. 
Therefore, I created the domainSort.py as a separate script for demo purposes. 
If you do not wish to wait hours for the ipChallenge.py, 
you can still test the performance of domainSort.py by running it on domainOnly_sample.txt, 
which is a sample of the resolved domains.

- I have also prepared other sample outputs as a result of running the ipChallenge.py for testing purposes

- To test the scripts using the sample files, be sure to change the filenames in the respective scripts to the sample file names

- In the future, I will add input functionality so that the user doesn't have to manually change the code to run the scripts on different files 
