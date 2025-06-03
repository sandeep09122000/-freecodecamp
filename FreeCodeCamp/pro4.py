
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def import_and_clean_data():
    # 1. Import data with date as index
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    
    # 2. Filter out top 2.5% and bottom 2.5%
    lower_bound = df['page_views'].quantile(0.025)
    upper_bound = df['page_views'].quantile(0.975)
    df_clean = df[(df['page_views'] >= lower_bound) & (df['page_views'] <= upper_bound)]
    
    return df_clean

def draw_line_plot(df):
    # Create a line plot of daily page views
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['page_views'], color='blue')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.tight_layout()
    # Save or return the figure
    return fig

def draw_bar_plot(df):
    # Prepare data: group by year and month, compute mean
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Group by year and month and calculate mean
    df_grouped = df_bar.groupby(['year', 'month'])['page_views'].mean().reset_index()
    
    # Pivot for plotting
    df_pivot = df_grouped.pivot(index='year', columns='month', values='page_views')
    # Reorder months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot[month_order]
    
    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.tight_layout()
    return fig

def draw_box_plot(df):
    df_box = df.copy()
    
    # Extract year and month
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    # To ensure months are in calendar order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    
    # Plot Year-wise box plot
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='page_views', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='page_views', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    return fig

# Main execution (for testing purposes)
if __name__ == '__main__':
    df_clean = import_and_clean_data()
    
    # Line plot
    fig1 = draw_line_plot(df_clean)
    plt.show()  # or fig1.savefig('line_plot.png')
    
    # Bar plot
    fig2 = draw_bar_plot(df_clean)
    plt.show()  # or fig2.savefig('bar_plot.png')
    
    # Box plots
    fig3 = draw_box_plot(df_clean)
    plt.show()  # or fig3.savefig('box_plots.png')



    from time_series_visualizer import import_and_clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

df = import_and_clean_data()

# Draw and save/display plots
fig_line = draw_line_plot(df)
fig_line.savefig('line_chart.png')

fig_bar = draw_bar_plot(df)
fig_bar.savefig('bar_chart.png')

fig_box = draw_box_plot(df)
fig_box.savefig('box_plots.png')