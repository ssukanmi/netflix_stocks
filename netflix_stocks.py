import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv('NFLX.csv')
netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
# print(netflix_stocks.head())
dowjones_stocks = pd.read_csv('DJI.csv')
dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
# print(dowjones_stocks.head())
netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)
# print(netflix_stocks_quarterly.head())

# print(netflix_stocks_quarterly.groupby('Quarter').Price.min())
# print(netflix_stocks_quarterly.groupby('Quarter').Price.max())

fig1 = plt.figure(figsize=(16, 10))
sns.violinplot(x='Quarter', y='Price', data=netflix_stocks_quarterly)
plt.title('Distribution of 2017 Netflix Stock Prices by Quarter')
plt.xlabel('Closing Stock Price')
plt.ylabel('Business Quarters in 2017')

fig2 = plt.figure(figsize=(16, 10))
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017", "2Q2017", "3Q2017", "4Q2017"]
earnings_actual = [.4, .15, .29, .41]
earnings_estimate = [.37, .15, .32, .41]
plt.scatter(x_positions, earnings_actual, color='r', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='b', alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')

fig3 = plt.figure(figsize=(16, 10))
revenue_by_quarter = [2.79, 2.98, 3.29, 3.7]
earnings_by_quarter = [.0656, .12959, .18552, .29012]
quarter_labels = ["2Q2017", "3Q2017", "4Q2017", "1Q2018"]
revenue_x = [i*2 + 0.8*1 for i in range(4)]
earning_x = [i*2 + 0.8*2 for i in range(4)]
x_tick = [(x1 + x2) / 2 for x1, x2 in zip(revenue_x, earning_x)]
plt.bar(revenue_x, revenue_by_quarter, label='revenue')
plt.bar(earning_x, earnings_by_quarter, label='earnings')
plt.legend()
plt.title('revnue and earnings by quarter')
plt.xticks(x_tick, quarter_labels)

fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
ax1.plot(netflix_stocks.Date, netflix_stocks.Price)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
ax1.set_title('Netflix')
ax1.set_xticklabels(netflix_stocks.Date, rotation=70)

ax2.plot(dowjones_stocks.Date, dowjones_stocks.Price)
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
ax2.set_title('Dow Jones')
ax2.set_xticklabels(dowjones_stocks.Date, rotation=70)

plt.subplots_adjust(wspace=0.5)

plt.show()
