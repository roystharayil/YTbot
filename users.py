with open('info/email.txt', 'r') as f:
    users = f.readlines()
    
    for user in users:
        print(user.split(",")[0],user.split(",")[1])

