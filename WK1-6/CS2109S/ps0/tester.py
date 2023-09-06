import numpy as np

def compute_death_rate_first_n_days(n, cases_cumulative, deaths_cumulative):
    number_countries = len(cases_cumulative)
    death_rates = []
    
    for i in range(number_countries):
        casesthatday = cases_cumulative[i][n-1]
        deathsthatday = deaths_cumulative[i][n-1]
 
        if casesthatday == 0:
            death_rate = 0
        else:
            death_rate = deathsthatday / casesthatday
        death_rates.append(death_rate)
    return death_rates

# Sample test case
def test_compute_death_rate():
    cases_cumulative = np.array([[10, 20, 30, 40, 50],
                                 [5, 10, 20, 20, 25]])
    deaths_cumulative = np.array([[1, 2, 3, 4, 5],
                                  [0, 1, 2, 2, 4]])
    
    n = 3
    expected = np.array([0.1, 0.1])
    result = compute_death_rate_first_n_days(n, cases_cumulative, deaths_cumulative)
    
    assert np.allclose(result, expected)

test_compute_death_rate()
