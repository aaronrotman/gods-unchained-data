// API version
var version = "v0";

// Base url for the API calls
var url = `https://api.godsunchained.com/${version}`;
console.log(url);

// @ DEV 
// Uncomment only ONE of the below urls at a time

// Query url that returns the data for Proto 300: "Guerilla Sabotage"
// var queryUrl = `${url}/proto/300`;

// Query url that returns the user data for the given ethereum address

var publicAddress = ethereumAddress;
var queryUrl = `${url}/user/${publicAddress}/inventory?page=1&perPage=31`;

// Query url that returns protos with 1 mana
// var queryUrl = `${url}/proto?mana=1&perPage=100`;

// Query url that returns the data for Proto 100128: "Amazon Recruit"
// var queryUrl = `${url}/proto/100128`;

// Make the API call using the url variable as the url to query
d3.json(queryUrl).then(function(data) {
    console.log(queryUrl);
    console.log(data);
});
