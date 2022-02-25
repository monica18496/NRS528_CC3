import os

os.mkdir("C:/draft_code")
os.mkdir("C:/draft_code/pending")
os.mkdir("C:/draft_code/complete")
os.mkdir("dir")
print(list)

os.rmdir("C:/draft_code/pending")
os.rmdir("C:/draft_code/complete")
os.rmdir("C:/draft_code")
os.rmdir("dir")
print(list)

os.mkdir("C:/includes")
os.mkdir("dir")
print(list)

os.rmdir("C:/includes")
os.rmdir("dir")
print(list)

os.mkdir("C:/layouts")
os.mkdir("C:/layouts/default")
os.mkdir("C:/layouts/post")
os.mkdir("C:/layouts/post/posted")
os.mkdir("dir")
print(list)

os.rmdir("C:/layouts/post/posted")
os.rmdir("C:/layouts/post")
os.rmdir("C:/layouts/default")
os.rmdir("C:/layouts")
os.rmdir("dir")
print(list)

os.mkdir("C:/site")
os.mkrdir("dir")
print(list)

os.rmdir("C:/site")
os.rmdir("dir")
print(list)
