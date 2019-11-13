import React from "react";

const CurrencyInfo = ({value,currency,onChanged}) => {
    if (currency) {
        return <div className="col-sm-6 currency-from-input">

            <h3 className={`currency-flag ${currency.code}`}>{currency.name}</h3>

            <div className="input-group">
                <input type="number" value={value} className="form-control"
                       onChange={(e)=>{
                           onChanged(e.target.value)
                       }}
                       aria-describedby="basic-addon2" step="1" pattern="\d\.\d{2}"/>
                <span className="input-group-addon" id="basic-addon2">{currency.code}</span>
            </div>

        </div>
    } else {
        return null;
    }
}

export default CurrencyInfo;
