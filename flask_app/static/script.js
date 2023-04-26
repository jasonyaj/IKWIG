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
  const toggleButton = document.querySelector('#selection');
  const hiddenItems = document.querySelectorAll('.hidden_item');

  let isHidden = true;

  toggleButton.addEventListener('click', () => {
    hiddenItems.forEach(item => {
        if (isHidden) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
    console.log(isHidden);
    isHidden = !isHidden;
  });


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