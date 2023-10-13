import pandas as pd

def random_undersampling(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Given a credit card dataset with 0 as the majority for 'Class' column, 
    returns a credit card dataset with two classes having the same shape, given raw data read from CSV.

    Parameters
    ----------
    df: pd.DataFrame
        The potentially imbalanced dataset.

    Returns
    -------
    Undersampled dataset with an equal number of fraudulent and legitimate data.
    '''
    
    # Separate the majority (non-fraudulent) and minority (fraudulent) classes
    legitimate_data = df[df['Class'] == 0]
    fraudulent_data = df[df['Class'] == 1]

    # Determine the number of samples to keep from the majority class
    num_samples_to_keep = len(fraudulent_data)

    # Randomly undersample the majority class to match the minority class
    legitimate_data_sampled = legitimate_data.sample(n=num_samples_to_keep, random_state=42)

    # Concatenate the undersampled majority class with the minority class
    undersampled_data = pd.concat([fraudulent_data, legitimate_data_sampled])

    # Shuffle the undersampled dataset
    undersampled_data = undersampled_data.sample(frac=1, random_state=42).reset_index(drop=True)

    return undersampled_data
