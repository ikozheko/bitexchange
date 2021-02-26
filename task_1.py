people_salary = {'John': 800, 'Bob': 700, 'Ann': 1000, 'Mathew': 1200, 'Andrew': 1500}
average_salary = sum([i for i in people_salary.values()]) / len(list(people_salary))
lower_average_salary = [i for i in people_salary if people_salary[i] < average_salary]
print(lower_average_salary)


