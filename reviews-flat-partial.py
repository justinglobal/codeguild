class Review:
    def __init__(self, rating, review_text, username, business_name):
        self.rating = rating
        self.review_text = review_text
        self.username = usersname
        self.business_name = business_name
    def __repr__(self):
        return 'Review({}, {})'.format(self.rating, self.review_text)

class Business:
    def __init__(self, business_name):
        self.business_name = business_name
    def __repr__(self):
        return "Business({}, {})".format(self.business_name)
    def get_avg_rating(self):
        avg_list = []
        for review in self.reviews:
            avg_list.append(review.rating)
        print(statistics.mean(avg_list))

class User:
    def __init__(self, username):
        self.username = username
    def __repr__(self):
        return 'User({})'.format(self.rating, self.review_text)
