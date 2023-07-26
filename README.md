<h1 align="center">IKWIG</h1>

<p align="center"><i>A Virtual Garage For the Collector</i></p>

---

## Table of Contents

- [Features](https://github.com/jasonyaj/IKWIG#features)
- [Background](https://github.com/jasonyaj/IKWIG#background)
- [Technologies Used](https://github.com/jasonyaj/IKWIG#technologies-used)
- [Functionality](https://github.com/jasonyaj/IKWIG#functionality)

## Background

Having a big interest in cars I have found that there is no app to keep track of my vehicle collection. There was a need to record previous cars owned as well as current cars in possession. I designed this web app to keep detailed information and be able to display the data to the user.

## Features

- Login/Registration with validations
  <img width="640" alt="login_register" src="https://github.com/jasonyaj/IKWIG/assets/124213154/309dac8e-106f-43f3-9e4f-d00cc31a58d1">

- My Garage
  <img width="640" alt="my_garage" src="https://github.com/jasonyaj/IKWIG/assets/124213154/145bd7f8-0ca2-4293-a470-101dce267412">

- Add
  <img width="640" alt="add" src="https://github.com/jasonyaj/IKWIG/assets/124213154/6c561f5b-884c-4fde-b9cb-483bfca14ac0">

- Update
  <img width="640" alt="update" src="https://github.com/jasonyaj/IKWIG/assets/124213154/ed3f1c63-095e-4640-b55f-5a03024fae4b">

- Mark as Sold
  <img width="640" alt="mark_as_sold" src="https://github.com/jasonyaj/IKWIG/assets/124213154/c2f79da5-88f0-4e7d-b646-6e98fe61251e">

## Technologies Used

- Python Flask
- HTML, CSS, and Bootstrap
- Jinja2
- AJAX, jQuery, and RESTful routing
- MySQL Workbench
- HTML validations as well as server-side validations and Bcrypt for secure login
- Custom API

## Functionality

Upon logging in, the user is taken to their personal virtual garage. When a car is created, the car will be selectable on the "Current Collection" list. Selecting a car on the list will display the information as well as photo entered by the user.

On the add a car page, users are able to enter specific information about their car. The fields include year, make, model, trim, color, vin, and a description box for for further details. One photo is allowed to be uploaded with the entry.

While a car is selected in the "Current Collection" list, the user is able to update the information of that car. All info as well as a photo will be able to be changed. Also while selected, a car can be moved to the "Sold" list by clicking the "Mark As Sold" button. In the "Sold" list cars will still be available for viewing but will no longer be available for updating.

[Return to Table of Contents](https://github.com/jasonyaj/IKWIG#table-of-contents)
