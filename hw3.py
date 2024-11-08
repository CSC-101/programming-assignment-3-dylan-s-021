build_data.getdata()

# Part 1
def population_total(county_demographics: list[data.CountyDemographics]) -> int:
    population_total = 0
    for i in county_demographics:
        population_total = population_total + county_demographics[i].population
    return population_total
