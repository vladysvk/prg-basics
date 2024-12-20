countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Ukraine","population":37000000},
    {"name":"USA", "population":335000000},
    {"name":"Canada","population":40000000},
    {"name":"Germany","population":85000000},
]

for country in countries:
    for key,value in country.items():
        print(f"{key} : {value}")