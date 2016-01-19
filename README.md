# showmethediff
Project to scan the TOS at given urls and track the diff as they change. 

Big on keep it simple / low overhead - python flask or django with regular HTML templates. 


Google diff match patch for diffs.

Contributions on flow/structure welcome...
  
#Instructions:

*Clone into local repo.
*Install pip - it'll make your life easier. http://pip.readthedocs.org/en/stable/installing/
*Install virtualenv if not already available.
*cd /localrepo
*virtualenv env
*source env/bin/activate
*pip install -r requirements.txt
*python scraper.py

#Immediate 'to-do' list:

*Swap out SQLite3 for PostGres<
*Set up Google-Diff-Match-Patch API call https://code.google.com/p/google-diff-match-patch/
*Probably implement django_rq for queuing read jobs
*Cron job to start the queue
Parse the HTML to readable format


