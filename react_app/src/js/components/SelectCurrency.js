import React from 'react';

class SelectCurrency extends React.Component {

    onSelectCurrency(code) {
        const {currencies, rates, currencyA, currencyAval} = this.props;
        const currency = currencies.filter(currency => currency.code === code);
        console.log('selecting currency: ' + code);
        // const rate = rates.filter(rate => rate.source_currency === currencyA.code && rate.target_currency === currency.code);
        // console.log(currencyA, currency);
        this.props.onChanged(currency[0])//, currencyAval * rate);
    }

    render() {

        let {currencies, rates, currencyA, currencyB, currencyAval} = this.props;

        if (currencies) {
            return <select onChange={(e) => this.onSelectCurrency(e.target.value)}>
                {
                    currencies.map(currency => {
                        const {code, name} = currency;
                        return <option key={code} value={code}>{name}</option>
                    })
                }
            </select>
        } else {
            return null;
        }
    }
}


export default SelectCurrency;