from selenium import webdriver
import time

def get_currency_values():
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get('http://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=EUR')
        time.sleep(5)
        value = browser.find_element_by_xpath("//*[@id='converterResult']/div/div/div[2]/span[1]")
        one_dollar = value.text
        print('The dollar at this time has a value of: €{} EUROS'.format(one_dollar))
        browser.get('http://www.xe.com/en/currencyconverter/convert/?Amount=1&From=EUR&To=USD')
        time.sleep(5)
        value = browser.find_element_by_xpath("//*[@id='converterResult']/div/div/div[2]/span[1]")
        one_euro = value.text
        print('The euro at this time has a value of: ${} dollars'.format(one_euro))
        one_dollar_float = float(one_dollar)
        one_euro_float = float(one_euro)
        operate(one_dollar_float, one_euro_float)


def operate(one_dollar_float, one_euro_float):

        while True:
                command = str(input('''Selet currency conversion:
				[1]Dollars to euros
				[2]Euros to dollars
				[e]exit'''))

                if command == '1':
                        dollar_to_euro(one_dollar_float)
                elif command == '2':
                        euro_to_dollar(one_euro_float)
                else:
                        break

def dollar_to_euro(one_dollar_float):
        dollar_amount = float(input('Dollars amount: '))
        result = one_dollar_float * dollar_amount
        print('${} Dollars are ${} Euros'.format(dollar_amount, result))

def euro_to_dollar(one_euro_float):
        euros_amount = float(input('Euros amount: '))
        result = one_euro_float * euros_amount
        print('€{} Euros are ${} Dollars'.format(euros_amount, result))


if __name__ == '__main__':
        get_currency_values()