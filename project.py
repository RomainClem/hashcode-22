class Project:
    """this is a class for project
        takes in name,
        takes in duration in days,
        takes in score,
        takes in best before time in days,
        takes in a dict of skills
    """
    def __init__(self, name: str, duration: int, score: int, best_before: int) -> None:
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.skills = []

    def __str__(self) -> str:
        return f'name: {self.name}, duration: {self.duration}, ' \
        f'score: {self.score}, best_before: {self.best_before}, skills: {self.skills}'
    
    def __repr__(self):
        return f'name: {self.name}, duration: {self.duration}, ' \
        f'score: {self.score}, best_before: {self.best_before}, skills: {self.skills}'
       