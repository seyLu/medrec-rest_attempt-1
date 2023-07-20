const regionsDatalist = document.getElementById("regions-datalist");
const provincesDatalist = document.getElementById("provinces-datalist");
const citiesDatalist = document.getElementById("cities-datalist");
const districtsDatalist = document.getElementById("districts-datalist");

DATALIST_MAP = {
    "regions": regionsDatalist,
    "provinces": provincesDatalist,
    "cities": citiesDatalist,
    "districts": districtsDatalist
}

async function getEndpoints(endpoints) {
    for (endpoint of endpoints) {
        const endpointRes = await fetch(`/api/${endpoint}`);
        const endpointJson = await endpointRes.json();

        for (item of endpointJson) {
            const option = document.createElement("option");
            option.id = item.code;
            option.innerHTML = item.name;
            DATALIST_MAP[endpoint].appendChild(option);
        }
    }
}




getEndpoints([
    "regions",
    "provinces",
    "cities",
    "districts",
]);
