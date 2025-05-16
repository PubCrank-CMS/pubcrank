{
  title: Using WeatherKit with Python
  date: 2022-08-09 00:00:00 -0600
  categories:
  [
    python
    weatherkit
    weather api
  ]
}


Apple bought out the Dark Sky weather company in 2020. They plan on shutting down the Darky Sky API and replacing it with the new WeatherKit service. The WeatherKit service is now in beta and can be used to retrieve weather forecasts and current conditions.

The Dark Sky API was extremely easy to use and provided excellent weather data. The WeatherKit API functions much the same as the Dark Sky API, however, the authorization is very different and some what more difficult. You still need to an API token like the previous API. However, now generating the token is more complex. Below is a gist that lays out how to use the API in Python with explanations of some aspects of the usage following.

<script src="https://gist.github.com/pizzapanther/8a29b5462c786f0bb94a257ea535cc0f.js"></script>

## Items Needed to Generate a Token

**WEATHERKIT_SERVICE_ID:** [Create a service](https://developer.apple.com/account/resources/identifiers/list/serviceId) in your Apple developer account. It should look something like `com.example.weatherkit-client` and make sure it ends in `.weatherkit-client`.

**WEATHERKIT_TEAM_ID:** Go to your [developer account](https://developer.apple.com/account/) and get your Team ID.

**WEATHERKIT_KID and WEATHERKIT_KEY:** [Generate a new key](https://developer.apple.com/account/resources/authkeys/list) and get the Key ID and contents of the p8 file.

## Generate a JWT

Once you have the required items, you can use them to generate a JSON Web Token using the `ES256` algorithm. The expiration used to generate the token can be a large amount of time, however, a short expiration is better in case your token ever got compromised.

## Using Your Token

Once you have a token generated, use it in an authorization header to make requests. The token can be reused until the token expiration has passed.
