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

<!--## Screenshots

![Example Input](/screenshots/ProgramRun.png "Example Input")
![Example Output](/screenshots/Output.png "Example Output")
-->

## How To Use

### `1) Install Packages`,

Install required packages using `pip install -r requirements.txt`.

![Install Package Dependencies](/screenshots/PIPinstall.png "Install Packages")

### `2) Run App`,

Run the app by executing `./run` in the terminal.

![Run App](/screenshots/RunApp.png "Run App")

### `3) Open App`,

Open the app by going to `http://localhost:8000/` in your browser.

![Open App](/screenshots/OpenApp.png "Open App")

### `4) Add Stock Tickers`,

Click the `Add Stocks` button and then type in a list of stock ticker symbols. The app will then fetch up-to-date data on each ticker and insert into a local database `stocks.db`.

![Add Tickers](/screenshots/AddStocks.png "Add Tickers")
![View Table](/screenshots/ViewStocks.png "View Stocks")

### `5) Screen Stocks`,

Screen stocks from those in the database by using the filters for `price`, `forward price-to-earnings ratio`, `forward earnings-per-share ratio`, `dividend yield`,`50 day moving average`, and `200 day moving average`.

![Screen Stocks](/screenshots/FilteredStocks.png "Screen Stocks")

## Built With

- Python
- FastAPI
- SemanticUI
- Jinja2
- SQLAlchemy
- Pydantic

<!--
## Future Updates

- Get ticker and historical price data programmatically
- Allow for input of date range arguments
- Create more sophisticated buy options for placed orders
-->
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