import random

# -- Cities

# COLOMBO_CITY
# Greater Colombo
# South Coast
# East Coast,
# High Country
# Ancient Cities
# Northern Regions

# -- Monthly
COLOMBO_CITY_MIN = 172763
COLOMBO_CITY_MIN = 206873

GREATER_COLOMBO_MIN = 188116
GREATER_COLOMBO_MAX = 136116

SOUTH_COAST_MIN = 284002
SOUTH_COAST_MAX = 369824

EAST_COST_MIN = 32964
EAST_COST_MAX = 206873

HIGH_COUNTRY_MIN = 39710
HIGH_COUNTRY_MAX = 48342

ANCIENT_CITIES_MIN = 128867
ANCIENT_CITIES_MAX = 164165

NORTHERN_REGIONS_MIN =  1889
NORTHERN_REGIONS_MAX =  2226

# -- Monthly Predictions --

def getColomboCityMonthlyPredictions():
    return random.randint(COLOMBO_CITY_MIN,COLOMBO_CITY_MIN)

def getGreaterColomboMonthlyPredictions():
    return random.randint(GREATER_COLOMBO_MIN,GREATER_COLOMBO_MAX)

def getSouthCoastMonthlyPredictions():
    return random.randint(SOUTH_COAST_MIN,SOUTH_COAST_MAX)

def getEastCoastMonthlyPredictions():
    return random.randint(EAST_COST_MIN,EAST_COST_MAX)

def getHighCountryMonthlyPredictions():
    return random.randint(HIGH_COUNTRY_MIN,HIGH_COUNTRY_MAX)

def getAncientCitiesMonthlyPredictions():
    return random.randint(ANCIENT_CITIES_MIN,ANCIENT_CITIES_MAX)

def getNorthernRegionsMonthlyPredictions():
    return random.randint(NORTHERN_REGIONS_MIN,NORTHERN_REGIONS_MAX)

# -- Daily Predictions --

def getColomboDailyPredictions():
    return random.randint(int(COLOMBO_CITY_MIN/30),int(COLOMBO_CITY_MIN/30))

def getGreaterColomboDailyPredictions():
    return random.randint(int(GREATER_COLOMBO_MIN/30),int(GREATER_COLOMBO_MAX/30))

def getSouthCoastDailyPredictions():
    return random.randint(int(SOUTH_COAST_MIN/30),int(SOUTH_COAST_MAX/30))

def getEastCoastDailyPredictions():
    return random.randint(int(EAST_COST_MIN/30),int(EAST_COST_MAX/30))

def getHighCountryDailyPredictions():
    return random.randint(int(HIGH_COUNTRY_MIN/30),int(HIGH_COUNTRY_MAX/30))

def getAncientCitiesDailyPredictions():
    return random.randint(int(ANCIENT_CITIES_MIN/30),int(ANCIENT_CITIES_MAX/30))

def getNorthernRegionsDailyPredictions():
    return random.randint(int(NORTHERN_REGIONS_MIN/30),int(NORTHERN_REGIONS_MAX/30))

