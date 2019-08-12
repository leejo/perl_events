import sys
sys.path.append('/Users/lee/working/InstaPy/assets')

from instapy import InstaPy

insta_username = ''
insta_password = ''

for line in open( '/Users/lee/working/.perl_events_instagram_bot.cred' ):
    if insta_username == '':
        insta_username = line.rstrip()
    else:
        insta_password = line.rstrip()

# set headless_browser=True if you want to run InstaPy on a server
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=True
)
session.login()

# don't use the relationship bounds check
session.set_relationship_bounds(
    enabled=False
)

session.set_delimit_liking(
    enabled=True,
    max=300, min=0
)

# follow everyone we like
session.set_do_follow(
    enabled=True,
    percentage=100,
    times=2
)

# unfollow users who don't follow us
session.unfollow_users(
    amount=1000,
    nonFollowers=True,
    style="RANDOM",
    sleep_delay=60,
)

# note - keep sum of all likes to < 300 per hour

# like all photos with these tags
session.like_by_tags(
    [
        # perl!
        'perl5',
        'perl6',

        # the rest
        'coding',
        'codingbootcamp',
        'computerengineering',
        'computerprogramming',
        'computing',
        'cprogramming',
        'creativecoding',
        'development',
        'erlang',
        'girlswhocode',
        'github',
        'golang',
        'hack',
        'hacker',
        'java',
        'javascript',
        'linux',
        'opensource',
        'php',
        'programmer',
        'programming',
        'programminglanguage',
        'programminglanguages',
        'programminglife',
        'programmingstudents',
        'python',
        'rubyprogramming',
        'software',
        'softwaredeveloper',
        'softwaredevelopers',
        'softwaredevelopment',
        'softwareengineer',
        'softwareengineering',
        'softwareengineers',
        'softwares',
        'startup',
        'tech',
        'webdevelopment',
        'webprogramming',
        'womenintech',
        'womenwhocode',
    ],
    skip_top_posts=True,
    amount=19
)

# end the bot session
session.end()
