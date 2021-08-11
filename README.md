<h1 align="center"><ProjectName></h1>

<p align="center"><ProjectDescription></p>

## Description

In this project, I've provided some examples of what I learned about the backtrader python package by following along with [Part Time Larry's](https://www.youtube.com/watch?v=UNkH1TQl7qo "Algorithmic Trading with Python and Backtrader") "Algorithmic Trading with Python and Backtrader" videos on youtube. The current project has two datasets (Oracle stock and S&P 500) and two trading strategies (Golden Cross and Buy & Hold for 5 days). 

## Links

- [Backtrader Quick Start](https://www.backtrader.com/docu/quickstart/quickstart/ "BT Quick Start")

- [ORCL Dataset](https://github.com/mementum/backtrader/blob/master/datas/orcl-1995-2014.txt "ORCL Dataset")

- [Golden Cross/Death Cross](https://www.daytradetheworld.com/trading-blog/golden-cross/ "Golden Cross Strat")

- [Repo](https://github.com/roderpad/BacktraderPlayground "BacktraderPlayground Repo")

- [Bugs](https://github.com/roderpad/BacktraderPlayground/issues "Issues Page")

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