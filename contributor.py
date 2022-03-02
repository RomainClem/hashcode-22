class Contributor:
    """this is a class for contributors
        takes in index in list,
        takes in name,
        takes in a dict of skills
    """
    def __init__(self, index:int, name: str) -> None:
        self.index = index
        self.name = name
        self.skills = {}
        self.last_project_end = -1
        self.last_updated_skill = ""

    def __str__(self) -> str:
        return f'name: {self.name}, skills: {self.skills}'
    
    def __repr__(self):
        return f'name: {self.name}, skills: {self.skills}'
       