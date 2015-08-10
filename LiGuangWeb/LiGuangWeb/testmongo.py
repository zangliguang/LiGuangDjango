import pymongo
__author__ = 'zangliguang'
# ¡¨Ω”mongodb≤‚ ‘
conn = pymongo.Connection("127.0.0.1", 27017)
db = conn.dbmeizi
db = conn.foo
content = db.meizi.find()
for i in content:
    print i
