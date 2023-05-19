class News:
    def __init__(self, username, headline, body):
        self.username = username
        self.headline = headline
        self.body = body

class Newsletter:
    def __init__(self):
        self.news = []
    # I will do the methods here to insert news
    def addPost(self, username, headline, body):
        newPost = News(username, headline, body)
        self.news.append(newPost)

    def getPosts(self):
        if len(self.news) > 0:
            text = '['
            #yes there posts
            for i in self.news:
                text += "\n{\"username\":\""+i.username+"\",\n\"headline\":\""+i.headline+"\",\n\"body_post\":\""+i.body+"\"},"
            text = text[:-1]
            text+='\n]'
            print(len(text))
            return text
        else:
            text='[\n]'
            # print(len(text))
            #length of 3
            return text