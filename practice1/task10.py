print('номер рейса:')
flight_number = input()
print('название авиакомпании (на русском языке):')
airline_name_RUS = input()
print('название авиакомпании (на английском языке):')
airline_name_ENG = input()
print('город прилета (на русском языке):')
arrival_city_RUS = input()
print('город прилета (на английском языке):')
arrival_city_ENG = input()
print('Заканчивается посадка на рейс', flight_number, airline_name_RUS, 'до', arrival_city_RUS)
print('This is the final boarding call for', airline_name_ENG, 'flight', flight_number, 'to', arrival_city_ENG)