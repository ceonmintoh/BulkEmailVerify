# BulkEmailVerify
Verify emails in bulk for free
WARNING: DOING THIS WILL GET YOUR IP PUT IN THE SPAMHOUS POLICY BLACKLIST (IF IT IS NOT ALREADY LISTED). 

The Spamhaus Policy Block List (PBL) is a list of all dynamic IP addresses and some static IP addresses, and is not specifically a blocklist. IPs on the PBL are not listed for sending spam or for anything they have done.

1. Install python and required dependencies.

2. ******STUDY THE CSV FILE AND FORMAT THE DATA IN A SIMILAR MANNER. CSV MUST INCLUDE an "Email", "Website" and "Last Name" COLUMNS WITH THE EXACT SAME FORMAT.
I used this to guess company emails based on first and last name + domain. Thus domain should not contain "https://www." and it should only contain abc.com

3. Read your csv file - Edit this Line with the path to your file
![2022-07-05 11_15_10-Window](https://user-images.githubusercontent.com/84612798/177257797-ed14e560-7f7c-4871-b2c3-b988fca3d301.png)

4. Run verify-guessed.py
