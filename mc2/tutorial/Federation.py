from pymongo import MongoClient
from os.path import expanduser

db_username = "xgboost"
db_password = "risecampmc2"

class PKI:
    def __init__(self):
        self.client = MongoClient('mongodb://%s:%s@54.202.14.46:27017/risecampPKI' % (db_username, db_password))
        self.db = self.client['risecampPKI']

    def upload_key(self, username, IP):
        try:
            # TODO determine IP address automatically
            posts = self.db.posts
            home = expanduser("~")
            pubkey = open(home + '/.ssh/id_rsa.pub').read().strip()
            post_data = {
                'user': username,
                'IP': IP,
                'key': pubkey
                }
            result = posts.insert_one(post_data)
        except Exception as e:
            print(str(e))

    def lookup(self, username):
        try:
            posts = self.db.posts
            query = { 
                    'user': username 
                    }
            # FIXME currently assumes only a single entry per username
            result = posts.find_one(query)
            if result == None: 
                print("No such user found") 
                return None, None
            else: 
                return result['IP'], result['key']
        except Exception as e:
            print(str(e))



class Federation:
    def __init__(self):
        self.client = MongoClient('mongodb://%s:%s@54.202.14.46:27017/risecampfederations' % (db_username, db_password))
        self.db = self.client['risecampfederations']

    def create_federation(self, master_username, members):
        try:
            if master_username in members:
                members.remove(master_username)

            collection = self.db.federations
            doc = { 
                    { 'master': master_username },
                    { 'master': master_username, 'members': members },
                    { 'upsert': True }
                    }
            # FIXME make sure 'master' is a primary key
            result = collection.update(doc)
        except Exception as e:
            print(str(e))
        
    def join_federation(self, username, master_username):
        try:
            collection = self.db.members
            doc = { 
                    'member': username,
                    'federation': master_username
                    }
            # FIXME make sure 'user' is a primary key
            result = collection.insert_one(doc)
        except Exception as e:
            print(str(e))

    def check_federation(self, master_username):
        try:
            collection = self.db.federations
            query = {
                    'master' : master_username,
                    }
            result = collection.find_one(query)
            if result == None:
                print("No such federation exists")
                return False
            members = result['members']
            print(members)

            collection = self.db.members
            for member in members:
                query = {
                        'member': member,
                        'federation': master_username
                        }
                if collection.count_documents(query, limit = 1) == 0:
                    return False
            return True
        except Exception as e:
            print(str(e))

