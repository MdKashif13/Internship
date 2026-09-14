import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
df=pd.read_csv('C:\\Users\\mdkas\\OneDrive\\Desktop\\INTERNSHIP\\Project 1\\ecommerce_orders_final.csv')

#Commercial Contribution Bar Chart

cat_rev = (
    df.groupby('Category')['Net_Revenue']
    .sum()
    .reset_index()
    .sort_values(by='Net_Revenue', ascending=False)
)

plt.figure(figsize=(10, 6))
colors_d1 = sns.color_palette('tab10', len(cat_rev))
bars_d1 = plt.bar(cat_rev['Category'], cat_rev['Net_Revenue'], color=colors_d1)

plt.title(
    'D1: Commercial Contribution - Total Net Revenue by Category',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Product Category', fontsize=12, labelpad=10)
plt.ylabel('Net Revenue ($)', fontsize=12, labelpad=10)

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

for bar in bars_d1:
  yval = bar.get_height()
  plt.text(
      bar.get_x() + bar.get_width() / 2,
      yval + (yval * 0.01),
      f'${yval:,.2f}',
      ha='center',
      va='bottom',
      fontsize=10,
  )

plt.tight_layout()
plt.savefig('D1_commercial_contribution.png', dpi=300)
plt.show()


#Fulfillment Distribution & Benchmark Histogram

plt.figure(figsize=(10, 6))
avg_est_days = df['Est_Delivery_Days'].mean()

sns.histplot(
    df['Actual_Delivery_Days'],
    bins=range(
        df['Actual_Delivery_Days'].min(), df['Actual_Delivery_Days'].max() + 2
    ),
    discrete=True,
    kde=True,
    color='skyblue',
    edgecolor='black',
    alpha=0.7,
)


plt.axvline(
    avg_est_days,
    color='red',
    linestyle='--',
    linewidth=2.5,
    label=f'Avg Estimated Benchmark ({avg_est_days:.2f} Days)',
)

plt.title(
    'D2: Fulfillment Distribution & Benchmark Histogram',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Actual Delivery Days', fontsize=12, labelpad=10)
plt.ylabel('Order Count', fontsize=12, labelpad=10)
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('D2_fulfillment_distribution.png', dpi=300)
plt.show()

#Discount Elasticity vs. Return Propensity Scatter Plot

plt.figure(figsize=(10, 6))
palette_d3 = {'Yes': '#d9534f', 'No': '#5cb85c'}

sns.scatterplot(
    data=df,
    x='Discount_Percent',
    y='Order_Value',
    hue='Returned',
    palette=palette_d3,
    alpha=0.7,
    s=70,
    edgecolor='k',
)

plt.title(
    'D3: Discount Elasticity vs. Return Propensity',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Discount Percent (%)', fontsize=12, labelpad=10)
plt.ylabel('Order Value ($)', fontsize=12, labelpad=10)
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
plt.legend(title='Returned', fontsize=11, title_fontsize=11)

plt.tight_layout()
plt.savefig('D3_discount_vs_return.png', dpi=300)
plt.show()


#Logistics Impact on Sentiment Bar Chart
plt.figure(figsize=(10, 6))

rating_by_fulfillment = (
    df.groupby('Fulfillment_Status')['Customer_Rating']
    .mean()
    .reset_index()
    .sort_values(by='Customer_Rating', ascending=False)
)

bars_d4 = plt.bar(
    rating_by_fulfillment['Fulfillment_Status'],
    rating_by_fulfillment['Customer_Rating'],
    color=sns.color_palette('viridis', len(rating_by_fulfillment)),
)

plt.title(
    'D4: Logistics Impact on Sentiment - Average Rating by Fulfillment Status',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Fulfillment Status', fontsize=12, labelpad=10)
plt.ylabel('Average Customer Rating (1-5)', fontsize=12, labelpad=10)
plt.ylim(0, 5.5)

for bar in bars_d4:
  yval = bar.get_height()
  plt.text(
      bar.get_x() + bar.get_width() / 2,
      yval + 0.1,
      f'{yval:.2f} ★',
      ha='center',
      va='bottom',
      fontsize=11,
      fontweight='bold',
  )

plt.tight_layout()
plt.savefig('D4_logistics_impact_sentiment.png', dpi=300)
plt.show()

