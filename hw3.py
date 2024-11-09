import build_data
import data
build_data.getdata()

# Part 1
# return the total population in a list of given counties
# input: a list of CountyDemographics
# output: the total population in all the counties from the given list of CountyDemographics
def population_total(county_demographics: list[data.CountyDemographics]) -> int:
    population_total = 0
    for i in range(len(county_demographics)):
        population_total = population_total + county_demographics[i].population['2014 Population']
    return population_total

# Part 2
# return counties in a specified state from a given list
# input: a list of CountyDemographics and a state abbreviation string
# output: a list of the CountyDemographics from the given list in the given state
def filter_by_state(county_demographics: list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:
    counties_in_state = []
    for i in range(len(county_demographics)):
        if county_demographics[i].state == state:
            counties_in_state.append(county_demographics[i])
    return counties_in_state

# Part 3
# return population at given education level given a list of counties
# input: a list of CountyDemographics and a string of an education key of interest
# output: the total sub-population across the counties in the given list with the education key given
def population_by_education(county_demographics: list[data.CountyDemographics], education_level:str) -> float:
    population = []
    education_percent = []
    pop_edu_level = 0
    for i in range(len(county_demographics)):
        if education_level in county_demographics[i].education:
            population.append(county_demographics[i].population['2014 Population'])
            education_percent.append(county_demographics[i].education[education_level])
            education_decimal = education_percent[i] / 100
            pop_edu_level = pop_edu_level + population[i] * education_decimal
        else:
            education_percent = 0
    return pop_edu_level

# return population of given ethnicity given a list of counties
# input: a list of CountyDemographics and a string of an ethnicity of interest
# output: the total sub-population across the counties in the given list with the ethnicity key given
def population_by_ethnicity(county_demographics: list[data.CountyDemographics], ethnicity:str) -> float:
    population = []
    ethnicity_percent = []
    pop_eth_level = 0
    for i in range(len(county_demographics)):
        if ethnicity in county_demographics[i].ethnicities:
            population.append(county_demographics[i].population['2014 Population'])
            ethnicity_percent.append(county_demographics[i].ethnicities[ethnicity])
            ethnicity_decimal = ethnicity_percent[i] / 100
            pop_eth_level = pop_eth_level + population[i] * ethnicity_decimal
        else:
            pop_eth_level = 0
    return pop_eth_level

# return number of people below poverty line from given list of counties
# input: a list of CountyDemographics
# output: the total population below the poverty level in all the counties in the given list
def population_below_poverty_level(county_demographics: list[data.CountyDemographics]) -> float:
    below_pov_level = 0
    for i in range(len(county_demographics)):
        below_pov_level = below_pov_level + county_demographics[i].income['Persons Below Poverty Level']
    return below_pov_level

# Part 4
# return percent of population at given education level given a list of counties
# input: a list of CountyDemographics and a string of an education key of interest
# output: the percent population across the counties in the given list with the education key given
def percent_by_education(county_demographics: list[data.CountyDemographics], education_level:str) -> float:
    percent_edu_level = 0
    for i in range(len(county_demographics)):
        if education_level in county_demographics[i].education:
            pop_edu_level = population_by_education(county_demographics, education_level)
            population = population_total(county_demographics)
            percent_edu_level = pop_edu_level / population * 100
        else:
            percent_edu_level = 0
    return percent_edu_level

# return percent of population of given ethnicity given a list of counties
# input: a list of CountyDemographics and a string of an ethnicity of interest
# output: the percent of population across the counties in the given list with the ethnicity key given
def percent_by_ethnicity(county_demographics: list[data.CountyDemographics], ethnicity:str) -> float:
    percent_eth_level = 0
    for i in range(len(county_demographics)):
        if ethnicity in county_demographics[i].ethnicities:
            pop_eth_level = population_by_ethnicity(county_demographics, ethnicity)
            population = population_total(county_demographics)
            percent_eth_level = pop_eth_level / population * 100
        else:
            percent_eth_level = 0
    return percent_eth_level

# return percent of people below poverty line from given list of counties
# input: a list of CountyDemographics
# output: the percent of population below the poverty level in all the counties in the given list
def percent_below_poverty_level(county_demographics: list[data.CountyDemographics]) -> float:
    below_pov_level = population_below_poverty_level(county_demographics)
    population = population_total(county_demographics)
    percent_below_pov_level = below_pov_level / population * 100
    return percent_below_pov_level

# Part 5
# list the counties with a given education level greater than a given threshold value
# input: a list of CountyDemographics, a string of an education key, a float threshold value
# output: a list of CountyDemographics for which the given education key is greater than the given threshold value
def education_greater_than(county_demographics: list[data.CountyDemographics], education_level:str, threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].education[education_level] > threshold:
            new_list.append(county_demographics[i])
    return new_list

# list the counties with a given education level less than a given threshold value
# input: a list of CountyDemographics, a string of an education key, a float threshold value
# output: a list of CountyDemographics for which the given education key is less than the given threshold value
def education_less_than(county_demographics: list[data.CountyDemographics], education_level:str, threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].education[education_level] < threshold:
            new_list.append(county_demographics[i])
    return new_list

# list the counties with a given ethnicity greater than a given threshold value
# input: a list of CountyDemographics, a string of an ethnicity key, a float threshold value
# output: a list of CountyDemographics for which the given ethnicity key is greater than the given threshold value
def ethnicity_greater_than(county_demographics: list[data.CountyDemographics], ethnicity:str, threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].ethnicities[ethnicity] > threshold:
            new_list.append(county_demographics[i])
    return new_list

# list the counties with a given ethnicity less than a given threshold value
# input: a list of CountyDemographics, a string of an ethnicity key, a float threshold value
# output: a list of CountyDemographics for which the given ethnicity key is less than the given threshold value
def ethnicity_less_than(county_demographics: list[data.CountyDemographics], ethnicity:str, threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].ethnicities[ethnicity] < threshold:
            new_list.append(county_demographics[i])
    return new_list

# list the counties with people below the poverty level greater than a given threshold value
# input: a list of CountyDemographics, a float threshold value
# output: a list of CountyDemographics for which the Persons Below Poverty Level key is greater than the given threshold value
def below_poverty_level_greater_than(county_demographics: list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].income["Persons Below Poverty Level"] > threshold:
            new_list.append(county_demographics[i])
    return new_list

# list the counties with people below the poverty level less than a given threshold value
# input: a list of CountyDemographics, a float threshold value
# output: a list of CountyDemographics for which the Persons Below Poverty Level key is less than the given threshold value
def below_poverty_level_less_than(county_demographics: list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in range(len(county_demographics)):
        if county_demographics[i].income["Persons Below Poverty Level"] < threshold:
            new_list.append(county_demographics[i])
    return new_list
