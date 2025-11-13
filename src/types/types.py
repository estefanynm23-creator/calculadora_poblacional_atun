from typing import List, Tuple, Dict, Any

class TunaPopulationData:
    def __init__(self, year: int, population: float):
        self.year = year
        self.population = population

class BevertonHoltParameters:
    def __init__(self, R_max: float, K: float):
        self.R_max = R_max
        self.K = K

class PopulationGrowthResult:
    def __init__(self, years: List[int], populations: List[float]):
        self.years = years
        self.populations = populations

    def to_dict(self) -> List[Dict[str, Any]]:
        return [{"year": year, "population": population} for year, population in zip(self.years, self.populations)]