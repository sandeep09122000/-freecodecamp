import pandas as pd

# Assuming you load your data into a DataFrame called df
# For this example, replace the following line with your actual data loading method
# For example: df = pd.read_csv('path_to_data.csv')
# Here, for demonstration, we'll assume df is already loaded as a variable
# But in your actual code, you should load the dataset.
# e.g., df = pd.read_csv('demographic_data.csv')

# Placeholder for DataFrame; replace with actual data loading
df = None

def analyze_demographic_data(df):
    # Initialize variables as None
    race_counts = None
    average_age_men = None
    percent_bachelors = None
    percent_advanced_edu_high_earners = None
    percent_non_advanced_edu_high_earners = None
    min_hours = None
    percent_min_hours_high_salary = None
    highest_earning_country = None
    highest_earning_country_percentage = None
    top_occupation_in_india = None

    # Check if df is loaded
    if df is None:
        raise ValueError("DataFrame is not loaded. Please load your dataset into 'df'.")

    # 1. How many people of each race are represented in this dataset?
    race_counts = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percent_bachelors = round((bachelors_count / total_count) * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, Doctorate) make more than 50K?
    advanced_educations = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_mask = df['education'].isin(advanced_educations)
    advanced_edu_high_salary = df[advanced_edu_mask & (df['salary'] == '>50K')]
    percent_advanced_edu_high_earners = round(
        (len(advanced_edu_high_salary) / len(df[advanced_edu_mask]) * 100), 1
    ) if len(df[advanced_edu_mask]) > 0 else 0

    # 5. What percentage of people without advanced education make more than 50K?
    non_advanced_mask = ~df['education'].isin(advanced_educations)
    non_advanced_high_salary = df[non_advanced_mask & (df['salary'] == '>50K')]
    percent_non_advanced_high_earners = round(
        (len(non_advanced_high_salary) / len(df[non_advanced_mask]) * 100), 1
    ) if len(df[non_advanced_mask]) > 0 else 0

    # 6. What is the minimum number of hours a person works per week?
    min_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    high_salary_min_hours_workers = min_hours_workers[min_hours_workers['salary'] == '>50K']
    percent_min_hours_high_salary = round(
        (len(high_salary_min_hours_workers) / len(min_hours_workers) * 100), 1
    ) if len(min_hours_workers) > 0 else 0

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_counts = df['native-country'].value_counts()
    country_high_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_percentage = (country_high_salary_counts / country_counts) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_high_salary.empty:
        top_occupation_in_india = india_high_salary['occupation'].value_counts().idxmax()
    else:
        top_occupation_in_india = None

    # Return all variables as a dictionary
    return {
        'race': race_counts,
        'average age of men': average_age_men,
        'percentage with Bachelors': percent_bachelors,
        'percentage with advanced education earning >50K': percent_advanced_edu_high_earners,
        'percentage without advanced education earning >50K': percent_non_advanced_high_earners,
        'min hours per week': min_hours,
        'percentage of min hours workers earning >50K': percent_min_hours_high_salary,
        'highest earning country': highest_earning_country,
        'highest earning country percentage': highest_earning_country_percentage,
        'most popular occupation in India among >50K earners': top_occupation_in_india
    }

# Example usage:
if __name__ == "__main__":
    # Load your dataset here, for example:
    # df = pd.read_csv('demographic_data.csv')
    # Replace the following line with your data loading code
    # For now, just an example placeholder:
    # df = pd.read_csv('path_to_your_csv.csv')
    pass
