
#Google Lightweight Automated Search Hacking (gooLASH)

## UNDER CONSTRUCTION

GooLASH (Hungarian: gulyás [ˈɡujaːʃ]) is a lightweight, Python-based tool designed to simplify the Google Dorking during the reconaissance phase of penetration tests. Google dorks are scraped from Exploit Database's Google Hacking Database (GHDB) (https://www.exploit-db.com/google-hacking-database/) and are automatically checked against your target URL. I see this tool being a useful resource for both penetration testers and bug bounty hunters.

 ## Motivation
There are similar solutions, namely GooDork, however, these are either no longer maintained, or require too much manual intervention. The goal of GooLASH is to be Automated (hence the A in the name). All that you need to provide is the target URL and GooLASH will handle the rest, brute forcing different Google dorks, and providing you with an easy to read report. 

 ## Use
* **update.py** - should be  used to scrape exploit-db's GHDB
* **goolash.py** - should be used to actually run the tool

 ## Contributors
* [Chase Miller](https://github.com/cnmiller) - @psuchase
