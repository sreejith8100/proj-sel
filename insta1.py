from instapy import InstaPy

session=InstaPy(username="user", password="pass") #enter username and password
session.login()
session.like_by_tags(["tag1", "tag2"]) #likes 4 posts of each tag by default
