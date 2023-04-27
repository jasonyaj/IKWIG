// carYear = document.getElementById(year);
// carYear.addEventListener("click", fun);
// document.getElementById().selected = true;
var currentValue = "";

function get_value(value){
  currentValue = value;
}

function update_href() {
  var updateLink = document.getElementById("updateLink");
  updateLink.href = `/garage/${currentValue}/edit`;
}

function sold_action() {
  var markSold = document.getElementById("markSold");
  markSold.action = `/garage/${currentValue}/sold`;
}

function display_selection(value) {
  // const toggleButton = document.querySelector('#selection');
  // const hiddenItems = document.querySelectorAll('.hidden_item');

  // let isHidden = true;

  // toggleButton.addEventListener('click', () => {
  //   hiddenItems.forEach(item => {
  //       if (isHidden) {
  //           item.style.display = 'block';
  //       } else {
  //           item.style.display = 'none';
  //       }
  //   });
  //   console.log(isHidden);
  //   isHidden = !isHidden;
  // });


  //save the Element you want to modify later as a variable
  // alert(value);
  // const carCardData = document.getElementById('#carCard');
  // //loop through each car in the list
  // for (const car in listOfCars) {
  //     //for each car in the list, check if the id of it matches the value passed in
  //     if (car.id === value) {
  //         //if it is the correct card, set the carCardData's HTML to the stuff we want to display
  //         carCardData.innerHTML = <h5>Year: <span class="ms-2">{{car.year}}</span></h5>
  //         <h5>Make: <span class="ms-2">{{car.make}}</span></h5>
  //         <h5>Model: <span class="ms-2">{{car.model}}</span></h5>
  //         <h5>Trim: <span class="ms-2">{{car.trim}}</span></h5>
  //         <h5>Color: <span class="ms-2">{{car.color}}</span></h5>
  //         <h5>Description:</h5>
  //         <textarea name="" id="" cols="30" rows="10">{{car.description}}</textarea>``
  //     }
  // }
}

async function load_cars(element, value) {
  let URL = "http://127.0.0.1:5000/api/cars"
  let settings = {
    method : "GET"
  }

  let response = await fetch(URL, settings);
  let data = await response.json();

  let card = document.getElementById("carCard");
  let targetID = value;
  let currentCar = data.filter(obj => obj.id === targetID);
  
  console.log(currentCar);
  console.log(value);

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
    card.innerHTML = "<h5>Sorry, that car was not found in our database.</h5>"
    console.log('Object with targetID not found');
  }
}