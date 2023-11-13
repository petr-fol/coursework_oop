class Vacancy:
    def __init__(self, profession: str, url: str, salary_min: int, salary_max: int, currency: str, requirement: str
                 ) -> None:
        self.profession = profession
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.requirement = requirement

    def __str__(self):
        return f"{self.profession}\n{self.requirement}"
