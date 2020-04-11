import re
def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    lst  = [row.split(':') 
              for row in  passwd.strip().split('\n')
              ]
    
    user_names = {row[0].strip(','):re.sub(r"[,]+",' ', row[4]).strip() 
            for row in lst
            }
    for user in user_names:
      if user_names[user] == '':
        user_names[user] = 'unknown'

    return user_names
