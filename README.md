<h1 align="center">IKWIG</h1>

<p align="center"><i>A Virtual Garage For the Collector</i></p>

---

## Table of Contents

- [Background](https://github.com/jasonyaj/IKWIG#background)
- [Features](https://github.com/jasonyaj/IKWIG#features)
- [Technologies Used](https://github.com/jasonyaj/IKWIG#technologies-used)
- [Functionality](https://github.com/jasonyaj/IKWIG#functionality)

## Background

Having a big interest in cars I have found that there is no app to keep track of my vehicle collection. There was a need to record previous cars owned as well as current cars in possession. I designed this web app to keep detailed information and be able to display the data to the user.

[Return to Table of Contents](https://github.com/jasonyaj/IKWIG#table-of-contents)

## Features

- Login/Registration with validations

  <img width="640" alt="login_register" src="https://github.com/jasonyaj/IKWIG/assets/124213154/10c79a52-df13-4439-8aa9-5c7aa39108cb">

- My Garage

  <img width="640" alt="my_garage" src="https://github.com/jasonyaj/IKWIG/assets/124213154/5fd05ae2-265c-4e27-aeef-3c0cd1004b1c">

- Add

  <img width="640" alt="add" src="https://github.com/jasonyaj/IKWIG/assets/124213154/435b58a3-9f46-4d5e-a72b-ea3b836f6d46">

- Update

  <img width="640" alt="update" src="https://github.com/jasonyaj/IKWIG/assets/124213154/684ad4bb-530c-47e1-9500-5d1e7708cd9d">

- Mark as Sold

  <img width="640" alt="mark_as_sold" src="https://github.com/jasonyaj/IKWIG/assets/124213154/c9427714-1502-40d4-8b25-8fa0caf4a4f3">

[Return to Table of Contents](https://github.com/jasonyaj/IKWIG#table-of-contents)

## Technologies Used

- Python Flask
- HTML, CSS, and Bootstrap
- Jinja2 and RESTful routing
- MySQL
- HTML validations as well as server-side validations and Bcrypt for secure login
- Custom API

[Return to Table of Contents](https://github.com/jasonyaj/IKWIG#table-of-contents)

## Functionality

Upon logging in, the user is taken to their personal virtual garage. When a car is added, the car will be selectable on the "Current Collection" list. Selecting a car on the list will display the information as well as photo entered by the user.

On the add a car page, users are able to enter specific information about their car. The fields include year, make, model, trim, color, vin, and a description box for for further details. One photo is allowed to be uploaded with the entry.

While a car is selected in the "Current Collection" list, the user is able to update the information of that car. All info as well as a photo will be able to be changed. Also while selected, a car can be moved to the "Sold" list by clicking the "Mark As Sold" button. In the "Sold" list cars will still be available for viewing but will no longer be available for updating.

[Return to Table of Contents](https://github.com/jasonyaj/IKWIG#table-of-contents)
