import App from '../App'

const baseUrl = "http://localhost:8000";

const login = () => fetch(baseUrl + '/api/v0/login/', {
    method: 'POST',
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'admin',
        password: 'admin'
    })
});

const getCurrencies = (token) => fetch(baseUrl + '/api/v0/currencies/list/', {
    method: 'GET',
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + token

    }
});

const getRates = (token) => fetch(baseUrl + '/api/v0/currencies/rates/', {
    method: 'GET',
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + token

    },
});

export {
    login,
    getCurrencies,
    getRates
}