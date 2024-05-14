# ❖ StockETrade
AIO CLI stock trading applicaiton linked with Alpaca API and GPT to buy stocks.

## How to use?
Follow the steps below to get started.
  
1. Create an account on [Alpaca](https://alpaca.markets/) and [OpenAI](https://openai.com/)

2. Run the `authenticate.py` file in the terminal and follow the prompts. Make sure to enter each API key seperately.

3. Run the ui.py file in the terminal, and check to see if all commands are working.

4. Enable paper trading in Alpaca to test if commands work properly.

## Commands and Syntax
StockeETrade uses typer for all CLI commands. Reference the page [here](https://typer.tiangolo.com/) to learn more.

1. To run scripts in terminal type `python ui.py --help` this will display all commands currently available in StockETrade.
   - Some Commands have multiple parameters, please ensure you read the description before running a command.
2. Commands
   - Check: Check the current market price of a stock, ETF, or fund, etc. 
   - Trade: Purchase a stock, ETF, or fund with assets available in Alpaca account. 
   - AI: Query GPT and get output based off data provided
   - Account: Get total account balance

## Dependencies
List of dependencies needed for StockETrade to work:
1. [LangChain](https://www.langchain.com/)
2. [Typer](https://typer.tiangolo.com/)
3. [OpenAI](https://openai.com/index/openai-api/)
4. [Alpaca](https://alpaca.markets/)
5. **AND ALL NECESSARY DEPENDENCIES NEEDED TO INSTALL THE FOLLOWING**
