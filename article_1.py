class Review:
    title = ''
    content = ''
    user = ''
    
    def __init__(self, content=content,  title=title, user=user):
        self.content= content
        self.title = title
        self.user = user
        
Review1 =Review(title="인셍영화이다", content="어쩌구 저쩌구111",user="나다")