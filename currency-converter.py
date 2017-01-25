#!/usr/bin/python3

import argparse
import json
import sys

from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates
from forex_python.converter import RatesNotAvailableError

def main(argv):
    parser = argparse.ArgumentParser(description='Currency converter.')
    # Options:
    # --amount
    # --input_currency
    # --output_currency
    # NOTE: --help option is implicit with 'argparse'.
    parser.add_argument("--amount", type=float, dest='amount', metavar='AMOUNT', required=True)
    parser.add_argument("--input_currency", type=str, dest='input_currency', metavar='INPUT_CURRENCY', required=True)
    parser.add_argument("--output_currency", type=str, dest='output_currency', metavar='OUTPUT_CURRENCY', default=None)

    opts = parser.parse_args(argv)

    # TODO: Conversion from currency symbol to currency code
    input_currency = opts.input_currency
    output_currency = opts.output_currency

    # Check if given currency codes are supported
    if CurrencyCodes().get_currency_name(input_currency) is None:
        print('{}: Unknown input currency.'.format(input_currency), file=sys.stderr)
        exit(1)

    if output_currency is not None and CurrencyCodes().get_currency_name(output_currency) is None:
        print('{}: Unknown output currency.'.format(output_currency), file=sys.stderr)
        exit(1)

    # Do the currency conversion
    if output_currency:
        val = CurrencyRates().get_rate(input_currency, output_currency)
        output_val = \
            { output_currency: val*opts.amount
            }
    else:
        output_val = CurrencyRates().get_rates(input_currency)
        for k in output_val.keys():
            output_val[k] *= opts.amount

    input_val = \
        { 'amount': opts.amount
        , 'currency': input_currency
        }

    json_result = \
        { 'input': input_val
        , 'output': output_val
        }

    print(json.dumps(json_result, indent=4, separators=(',', ': '), sort_keys=True))


if __name__ == "__main__":
    main(sys.argv[1:])
