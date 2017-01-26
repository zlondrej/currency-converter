# Python Currency Converter

Simple currency converter that converts currencies and prints out result
in cool `JSON` format.

## Requirements

* python 3
* forex-python

## Usage

```
./currency-converter.py
    [-h]
    --amount AMOUNT
    --input_currency INPUT_CURRENCY
    [--output_currency OUTPUT_CURRENCY]

-h, --help                            show this help message and exit
--amount AMOUNT                       amount to convert
--input_currency INPUT_CURRENCY       code or symbol of currency to convert from
--output_currency OUTPUT_CURRENCY     code or symbol of currency to convert to (optional)
```

### Supported currency symbol conversions

This table shows all supported currency symbols and corresponding currency.

| Currency symbol | Currency code | Currency name |
|-----|-----|------------------------|
| $   | USD | United States dollar   |
| Fr. | CHF | Swiss franc            |
| Ft  | HUF | Hungarian forint       |
| HK$ | HKD | Hong Kong dollar       |
| Kr  | DKK | Danish krone           |
| Kč  | CZK | Czech koruna           |
| L   | RON | Romanian leu           |
| NZ$ | NZD | New Zealand dollar     |
| R$  | BRL | Brazilian real         |
| R   | RUB | Russian ruble          |
| RM  | MYR | Malaysian ringgit      |
| Rp  | IDR | Indonesian rupiah      |
| S$  | SGD | Singapore dollar       |
| W   | KRW | South Korean won       |
| kn  | HRK | Croatian kuna          |
| kr  | NOK | Norwegian krone        |
| zł  | PLN | Polish zloty           |
| £   | GBP | British pound          |
| ¥   | JPY | Japanese yen           |
| ฿   | THB | Thai baht              |
| ₪   | ILS | Israeli new sheqel     |
| €   | EUR | European Euro          |
| ₱   | PHP | Philippine peso        |
| ₹   | INR | Indian rupee           |
