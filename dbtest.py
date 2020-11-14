import pickledb

db = pickledb.load('daoc.db', False)
print(db.dgetall())
db.dump()