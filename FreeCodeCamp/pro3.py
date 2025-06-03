
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Import data from 'medical_examination.csv' and assign it to df
df = pd.read_csv('medical_examination.csv')

# 2. Add an 'overweight' column
# Calculate BMI: weight / (height in meters)^2
# height is in cm, convert to meters by dividing by 100
# weight is in kg
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
# Overweight if BMI > 25
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize data for 'cholesterol' and 'gluc'
# 1: normal -> 0; 2 or 3: above normal -> 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the categorical plot
def draw_cat_plot():
    # Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # Group and reformat data to count the occurrences
    # Rename 'variable' column for clarity if needed
    # Count of each category per 'cardio' group
    df_cat = df_cat.value_counts().reset_index(name='total')

    # Draw the categorical plot
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    g.set_axis_labels('variable', 'total')
    g.set_titles('Cardio = {col_name}')
    plt.tight_layout()
    # Save or show as needed; for now, just return figure
    return g.fig

# 5. Draw the heat map
def draw_heat_map():
    # Clean the data:
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = pd.np.triu(pd.np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        cmap='coolwarm',
        linewidths=0.5,
        ax=ax
    )

    plt.tight_layout()
    return fig

# Note: If using seaborn or matplotlib, ensure plt.show() is called in your main script
# or save figures as needed.

# Example usage:
if __name__ == '__main__':
    # Generate and display the categorical plot
    cat_fig = draw_cat_plot()
    plt.show()

    # Generate and display the heatmap
    heat_fig = draw_heat_map()
    plt.show()

