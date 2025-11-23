group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}
def max_age(group):
    return max(member["age"] for member in group.values())  
print(max_age(group))

def ave_relations(group):
    total_relations = sum(len(member["relations"]) for member in group.values())
    return total_relations / len(group)
print(ave_relations(group))

def rel_max_age(group):
    rel_over_1 = [member for member in group.values() if len(member["relations"]) >= 1]
    max_age_rel = max(member["age"] for member in rel_over_1)
    return max_age_rel   
print(rel_max_age(group))

def friend_max_age(group):
    friend = [member for member in group.values() if "friend" in member["relations"].values()]
    max_age_friend = max(member["age"] for member in friend)
    return max_age_friend
print(friend_max_age(group))

 

