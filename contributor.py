class Contributor:
    """this is a class for contributors
        takes in name,
        takes in a dict of skills
    """
    def __init__(self, name: str, skills={}) -> None:
        self.name = name
        self.skills = skills

    def __str__(self) -> str:
        return f'name: {self.name}, skills: {self.skills}'
    
    def __repr__(self):
        return f'name: {self.name}, skills: {self.skills}'
       