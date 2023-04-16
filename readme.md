
## Overall inputs

n as the total number of users on the platform
m as the total number of posts on the platform
p as the number of posts made by a particular user
f as the number of followers a particular user has
l as the number of likes a particular post has
t as the topic(s) associated with a particular post

With these variables in mind, we can define the following equations:

The boost given to a post by a follower:

Bf = 1 + (f / n)

This equation gives a boost factor of 1 plus the ratio of the number of followers a particular user has (f) to the total number of users on the platform (n).

The boost given to a post by a share:

Bs = 2

This equation gives a boost factor of 2 to a post that has been shared.

The boost given to a post by a like:

Bl = 1 + (l / m)

This equation gives a boost factor of 1 plus the ratio of the number of likes a particular post has (l) to the total number of posts on the platform (m).

The boost given to a post by a topic:

Bt = 1 + (Ct / m)

This equation gives a boost factor of 1 plus the ratio of the number of posts on the platform that contain a particular topic (Ct) to the total number of posts on the platform (m).

With these equations in mind, we can calculate the overall boost factor for a particular post:

B = Bf * Bs * Bl * Bt

This equation multiplies the boost factors for each of the four variables we've defined. The resulting B value represents the overall boost factor for a particular post, taking into account its author's number of followers, the number of times it has been shared, the number of likes it has received, and the topics associated with it.

Finally, we can use this overall boost factor to calculate a post's rank on a particular user's feed:

R = log10(B)

This equation takes the logarithm (base 10) of the overall boost factor to obtain a numerical rank value R. This value can be used to sort and display posts in order of relevance on a user's feed, with posts having a higher R value appearing closer to the top.

## Sim Data Gen
users: an array of dictionaries representing each user on the platform, with their id and followers count.
posts: an array of dictionaries representing each post on the platform, with its id, author_id, followers count of the author, likes count, and a list of topics associated with it.
trends: an array of dictionaries representing the trending topics on the platform, with their id and count of associated posts.

## Sim 
This code loads the data from the data.json file, applies the math to calculate the boosts for each post, user, and trend, and then outputs some useful information based on the calculated boosts. The output includes the ID of the post with the biggest boost, the ID of the user with the highest overall average boost, and the ID of the trend that is doing the best. Note that the math used in this code is based on the math you provided earlier. If you want to use a different formula, you'll need to modify the code accordingly.