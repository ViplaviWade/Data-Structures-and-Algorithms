def find_user_by_id(users, user_id):
    return next((user for user in users if user['id'] == user_id ), None)
