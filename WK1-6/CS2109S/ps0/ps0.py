import copy
import numpy as np
from matplotlib import pyplot as plt



from prepare_data import *

# Example on loading the data for Task 2
from prepare_data import * # loads the `get_...` helper funtions

df = get_data()
cases_cumulative = get_n_cases_cumulative(df)
deaths_cumulative = get_n_deaths_cumulative(df)
healthcare_spending = get_healthcare_spending(df)
mask_prices = get_mask_prices(healthcare_spending.shape[1])
stringency_values = get_stringency_values(df)
cases_top_cumulative = get_n_cases_top_cumulative(df)

# Task 2.1
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
                                 [5, 10, 15, 20, 25]])
    deaths_cumulative = np.array([[1, 2, 3, 4, 5],
                                  [0, 1, 2, 3, 4]])
    
    n = 3
    expected = np.array([0.2, 0.4])
    result = compute_death_rate_first_n_days(n, cases_cumulative, deaths_cumulative)
    
    assert np.allclose(result, expected)

test_compute_death_rate()

# Task 2.2
def compute_increase_in_cases(n, cases_cumulative):
    '''
    Computes the daily increase in confirmed cases for each country for the first n days, starting
    from the first day.
    Parameters
    ----------    
    n: int
        How many days of data to return in the final array. If the input data has fewer
        than n days of data then we just return whatever we have for each country up to n. 
    cases_cumulative: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the cumulative number of
        confirmed cases in that country, i.e. the ith row of `cases_cumulative`
        contains the data of the ith country, and the (i, j) entry of
        `cases_cumulative` is the cumulative number of confirmed cases on the
        (j + 1)th day in the ith country.
    
    Returns
    -------
    Daily increase in cases for each country as a 2D `ndarray` such that the (i, j)
    entry corresponds to the increase in confirmed cases in the ith country on
    the (j + 1)th day, where j is non-negative.
    Note
    ----
    The number of cases on the zeroth day is assumed to be 0, and we want to
    compute the daily increase in cases starting from the first day.
    '''
    
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError
    

# Test case for Task 2.2
def test_22():#  
    cases_cumulative = np.zeros((100, 20))
    cases_cumulative[:, :] = np.arange(1, 21)
    actual = compute_increase_in_cases(100, cases_cumulative)
    assert(np.all(actual == np.ones((100, 20))))

    sample_cumulative = np.array([[1,2,3,4,8,8,10,10,10,10],[1,1,3,5,8,10,15,20,25,30]])
    expected = np.array([[1, 1, 1, 1, 4.], [1, 0, 2, 2, 3]])
    assert(np.all(compute_increase_in_cases(5,sample_cumulative) == expected))

    expected2 = np.array([[1, 1, 1, 1, 4, 0, 2, 0, 0, 0],[1, 0, 2, 2, 3, 2, 5, 5, 5, 5]])
    assert(np.all(compute_increase_in_cases(10,sample_cumulative) == expected2))
    assert(np.all(compute_increase_in_cases(20,sample_cumulative) == expected2))

    sample_cumulative2 = np.array([[51764, 51848, 52007, 52147, 52330, 52330],\
                                [55755, 56254, 56572, 57146, 57727, 58316],\
                                [97857, 98249, 98631, 98988, 99311, 99610]])
    expected3 = np.array([\
                [51764, 84, 159, 140, 183, 0],\
                [55755, 499, 318, 574, 581, 589],\
                [97857, 392, 382, 357, 323, 299]])
    assert(np.all(compute_increase_in_cases(6,sample_cumulative2) == expected3))

#test_22()



# Task 2.3
def find_max_increase_in_cases(n_cases_increase):
    '''
    Finds the maximum daily increase in confirmed cases for each country.
    Parameters
    ----------
    n_cases_increase: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the daily increase in the number of confirmed cases on the
        (j + 1)th day in the ith country.
    
    Returns
    -------
    Maximum daily increase in cases for each country as a 1D `ndarray` such that the
    ith entry corresponds to the increase in confirmed cases in the ith country as
    represented in `n_cases_increase`.
    '''
    
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError


# Test case for Task 2.3
def test_23():
    n_cases_increase = np.ones((100, 20))
    actual = find_max_increase_in_cases(n_cases_increase)
    expected = np.ones(100)
    assert(np.all(actual == expected))

    sample_increase = np.array([[1,2,3,4,8,8,10,10,10,10],[1,1,3,5,8,10,15,20,25,30]])
    expected2 = np.array([10, 30]) # max of [1,2,3,4,8,8,10,10,10,10] => 10, max of [1,1,3,5,8,10,15,20,25,30] => 30
    assert(np.all(find_max_increase_in_cases(sample_increase) == expected2))

    sample_increase2 = np.array([\
                [51764, 84, 159, 140, 183, 0],\
                [55755, 499, 318, 574, 581, 589],\
                [97857, 392, 382, 357, 323, 299]])
    expected3 = np.array([51764, 55755, 97857])
    assert(np.all(find_max_increase_in_cases(sample_increase2) == expected3))

    n_cases_increase2 = compute_increase_in_cases(cases_top_cumulative.shape[1], cases_top_cumulative)
    expected4 = np.array([ 68699.,  97894., 258110.])
    assert(np.all(find_max_increase_in_cases(n_cases_increase2) == expected4))

#test_23()


# Task 2.4
def compute_n_masks_purchaseable(healthcare_spending, mask_prices):
    '''
    Computes the total number of masks that each country can purchase if she
    spends all her emergency healthcare spending on masks.
    Parameters
    ----------
    healthcare_spending: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the emergency healthcare
        spending made by that country, i.e. the ith row of `healthcare_spending`
        contains the data of the ith country, and the (i, j) entry of
        `healthcare_spending` is the amount which the ith country spent on healthcare
        on (j + 1)th day.
    mask_prices: np.ndarray
        1D `ndarray` such that the jth entry represents the cost of 100 masks on the
        (j + 1)th day.
    
    Returns
    -------
    Total number of masks which each country can purchase as a 1D `ndarray` such
    that the ith entry corresponds to the total number of masks purchaseable by the
    ith country as represented in `healthcare_spending`.
    Note
    ----
    The masks can only be bought in batches of 100s.
    '''
    
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError

# Test case for Task 2.4
def test_24():
    prices_constant = np.ones(5)
    healthcare_spending_constant = np.ones((7, 5))
    actual = compute_n_masks_purchaseable(healthcare_spending_constant, prices_constant)
    expected = np.ones(7) * 500
    assert(np.all(actual == expected))

    healthcare_spending = healthcare_spending[:3, :]  #Using data from CSV
    expected2 = [3068779300, 378333500, 6208321700]
    assert(np.all(compute_n_masks_purchaseable(healthcare_spending, mask_prices)==expected2))

    healthcare_spending2 = np.array([[0, 100, 0], [100, 0, 200]])
    mask_prices2 = np.array([4, 3, 20])
    expected3 = np.array([3300, 3500])
    assert(np.all(compute_n_masks_purchaseable(healthcare_spending2, mask_prices2)==expected3))

#test_24()

# Task 2.5
def compute_stringency_index(stringency_values):
    '''
    Computes the daily stringency index for each country.
    Parameters
    ----------
    stringency_values: np.ndarray
        3D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the stringency values as a
        vector. To be specific, on each day, there are four different stringency
        values for 'school closing', 'workplace closing', 'stay at home requirements'
        and 'international travel controls', respectively. For instance, the (i, j, 0)
        entry represents the `school closing` stringency value for the ith country
        on the (j + 1)th day.
    
    Returns
    -------
    Daily stringency index for each country as a 2D `ndarray` such that the (i, j)
    entry corresponds to the stringency index in the ith country on the (j + 1)th
    day.
    In this case, we shall assume that 'stay at home requirements' is the most
    restrictive regulation among the other regulations, 'international travel
    controls' is more restrictive than 'school closing' and 'workplace closing',
    and 'school closing' and 'workplace closing' are equally restrictive. Thus,
    to compute the stringency index, we shall weigh each stringency value by 1,
    1, 3 and 2 for 'school closing', 'workplace closing', 'stay at home
    requirements' and 'international travel controls', respectively. Then, the 
    index for the ith country on the (j + 1)th day is given by
    `stringency_values[i, j, 0] + stringency_values[i, j, 1] +
    3 * stringency_values[i, j, 2] + 2 * stringency_values[i, j, 3]`.
    Note
    ----
    Use matrix operations and broadcasting to complete this question. Please do
    not use iterative approaches like for-loops.
    '''
    
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError

# Test case for Task 2.5
def test_25():
    stringency_values = np.ones((10, 20, 4))
    stringency_values[:, 10:, :] *= 2
    actual = compute_stringency_index(stringency_values)
    expected = np.ones((10, 20)) * (1 + 1 + 3 + 2)
    expected[:, 10:] *= 2
    assert(np.all(actual == expected))

    stringency_values2 = np.array([[[0, 0, 0, 0], [1, 0, 0, 0]], [[0, 0, 0, 0], [0, 1, 2, 0]]])
    actual2 = compute_stringency_index(stringency_values2)
    expected2 = np.array([[0, 1], [0, 7]])
    assert(np.all(actual2 == expected2))



#test_25()


# Task 2.6
def average_increase_in_cases(n_cases_increase, n_adj_entries_avg=7):
    '''
    Averages the increase in cases for each day using data from the previous
    `n_adj_entries_avg` number of days and the next `n_adj_entries_avg` number
    of days.
    Parameters
    ----------
    n_cases_increase: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the daily increase in the number of confirmed cases on the
        (j + 1)th day in the ith country.
    n_adj_entries_avg: int
        Number of days from which data will be used to compute the average increase
        in cases. This should be a positive integer.
    
    Returns
    -------
    Mean increase in cases for each day, using data from the previous
    `n_adj_entries_avg` number of days and the next `n_adj_entries_avg` number
    of days, as a 2D `ndarray` such that the (i, j) entry represents the
    average increase in daily cases on the (j + 1)th day in the ith country,
    rounded down to the smallest integer.
    
    The average increase in cases for a particular country on the (j + 1)th day
    is given by the mean of the daily increase in cases over the interval
    [-`n_adj_entries_avg` + j, `n_adj_entries_avg` + j]. (Note: this interval
    includes the endpoints).
    Note
    ----
    Since this computation requires data from the previous `n_adj_entries_avg`
    number of days and the next `n_adj_entries_avg` number of days, it is not
    possible to compute the average for the first and last `n_adj_entries_avg`
    number of days. Therefore, set the average increase in cases for these days
    to `np.nan` for all countries.
    '''
    
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError

# Test case for Task 2.6
def test_26():
    n_cases_increase = np.array([[0, 5, 10, 15, 20, 25, 30]])
    actual = average_increase_in_cases(n_cases_increase, n_adj_entries_avg=2)
    expected = np.array([[np.nan, np.nan, 10, 15, 20, np.nan, np.nan]])
    assert(np.array_equal(actual, expected, equal_nan=True))

#test_26()

# Task 2.7
def is_peak(n_cases_increase_avg, n_adj_entries_peak=7):
    '''
    Determines whether the (j + 1)th day was a day when the increase in cases
    peaked in the ith country.
    Parameters
    ----------
    n_cases_increase_avg: np.ndarray
        2D `ndarray` with each row representing the data of a country, and the columns
        of each row representing the time series data of the average daily increase in the
        number of confirmed cases in that country, i.e. the ith row of 
        `n_cases_increase` contains the data of the ith country, and the (i, j) entry of
        `n_cases_increase` is the average daily increase in the number of confirmed
        cases on the (j + 1)th day in the ith country. In this case, the 'average'
        is computed using the output from `average_increase_in_cases`.
    n_adj_entries_peak: int
        Number of days that determines the size of the window in which peaks are
        to be detected. 
    
    Returns
    -------
    2D `ndarray` with the (i, j) entry indicating whether there is a peak in the
    daily increase in cases on the (j + 1)th day in the ith country.
    Suppose `a` is the average daily increase in cases, with the (i, j) entry
    indicating the average increase in cases on the (j + 1)th day in the ith
    country. Moreover, let `n_adj_entries_peak` be denoted by `m`.
    In addition, an increase on the (j + 1)th day is deemed significant in the
    ith country if `a[i, j]` is greater than 10 percent of the mean of all
    average daily increases in the country.
    Now, to determine whether there is a peak on the (j + 1)th day in the ith
    country, check whether `a[i, j]` is maximum in {`a[i, j - m]`, `a[i, j - m + 1]`,
    ..., `a[i, j + m - 1]`, `a[i, j + m]`}. If it is and `a[i, j]` is significant,
    then there is a peak on the (j + 1)th day in the ith country; otherwise,
    there is no peak.
    Note
    ----
    Let d = `n_adj_entries_avg` + `n_adj_entries_peak`, where `n_adj_entries_avg`
    is that used to compute `n_cases_increase_avg`. Observe that it is not
    possible to detect a peak in the first and last d days, i.e. these days should
    not be peaks.
    
    As described in `average_increase_in_cases`, to compute the average daily
    increase, we need data from the previous and the next `n_adj_entries_avg`
    number of days. Hence, we won't have an average for these days, precluding
    the computation of peaks during the first and last `n_adj_entries_avg` days.
    Moreover, similar to `average_increase_in_cases`, we need the data over the
    interval [-`n_adj_entries_peak` + j, `n_adj_entries_peak` + j] to determine
    whether the (j + 1)th day is a peak.
    Hint: to determine `n_adj_entries_avg` from `n_cases_increase_avg`,
    `np.count_nonzero` and `np.isnan` may be helpful.
    '''

    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError


def test_27():
    n_cases_increase_avg = np.array([[np.nan, np.nan, 10, 10, 5, 20, 7, np.nan, np.nan], [np.nan, np.nan, 15, 5, 16, 17, 17, np.nan, np.nan]])
    n_adj_entries_peak = 1

    actual = is_peak(n_cases_increase_avg, n_adj_entries_peak=n_adj_entries_peak)
    expected = np.array([[False, False, False, False, False, True, False, False, False],
                        [False, False, False, False, False, True, False, False, False]])
    assert np.all(actual == expected)

    n_cases_increase_avg2 = np.array([[np.nan, np.nan, 10, 20, 20, 20, 20, np.nan, np.nan], [np.nan, np.nan, 20, 20, 20, 20, 10, np.nan, np.nan]])
    n_adj_entries_peak2 = 1

    actual2 = is_peak(n_cases_increase_avg2, n_adj_entries_peak=n_adj_entries_peak2)
    expected2 = np.array([[False, False, False, True, False, False, False, False, False],
                        [False, False, False, False, False, False, False, False, False]])
    assert np.all(actual2 == expected2)

#test_27()

def visualise_increase(n_cases_increase, n_cases_increase_avg=None):
    '''
    Visualises the increase in cases for each country that is represented in
    `n_cases_increase`. If `n_cases_increase_avg` is passed into the
    function as well, visualisation will also be done for the average increase in
    cases for each country.

    NOTE: If more than 5 countries are represented, only the plots for the first 5
    countries will be shown.
    '''
    days = np.arange(1, n_cases_increase.shape[1] + 1)
    plt.figure()
    for i in range(min(5, n_cases_increase.shape[0])):
        plt.plot(days, n_cases_increase[i, :], label='country {}'.format(i))
    plt.legend()
    plt.title('Increase in Cases')

    if n_cases_increase_avg is None:
        plt.show()
        return
    
    plt.figure()
    for i in range(min(5, n_cases_increase_avg.shape[0])):
        plt.plot(days, n_cases_increase_avg[i, :], label='country {}'.format(i))
    plt.legend()
    plt.title('Average Increase in Cases')
    plt.show()


def visualise_peaks(n_cases_increase_avg, peaks):
    '''
    Visualises peaks for each of the country that is represented in
    `n_cases_increase_avg` according to variable `peaks`.
    
    NOTE: If there are more than 5 countries, only the plots for the first 5
    countries will be shown.
    '''
    days = np.arange(1, n_cases_increase_avg.shape[1] + 1)

    plt.figure()
    
    for i in range(min(5, n_cases_increase_avg.shape[0])):
        plt.plot(days, n_cases_increase_avg[i, :], label='country {}'.format(i))
        peak = (np.nonzero(peaks[i, :]))[0]
        peak_days = peak + 1 # since data starts from day 1, not 0
        plt.scatter(peak_days, n_cases_increase_avg[i, peak])
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    df = get_data()
    n_cases_cumulative = get_n_cases_cumulative(df)
    n_deaths_cumulative = get_n_deaths_cumulative(df)
    healthcare_spending = get_healthcare_spending(df)
    mask_prices = get_mask_prices(healthcare_spending.shape[1])
    stringency_values = get_stringency_values(df)
    n_cases_top_cumulative = get_n_cases_top_cumulative(df)

