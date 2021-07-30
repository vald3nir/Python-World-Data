# Python-World-Data

API to show world data like address and information about money

## Features:

- links the images of country flags from the abbreviation of their respective currencies.
- get a location's address from geographic coordinates

## APIs used:

### Currency Layer API https://currencylayer.com/

List the money abbreviation

### Rest Countries API https://restcountries.eu/

List the country information


## Examples:

### Geolocation

      curl --location --request GET 'https://python-world-data.herokuapp.com/address?latitude=-3.722158&longitude=-38.563948'
      
### List money code of countries 

      curl --location --request GET 'https://python-world-data.herokuapp.com/country_money'
      
### Creates a URL of a country's flag image

      curl --location --request GET 'https://python-world-data.herokuapp.com/country_flag/BND'
