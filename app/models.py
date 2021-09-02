class Source:
    '''
     This is the source class that defines News Source Objects
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name =name
        self.description =description
        self.url =url
        self.category =category
        self.country =country


class Article:
    '''
    This is the article class that defines News Articles Objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
