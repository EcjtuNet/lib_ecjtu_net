from Model import *

class Token(db.Entity):
    user = Set("User")
    token = Required(str)
    last_use_time = Required(str)
