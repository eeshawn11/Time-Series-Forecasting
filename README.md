# Time-Series-Forecasting

## Time series forecasting with Prophet

Time series analysis using a [dataset](https://www.kaggle.com/datasets/eeshawn/half-hourly-electrical-demand-in-singapore) gathered from the [Energy Market Authority](https://www.ema.gov.sg/index.aspx) of Singapore. The original data is stored in individual weekly Excel files by month and year, which I have scraped from the website and combined into a dataset.

This is a relatively straightforward univariate time series problem involving electricity demand in Singapore, which I have attempted to forecast using Prophet, achieving a Mean Absolute Percentage Error (MAPE) of **3.67%**.

Skills Demonstrated:

- Web scraping with `Selenium`
- Data transformation with `pandas`
- Time series analysis with Facebook `Prophet`
