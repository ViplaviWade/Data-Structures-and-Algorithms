def find_user_by_id(users, user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None
