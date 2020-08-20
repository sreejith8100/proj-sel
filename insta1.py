from instapy import InstaPy

session=InstaPy(username="sreejith_81", password="sreejith@8100")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
