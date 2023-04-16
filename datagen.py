import json
import random

# Define variables
num_users = 100
num_posts = 1000
num_topics = 50
max_followers = 80
max_likes = 75

# Generate user data
users = [{'id': i, 'followers': random.randint(0, max_followers)} for i in range(num_users)]

# Generate post data
posts = []
for i in range(num_posts):
    author_id = random.randint(0, num_users - 1)
    post = {
        'id': i,
        'author_id': author_id,
        'followers': users[author_id]['followers'],
        'likes': random.randint(0, max_likes),
        'topics': [random.randint(0, num_topics - 1) for _ in range(random.randint(1, 3))]
    }
    posts.append(post)

# Generate trend data
trends = [{'id': i, 'count': random.randint(1, 10)} for i in range(num_topics)]

# Print and save data
print('Users:')
print(users[:5])
print('Posts:')
print(posts[:5])
print('Trends:')
print(trends[:5])

data = {
    'users': users,
    'posts': posts,
    'trends': trends,
}

with open('data.json', 'w') as f:
    json.dump(data, f)
