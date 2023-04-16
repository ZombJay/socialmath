import json

# Load data from file
with open('data.json', 'r') as f:
    data = json.load(f)

users = data['users']
posts = data['posts']
trends = data['trends']

# Apply the math
user_boosts = {}
trend_boosts = {}

for post in posts:
    # Calculate user boost
    user_id = post['author_id']
    user_followers = users[user_id]['followers']
    post_followers = post['followers']
    post_likes = post['likes']
    user_boost = (1 + post_followers) * (1 + post_likes) * user_followers
    if user_id not in user_boosts:
        user_boosts[user_id] = []
    user_boosts[user_id].append(user_boost)

    # Calculate trend boost
    for trend_id in post['topics']:
        if trend_id not in trend_boosts:
            trend_boosts[trend_id] = []
        trend_boosts[trend_id].append(user_boost)

# Output useful information
max_post_boost = max(posts, key=lambda x: (1 + x['followers']) * (1 + x['likes']))
print(f"The post with ID {max_post_boost['id']} has the biggest boost")

max_user_avg_boost = max(user_boosts.items(), key=lambda x: sum(x[1])/len(x[1]))
print(f"User with ID {max_user_avg_boost[0]} has the highest overall average boost")

max_trend_boost = max(trend_boosts.items(), key=lambda x: sum(x[1]))
print(f"Trend with ID {max_trend_boost[0]} is doing the best")
