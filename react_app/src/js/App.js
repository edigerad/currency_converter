import React from 'react';
import image from '../resources/images/cash-calculator.svg'
import SelectCurrency from './components/SelectCurrency'
import CurrencyInfo from './components/CurrencyInfo'

import {login, getCurrencies, getRates} from './api/index'

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            currencies: [],
            rates: [],
            currencyA: {},
            currencyB: {},
            currencyAval: 0,
            currencyBval: 0
        };
        login().then(response => response.json()).then((response) => {
            localStorage.token = response.token;
        }).then(() => {
            getCurrencies(localStorage.token).then(response => response.json()).then((response) => {
                this.setState({
                    currencies: response,
                    currencyA: response[0],
                    currencyB: response[0],
                });
            });
        }).then(() => {
            getRates(localStorage.token).then(response => response.json()).then((response) => {
                this.setState({
                    rates: response
                });
            });
        });


    }

    render() {
        const {currencies, rates, currencyA, currencyB, currencyAval, currencyBval} = this.state;
        if (currencies) {
            return (
                <div>
                    <header>
                        <img src={image}/>
                        <h1>Currency Converter</h1>
                    </header>
                    <div className="content">
                        <div className="row row-select-currency">
                            <div className="col-md-6">
                                <h2>Source Currency</h2>
                                <p>
                                    <SelectCurrency onChanged={(value) => {
                                        const {rates, currencyB, currencyAval} = this.state;
                                        console.log(currencyAval);
                                        if (value.code === currencyB.code) {
                                            this.setState({currencyA: value, currencyBval: currencyAval});
                                        } else {
                                            const rate = rates.filter(rate => rate.source_currency === value.code && rate.target_currency === currencyB.code);

                                            this.setState({
                                                currencyA: value,
                                                currencyBval: currencyAval * rate[0].rate
                                            });
                                        }
                                    }} currencies={currencies} rates={rates}/>
                                </p>
                            </div>
                            <div className="col-md-6">
                                <h2>Target Currency</h2>
                                <p>
                                    <SelectCurrency onChanged={(value) => {
                                        const {rates, currencyB, currencyAval} = this.state;
                                        if (value.code === currencyA.code) {
                                            this.setState({currencyB: value, currencyBval: currencyAval});
                                        } else {
                                            const rate = rates.filter(rate => rate.source_currency === currencyA.code && rate.target_currency === value.code);
                                            this.setState({
                                                currencyB: value,
                                                currencyBval: currencyAval * rate[0].rate
                                            });
                                        }
                                    }} currencies={currencies} rates={rates} currencyAval={currencyAval}
                                                    currencyA={currencyA}
                                                    currencyB={currencyB}/>

                                </p>
                            </div>
                        </div>

                        <div className="row">
                            {currencyA && <CurrencyInfo
                                onChanged={(valueE) => {
                                    const {rates, currencyA, currencyB} = this.state;
                                    if (currencyA.code === currencyB.code) {
                                        this.setState({currencyAval: valueE, currencyBval: valueE});
                                    } else {
                                        const rate = rates.filter(rate => rate.source_currency === currencyA.code && rate.target_currency === currencyB.code);
                                        this.setState({currencyAval: valueE, currencyBval: valueE * rate[0].rate});
                                    }
                                }}
                                currency={currencyA}/>}
                            {currencyB && <CurrencyInfo
                                value={currencyBval}
                                currency={currencyB}
                            />}
                        </div>
                    </div>
                </div>
            )
        } else {
            return null;
        }

    }
}

export default App;