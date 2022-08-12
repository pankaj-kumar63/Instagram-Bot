import Accounts
from instapy import InstaPy

for i in range(0,len(Accounts.username)):
    session=InstaPy(username=Accounts.username[i],password=Accounts.password[i],headless_browser=True)
    session.login()

    # session.set_relationship_bounds(enabled=True, max_followers=500)
    #
    # session.set_do_follow(enabled=True, percentage=100, times=1)
    # session.follow_by_list(followlist=['shukla928'], times=1, sleep_delay=3, interact=False)

    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.set_do_like(True,percentage=100)
    session.like_by_users('shukla928',3,media='Photo')

    session.end()


