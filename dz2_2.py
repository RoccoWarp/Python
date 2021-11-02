weather_report = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# for i, x in enumerate(weather_report):
#     if x == '5':
#         weather_report[i] = '"05"'
#     if x == '+5':
#         weather_report[i] = '"+05"'
#     if x == '17':
#         weather_report[i] = '"17"'
# print(' '.join(weather_report))

new_weather_report = []
for i in weather_report:
    if i.isdigit() or i.startswith('+'):
        new_weather_report.extend(['"',i,'"'])
    else: new_weather_report.append(i)
print(new_weather_report)
print(' '.join(new_weather_report))

