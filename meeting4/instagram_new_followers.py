import instaloader
import getpass

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

L = instaloader.instaloader()

username = input(" enter username instagram : ")
password = getpass.getpass(" enter password : ")


L.login(username, password)
print(" Login to the account was successful")

profile = instaloader.profile.from_username(L.context, "pishrorezanaseri")

new_followers= []
for follower in profile.get_followers():
    new_followers.append(follower)
  
for new_follow in new_followers:
    if new_follow not in old_followers:
        print(new_follow)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")

f.close()
