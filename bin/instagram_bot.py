import sys
sys.path.append('../../InstaPy')

from instapy import InstaPy

insta_username = ''
insta_password = ''

for line in open( '../../.perl_events_instagram.cred' ):
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

# follow everyone we like
session.set_do_follow(
    enabled=True,
    percentage=100,
    times=2
)

# unfollow users who don't follow us
session.unfollow_users(
    amount=750,
    onlyNotFollowMe=True,
    onlyInstapyMethod='FIFO',
    sleep_delay=60
)

# but don't unfollow if they've liked one of our last 3 posts
session.set_dont_unfollow_active_users(
    enabled=True,
    posts=3
)

# note - keep sum of all likes to < 300 per hour

try:
    # like all photos with these tags
    session.like_by_tags(
        [
            # perl!
            'perl5',
            'perl6',

            # the rest
            'coding',
            'codingbootcamp',
            'codingisfun',
            'codinglife',
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
            'programmingisfun',
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
        skip_top_posts=False,
        amount=25
    )
except:
    print "Problem liking tags"

# end the bot session
session.end()
