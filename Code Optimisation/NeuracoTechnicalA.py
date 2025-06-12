# Refactor this code from Neuro Technical Interview
class userManager:
    def __init__(self):
        self.users = []
        self.admins = []
    
    def add_user(self,name,age,email,admin=False):
        # adds a user to the system
        if not name or not age or not email or age < 0:
            return False
        user = {'name':name,'age':age,'email':email}
        (self.admins if admin == True else self.users).append(user)
        return True
    
    def get_user(self,email):
        # gets a user from the system
        for user_group in (self.users, self.admins):
            for user in user_group:
                if user['email'] == email:
                    return user
        return None
    
    def delete_user(self,email):
        for usergroup in (self.users, self.admins):
            user = next((u for u in usergroup if u['email'] == email), None)
        if user:
            usergroup.remove(user)
            return True
        return False

def process_user_data(users_list):
    return [
        {
            'name': u.get('name', ''),
            'email': u['email'],
            'age': u.get('age', 0),
            'status': 'active'
        }
        for u in users_list
        if u.get('active') and u.get('age', 0) >= 18 and u.get('email')
    ]