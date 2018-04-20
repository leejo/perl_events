# Perl Events Instagram

This is a repo for the [Perl Events](https://www.instagram.com/perl_events/)
Instagram account. What we have here is a script to automatically like and
follow various other programming related Instagram accounts in the hope that
they will follow us back and see the various Perl related events that are
happening

### Setup

The script can be found in the `bin/` directory, you will need the [InstaPy](https://github.com/timgrossmann/InstaPy)
library installed one level up relative to this checkout and and a recent
version of python2 as a prerequisite. You will also need the latest [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
installed in the InstaPy checkout at `InstaPy/assets/chromedriver`

You will finally need to create a .perl\_events\_instagram.cred file
in the directory above this checkout which contains:

```
perl_events
$perl_events_password
```

You will need to contact [leejo](https://github.com/leejo) or Sawyer for
the perl\_events Instagram password

### Running

To run the script:

```
cd bin/
/path/to/your/python ./instagram_bot.py >> logs/bot.txt 2>&1 &
```

Add the script to your cron and run it once a day, maybe twice a day and
hopefully the number of followers will start to increase. As of the first
commit of this repo we are currently at:

* 50 publications
* 106 abonnés
* 196 suivis
