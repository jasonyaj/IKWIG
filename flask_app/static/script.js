// on load to set first car on the list as default and render card
window.onload = function() {
  var selectElement = document.getElementById("cars");
  selectElement.selectedIndex = 0;
  get_value(selectElement.value);
  load_cars(this, Number(selectElement.value));
  console.log(typeof(selectElement.value));
};

// global car id of current select
var currentValue = "";

// on click of selection grabs and sets car id value
function get_value(value){
  currentValue = value;
}

// use to insert the car id value to the href of the update page
function update_href() {
  var updateLink = document.getElementById("updateLink");
  updateLink.href = `/garage/${currentValue}/edit`;
}

// triggers sold route to update boolean value (1= true/sold, 0=false/not sold)
function sold_action() {
  var markSold = document.getElementById("markSold");
  markSold.action = `/garage/${currentValue}/sold`;
}

// API route and method
async function load_cars(element, value) {
  // "route"
  let URL = "http://127.0.0.1:5000/api/cars"
  let settings = {
    method : "GET"
  }

  let response = await fetch(URL, settings);
  let data = await response.json();

  // "method" to grab a single car data by car id and render card
  let card = document.getElementById("carCard");
  let targetID = value;
  let currentCar = data.filter(obj => obj.id === targetID);

  if (currentCar.length > 0) {
    card.innerHTML = `
    <div class="row">
    <img
      src="../static/img/${currentCar[0].file_name}"
      alt="Photo of the selected car."
      onError="this.onerror=null;this.src='../static/img/OneHorsepower.jpg';"
    />
    </div>
    <h5>Year: <span class="ms-2">${currentCar[0].year}</span></h5>
    <h5>Make: <span class="ms-2">${currentCar[0].make}</span></h5>
    <h5>Model: <span class="ms-2">${currentCar[0].model}</span></h5>
    <h5>Trim: <span class="ms-2">${currentCar[0].trim}</span></h5>
    <h5>Color: <span class="ms-2">${currentCar[0].color}</span></h5>
    <h5>Description:</h5>
    <textarea class="mb-5" cols="30" rows="10">${currentCar[0].description}</textarea>
    `
  } else {
    card.innerHTML = "<h5>No car selected or found in the database.</h5>"
    console.log('Object with targetID not found');
  }
}