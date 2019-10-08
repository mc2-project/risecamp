from pymongo import MongoClient
from os.path import expanduser

db_username = "xgboost"
db_password = "risecampmc2"

class PKI:
    def __init__(self):
        self.client = MongoClient('mongodb://%s:%s@54.202.14.46:27017/PKI' % (db_username, db_password))
        self.db = self.client['PKI']


    def upload(self, username, IP, pubkey):
        try:
            collection = self.db.posts
            query = \
            { 
                    'user': username
            }
            doc = \
            { 
                    'user': username, 
                    'IP': IP, 
                    'key': pubkey 
            }
            result = collection.find_one_and_replace(query, doc, upsert=True)
            print(result)
        except Exception as e:
            print(str(e))


    def lookup(self, username):
        try:
            posts = self.db.posts
            query = { 
                    'user': username 
                    }
            result = posts.find_one(query)
            if result == None: 
                print("User %s not found" % username) 
                return None, None
            else: 
                return result['IP'], result['key']
        except Exception as e:
            print(str(e))

    
    def save_key(self, username):
        try:
            IP, key = self.lookup(username)
            if key == None:
                return
            home = expanduser("~")
            with open(home + "/.ssh/authorized_keys", "a") as authorized_keys:
                authorized_keys.write("%s\n" % key)
                print("Saved key for user %s" % username)
        except Exception as e:
            print(str(e))


class Federation:
    def __init__(self, username):
	self.client = MongoClient('mongodb://%s:%s@54.202.14.46:27017/Federations' % (db_username, db_password))
	self.db = self.client['Federations']
	self.username = username
	self.aggregator = None


    def check_federation(self):
        if self.aggregator is None:
            print("No federation to check. Please create or join a federation first.")
            return

	try:
	    collection = self.db.federations
	    query = \
	    {
		    'master' : self.aggregator,
	    }
	    result = collection.find_one(query)
	    if result == None:
		print("No such federation exists")
		return False

	    members = result['members']
	    print("Federation members: %s" % members)

	    collection = self.db.members
	    for member in members:
		query = \
		{
			'member': member,
			'federation': self.aggregator
		}
		if collection.count_documents(query, limit = 1) == 0:
		    print("User %s has not joined the federation" % member)
		    return False
	    print("All users have joined the federation")
	    return True
	except Exception as e:
	    print(str(e))


class FederationAggregator(Federation):
    def __init__(self, username):
	Federation.__init__(self, username)
	self.aggregator = username


    def create_federation(self, members):
	try:
	    if self.username not in members:
		members.append(self.username)

	    collection = self.db.federations
	    query = \
	    { 
		    'master': self.username 
	    }
	    doc = \
	    { 
		    'master': self.username, 
		    'members': members 
	    }
	    result = collection.find_one_and_replace(query, doc, upsert=True)
	    print(result)


	    collection = self.db.members
	    query = \
	    { 
		    'member': self.username 
	    }
	    doc = \
	    { 
		    'member': self.username,
		    'federation': self.username,
		    'role': 'master'
	    }
	    result = collection.find_one_and_replace(query, doc, upsert=True)
	except Exception as e:
	    print(str(e))


class FederationMember(Federation):
    def __init__(self, username):
	Federation.__init__(self, username)


    def join_federation(self, master_username):
        try:

            collection = self.db.federations
            query = \
            { 
                    'master': master_username,
                    'members': {'$all': [self.username]}

            }
            result = collection.find_one(query)
            if result == None:
                print("Either the federation does not exist, or the central server (aggregator) hasn't added you as a member.")
                return

            self.aggregator = master_username

            collection = self.db.members
            query = \
            { 
                    'member': self.username 
            }
            doc = \
            { 
                    'member': self.username,
                    'federation': master_username,
                    'role': 'worker'
            }
            result = collection.find_one_and_replace(query, doc, upsert=True)
            print(result)
            
        except Exception as e:
            print(str(e))

