month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Fall',
    10: 'Fall', 11: 'Fall', 12: 'Winter'
}
def get_season(month):
    return month_to_season.get(month, 'Invalid month number')
month_number = 7  
season = get_season(month_number)
print(f"Month {month_number} is in the {season} season.")
