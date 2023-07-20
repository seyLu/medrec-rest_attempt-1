const regionsDatalist = document.getElementById("regions-datalist");
const provincesDatalist = document.getElementById("provinces-datalist");
const citiesDatalist = document.getElementById("cities-datalist");
const districtsDatalist = document.getElementById("districts-datalist");

DATALIST_MAP = {
    "provinces": provincesDatalist,
    "cities": citiesDatalist,
    "districts": districtsDatalist
}


async function getEndpoints(endpoints) {
    for (endpoint of endpoints) {
        const res = await fetch(`/api/${endpoint}`);
        const items = await res.json();

        DATALIST_MAP[endpoint].innerHTML = "";

        for (item of items) {
            const option = document.createElement("option");
            option.value = item.name;
            option.innerHTML = item.code;
            option.dataset.code = item.code;

            if (item.region_code) option.dataset.region_code = item.region_code;
            if (item.province_code) option.dataset.province_code = item.province_code;
            if (item.city_code) option.dataset.city_code = item.city_code;
            if (item.district_code) option.dataset.district_code = item.district_code;

            DATALIST_MAP[endpoint].appendChild(option);
        }
    }
}


getEndpoints([
    "provinces",
    "cities",
    "districts",
]);


async function getEndpointName(endpoint, code) {
    const res = await fetch(`/api/${endpoint}/${code}`);
    const item = await res.json();

    return item.name;
}


async function getEndpoint(parent_endpoint, code, endpoint) {
    const res = await fetch(`/api/${parent_endpoint}/${code}/${endpoint}`);
    const items = await res.json();

    DATALIST_MAP[endpoint].innerHTML = "";

    for (item of items) {
        const option = document.createElement("option");
        option.value = item.name;
        option.innerHTML = item.code;
        option.dataset.code = item.code;

        if (item.region_code) option.dataset.region_code = item.region_code;
        if (item.province_code) option.dataset.province_code = item.province_code;
        if (item.city_code) option.dataset.city_code = item.city_code;
        if (item.district_code) option.dataset.district_code = item.district_code;

        DATALIST_MAP[endpoint].appendChild(option);
    }
}


const regionsInput = document.getElementById("regions-input");
const provincesInput = document.getElementById("provinces-input");
const citiesInput = document.getElementById("cities-input");
const districtsInput = document.getElementById("districts-input");


provincesInput.addEventListener("input", async e => {
    if (!(e instanceof InputEvent) || e.inputType === 'insertReplacementText') {
        const input_val = provincesInput.value;
        const option_val = provincesDatalist.querySelector(`option[value="${input_val}"]`);

        citiesInput.value = "";
        districtsInput.value = "";

        getEndpoint("provinces", option_val.dataset.code, "cities")
        getEndpoint("provinces", option_val.dataset.code, "districts")
    }
});


citiesInput.addEventListener("input", async e => {
    if (!(e instanceof InputEvent) || e.inputType === 'insertReplacementText') {
        const input_val = citiesInput.value;
        const option_val = citiesDatalist.querySelector(`option[value="${input_val}"]`);

        districtsInput.value = "";

        provincesInput.value = await getEndpointName("provinces", option_val.dataset.province_code);
        getEndpoint("cities", option_val.dataset.code, "districts")
    }
});


districtsInput.addEventListener("input", async e => {
    if (!(e instanceof InputEvent) || e.inputType === 'insertReplacementText') {
        const input_val = districtsInput.value;
        const option_val = districtsDatalist.querySelector(`option[value="${input_val}"]`);

        provincesInput.value = await getEndpointName("provinces", option_val.dataset.province_code);
        citiesInput.value = await getEndpointName("cities", option_val.dataset.city_code);
    }
});
