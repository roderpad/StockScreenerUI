<h1 align="center"><ProjectName></h1>

<p align="center"><ProjectDescription></p>

## Description

In this project, I've created a stock screener web application using FastAPI (a new Python framework built on Starlette) by following along with [Part Time Larry's](https://www.youtube.com/watch?v=5GorMC2lPpk "FastAPI Python Tutorial - Building a Stock Screener with FastAPI") "FastAPI Python Tutorial - Building a Stock Screener with FastAPI" videos on youtube. The project utilizes many of the FastAPI features including pydantic models, dependency injection, background/async tasks, and SQLAlchemy integration. API endpoint testing was done using Insomnia API client. 

### `UI Design`
The frontend UI design is done using SemanticUI and Jinja2 templates, including CSS and JavaScript from the CDN.

### `Database Design`
The database design is done using SQLAlchemy models. The database has one table 'stocks.db' that holds stock data retrieved programmatically as a background task to prevent UI hang from yahoo finance (yfinance package). 

## Links
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/ "FastAPI Tutorial")

- [SemanticUI CDN](https://semantic-ui.com/introduction/advanced-usage.html#cdn-releases "SemanticUI CDN")

- [Insomnia API client](https://insomnia.rest/ "Insomnia API client")

- [Repo](https://github.com/roderpad/StockScreenerUI "StockScreenerUI Repo")

- [Bugs](https://github.com/roderpad/StockScreenerUI/issues "Issues Page")

## Screenshots

![Example Input](/screenshots/ProgramRun.png "Example Input")
![Example Output](/screenshots/Output.png "Example Output")

## How To Use

An example of how to run this is: `python trader.py golden_cross SPY 5000 20`. This runs the backtest using the golden_cross strategy using S&P500 data starting with $5k and order sizes of 20 stocks.

The five arguments:

### `strategy`,

The type of strategy you want to backtest. Currently only `golden_cross` and `buy_hold5days` are accepted.

### `ticker`,

The stock ticker used to test your strategy on. Currently only `ORCL` and `SPY` are accepted.

### `starting_cash`,

The amount of cash you want to start your backtest with.

### `order_size`,

The number of stocks you wish to execute an order with.

## Built With

- Python
- Matplotlib
- Backtrader

## Future Updates

- Get ticker and historical price data programmatically
- Allow for input of date range arguments
- Create more sophisticated buy options for placed orders

--->
## Author

**Paden Roder**

- [GitHub Profile](https://github.com/roderpad "Paden Roder")
- [Email: roderpad@gmail.com](mailto:roderpad@gmail.com)
- [Personal Website](https://padenroder.com/ "Website")
- [Twitter](https://twitter.com/PadenRoder "Twitter")
- [LinkedIn](https://www.linkedin.com/in/padenroder/ "LinkedIn")
- [Twitch](https://www.twitch.tv/roderbro "Twitch")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!