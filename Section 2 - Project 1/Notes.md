- Right click on .json file -> open in new Browser Tab to see the full json file
# 02_Code Explanation
# Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]  #list comphrension is used 
    # simpler version
    #The structure is: [ expression for item in iterable if condition ]
<!--- cleaned_users = []
    for user in data["users"]:
        if user["name"].strip():   # if user["name"].strip() has some value ot return true if its empty it return false {.strip() removes spaces /n and tab}
            cleaned_users.append(user)
     data["users"] = cleaned_users
--> 
# Remove duplicate friends
    for user in data["users"]:
        user['friends'] = list(set(user['friends']))
<!--  If a user has any duplicate names in their friends list, it removes those duplicates. It does this by converting the list to a set (which automatically removes duplicates) and then back to a list (since sets don’t keep items in list form). -->

# Remove inactive users
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]
<!--It goes through each user and keeps only those who are active — meaning they either have friends or have liked pages.
If both the friends list and liked_pages list are empty, the user is considered inactive and removed.-->

# Remove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data


<!-- It creates an empty dictionary called unique_pages.
Then, it goes through every page in data['pages'].
Each page is added to the dictionary using its id as the key.
If two pages have the same id, the later one replaces the earlier one.
Finally, it takes all the unique pages from the dictionary (just the values) and puts them back into data['pages'].-->

# 03_Do Chatgpt for explanation