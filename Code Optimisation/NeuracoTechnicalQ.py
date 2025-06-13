class userManager:
    def __init__(self):
        self.users = []
        self.admins = []
    
    def Add_user(self,name,age,email,admin=False):
        # adds a user to the system
        if name == '' or age == '' or email == '':
            return False
        if age < 0: return False
        user = {'name':name,'age':age,'email':email}
        try:
            if admin == True:
                self.admins.append(user)
                return True
            else:
                self.users.append(user)
                return True
        except:
            return False
    
    def get_user(self,email):
        # gets a user from the system
        for u in self.users:
            if u['email'] == email:
                return u
        for a in self.admins:
            if a['email'] == email:
                return a
        return None
    
    def delete_user(self,email):
        u = self.get_user(email)
        if u in self.users:
            self.users.remove(u)
            return True
        if u in self.admins:
            self.admins.remove(u)
            return True
        return False

def process_user_data(users_list):
    processed = []
    for i in range(len(users_list)):
        u = users_list[i]
        if u.get('active') == True:
            if u.get('age', 0) >= 18:
                if u.get('email') != None and u.get('email') != '':
                    processed.append({
                        'name': u.get('name', ''),
                        'email': u.get('email'),
                        'age': u.get('age', 0),
                        'status': 'active'
                    })
    return processed