
class Recipe:
    def __init__(
        self,
        title = "",
        description = "",
        difficulity = "",
        
        ):
        self.title = title
        self.description = description
        self.difficulity = difficulity
      
    def to_dict(self):
        return{
            'title':self.title,
            'description':self.description,
            'difficulity':self.difficulity

        }