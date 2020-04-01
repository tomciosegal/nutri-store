[![Build Status](https://travis-ci.org/tomciosegal/nutri-store.svg?branch=master)](https://travis-ci.org/tomciosegal/nutri-store)

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Header](#header)
        - [Navbar](#navbar)
        - [Footer](#footer)
        - [Home Page](#home-page)
        - [Product Details Page](#product-details-page)
        - [About Page](#about-page)
        - [Contact Page](#contact-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#profile-page)
        - [Checkout](#checkout)
            - [Cart Page](#cart-page)
            - [Shipping Page](#shipping-page)
            - [PaymentPage](#paymentt-page)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)
        - [Accounts App Models](#accounts-app-models)
        - [Checkout app models](#checkout-app-models)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - [Code Validation](#code-validation) 
    - [Manual Testing](#manual-testing)

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    
8. [Contact](#contact)

***

<br/>

# Overview
[The Nutristore](https://nutristore-cygal.herokuapp.com/) was built and deployed by Tomasz Cygal as his final project for 
the [Code Institute Full Stack Web Development Diploma](https://codeinstitute.net/). The project has been developed using [Django](https://www.djangoproject.com/), with the goal of 
fulfilling the requirements of the final, Full-Stack Milestone Project of the Code Institute Full-Stack Software Developer Course.
The  purpose of The Nutristore online shop is to promote organic food suplemennts. The advantages of organic
Unlike synthetic supplements, which can contain chemical compounds that don't occur in nature, organic supplements are free of pesticides, insecticides and other toxic ingredients.
Every athlete knows healthy food is 70% of success and suplements fill the rest to suplly vitamins and nutritions. Suplements most of thetime dont come from 
the nature they are Lab built, therefore using and promoting organic and vegan suplements can help reduce intake of unwated substances.
This website is designed to create an impession of cleanneses and richness of the product accompanied with smooth and effortless online shopping experience. 
Specifically targeted at customers who want to support they effort with the cleanest, pure, raw materials, to provide pure clean recovery to their body. 

All images displayed are stored in an [AWS S3](https://aws.amazon.com/s3/) bucket, as are static files like CSS, icons and user-uploded profile pictures.

The project is hosted at [Heroku](https://www.heroku.com/). A [Postgresql](https://www.postgresql.org/) database, also hosted at Heroku, is used to store image data and user data.

# UX

## Goals

### Visitor Goals

The central target audience for Nutristore are:
- People who are looking for suplements free of artificial fillers and excipients.
- Athlets who will experience better taste & nutrient absorption.
- People who value suplements with no toxic chemicals or harmful toxins.
- Visitors to the site are interested in how the product was produced and where it came from.

User goals are:
- Find a supplements that wont harm your body.
- Find a product that will provide cleanest source of nutritions.
- Enjoy the amazing taste and flavour.
- Buy from a trustworthy online shop.
- Show total price and number of items in cart.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.



The Nutristore online shop is a great way to meet these needs because:
- The website has been designed to provide a clear view of product visitors are looking for.
- Header was placed above navbar where visitor can find search box basic info access to account and cart.
- Using navbar Nutristore website can be searched by category, similar items and using text search, making it easy for customers to find specific things that interest them.

### Business Goals

The Goals of The Nutristore business are:
- Provide a professional online shop that helps the user to feel safe that they are buying from a trustworthy source. 
- Build brand awareness by including all the colours, fonts and logo associated with The Nutristore.
- Build The Nutristore newsletter subscriptions.
- Fast and efficient delivery.
- Make sales of products easy for buyers to increase sales conversion.
- The presentation and layout of the site may not cause consternation, loss, or a desire to resign from shopping.

## User Stories

A Visitor to The Nutristore website  expects/wants/needs:

1. As user I want The site to be easy to navigate from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. As new visitor I want ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information.

1. As new customer I dont want to be confused by the layout or process of payment, and be able to easy find what i am looking for.

1. I want the information presented on the site must be clear and easy to understand. they cannot cause misinformation

1. As customer I expect be able to subscribe for the newest products and promotions.

1. As new user I expect information and photos must be arranged in a clear and eye-catching manner, regardless of the size of the screen I use

1. In order to avoid unawareness of purchase, I want product information must be sufficiently clear to understand.

1. As ne user i expect a clear terms and conditions and privacy policy.

1. A text search function so that I can quickly narrow down my search when looking for something specific.

1. I need To be able to see a summary of my order on every page of the checkout process.

1. When I am logged in I can access my account details and update them if I need to. 

1. I expect to be able to find information on my past orders. 

1. I expect to be able to easily get in contact with the shop owner via a contact form.


## Design Choices

The Nutristore website has an overall Lab style, where viewer can feel cleanneses of the product and used clean ingredients
to build formula.

### Fonts
- The primary font [Work Sans](https://fonts.google.com/specimen/Work+Sans?selection.family=Roboto:wght@400;700&query=work) was chosen for the main text of the site because of it clear readability.

### Colours

- light green: #77ac3c;
- green: #79b03e
- light grey: #e3e1e1

- The brand colours for this project were chosen to make to create the impression of a clean, sterile room where natural supplements are produced. thus, we want to ensure a potential customer about the purity of our product.
- The green was chosen to provide a highlighting contrast for links, prices and important buttons for the user such as "add to cart" and "checkout now".

## Wireframes

Please click here to see all the [Wireframes](https://github.com/tomciosegal/nutri-store/tree/master/wireframes) created.

# Features
 
## Existing Features

### Elements on every page

#### Header:

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/header.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

- The header features on every page apart from the checkout pages. The Nutristore logo on the far left, which links to the home page of the site.

- Next to the The Nutristore logo a free shipping icon is placed, this link will direct to a details how user can avail free shipping.

- In the middle of the header user can find a usefull search box where you look for desired item for example "protein"
  
- On the right side of the header visitor can find the links to login,and shopping cart.

    - A user who is currently logged out will also see options to register or log into the website.

    - A user who is logged in will see options to view their profile page or log out.

- The shopping cart icon is located to the far right of the navigation bar. 

    
    - The shopping cart counter works even for a user who is not logged in. This is because all the information about which products the user has added 
      to their cart is stored in their session data. This makes it possible for a new user to add things to their cart before being asked to log in or register. 
      This way user can add items to cart without registering, however when user will go to cart and will try to do checkout he/she will be directed to login/register page.
    
    - When user logs in a cart will remain with items picked as anonymous user.

    - When user logs out and will log back in again a cart also will remain will items selected in session.

***

#### Navbar:

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar.jpg" alt="TheNutristore Navbar on desktop devices" aria-label="Nutristore" />
</div>

- The navbar features on every page  but along with header does not display on checkout pages in order to
  to remove distractions and links that would take the user away from their cart once they decide to start the checkout process.

- In desktop view on the left side of the navbar is a list of the categories:View All, Protein, Carbs, Merch.


- In tablet view the logo remains in the left side of the navigation bar, where users would expect it to be.

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-tablet.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>

- In mobile view the logo moves to the top center of the page, search input is not displayed to save room on small screens
    the navigation bar changes to dropdown toggle with categories to choose from.

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-mobile.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

***

<br/>

#### Footer

<br/>

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/footer-mobile.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>

- The footer background of grey was chosen to provide same contrast as navbar. The Headings are displayed same color as navbar.

- The footer features the copyright information for The Nutristore.

- In the center of the footer icons with ways of payment swoing acceped ways to finalise trnasaction. 

- A social media icons are listed on the right hand side of the footer. Under media icons visitor can find
  usefull info about store (opening times phone number location)

- Footer also contains about, delivery information, return policy, contact pages where user would expect to find important
    information about policy and store it self.

- In the mobile view footer aligns all features one under another one.

<br/>

***

### Home Page

## Top of Home Page

<br/>

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/main-page.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>

- The home page comprises of two rows of products devided on 4 colums in each row, and it will display maximum of
  8 products per page. 

- Every product is wrapped in panel-body that nicely hovers when mouse on.

- When clicking on the image or product name user will be directed to product details where more info will be displayed.

## Bottom of Home Page

<br/>

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/main-page-bottom.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>


- At the bottom of the page user will find paginator that is responsible for dispalying maximum of 8 products per page,
mobile and tablet same same feature provided.

- Directly under paginator visitor will find subscribtion button for customers willing to get most updated offers.
***
<br/>


### Product details

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/product-details.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>

- The product **title, price and description** are all clearly visible on top of the product panel.
- Larger image gives a customer an better overview what is about to buy
- Next to the product image is standard information that is applicable to all products in the shop. 
- From this point customer can either add desired item to basket go back shopping or  do checkout if any items in cart. 
<br/>

***
### About page

- The about page features a The Nutristore logo and a informations that will bring a customer closer to a process of
  manufactiuring and ingredients used and chemical free produce.
***
<br/>


### Contact Page

<br/>

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/contact-form.jpg" alt="TheNutristore contact-form" aria-label="Nutristore" />
</div>
<br/>


- The contact page contains a form for the user to fill in to send the shop owner an email.
- Name, email address and message are all required fields so that the shop owner receives all the information she needs to respond.
- If the user is logged in then their email address will already be populated in the email field.
- When the user clicks "send" the email is processed and sent via emailjs to The House of Mouse email address.
***
<br/>


### Register Page

<br/>
<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/contact-form.jpg" alt="TheNutristore contact-form" aria-label="Nutristore" />
</div>

<br/>


- A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields. 
- Information about what characters are accepted by these fields is displayed with the form.
- If a user who is already logged in tries to access this page, they are redirected to the home page.

***
<br/>


### Login Page

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/login-page.jpg" alt="TheNutristore login-form" aria-label="Nutristore" />
</div>
<br/>


- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and relevant feedback is sent to the user when they sign in.

<br/>

***

### Profile Page
<br/>
<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/profile-page.jpg" alt="TheNutristore profile-form" aria-label="Nutristore" />
</div>

<br/>


- The users account page can only be accessed by a logged in user if user not logged in the Profile icon is not displayed.

- The account page has basic info about user. All this details are saved after after filling shipping details,
  so user will have his profile filled after that step.

- Another feature related to profile is that when customer will decide to fill the details in profile page they will be automatically 
  saved and auto populated in shipping page from the first purchase.

- **Profile Info** has also very important feature where user can update any of the details.by clicking update button.
    This changes will be visible with the next checkout process as input will be autopopulated.

- **My Orders**, where a user can see a summary of all their previous orders and all orders are populated by date for easier search. 
***
<br/>

### Log out page
- Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared. 
  The message on top page will inform the user whataction was made. After loging back in the users cart will still remain
  with all items prevoiusly selected to buy.
***
<br/>


#### Checkout

<br/>

- Checkout process starts when you click on cart that will show user summary of the shopping he made. From here you can either go back and
  continue shopping or proceed to shipping details. 
    
- The checkout process is broken up into 3 stages. The reason for this was to break up the process into small steps as is common in online shops.

    <br/>

    ***

    1. **Cart**

        <br/>

    <div align="center">
        <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/cart-page.jpg" alt="TheNutristore cart-page" aria-label="Nutristore" />
    </div>

    <br/>


- The shopping cart page features a summary of all the items the user has added to their cart.

- Each list item includes a picture of the item, the item title and price.

- The total amount and cart view is availible to see in top right corner of the page.

- A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change.

- User can avail 10% discount when spending at least 50 Euro, and this message will be populated under summary order
  center of the page with exatc amount saved depending on total amount.

- User that is not logged in will be directed to login page that also gives option to register. Only registered customer will be able to proceed tothe checkout page. 

- Very important feature that starts in cart is that the user always have a two buttons to click KEEP SHOPPING or
 CONTINUE to Payment, this way user is never forced to use back button in the browser.

<br/>

- Here customer is introduced to items selected during shopping and total price.
- If applicable, amount saved thanks to discount provided will be displayed next to total.
- Here the user has option to:
    - amend amount of items purchased
    - delete item if neccessary 
    - keep shopping
    - proceed to checkout

        <br/>

        - The "Checkout" button leads the user to the shipping page.

    <br/>

    ***

    2. **Shipping**

    <div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/shipping-page.jpg" alt="TheNutristore shipping-page" aria-label="Nutristore" />
    </div>

    <br/>

    - Shipping details will be auto populated if user filled form in profile,if not after that step all the user details will be saved in profile 
           and in future shopping it will be filled automatically for customer.        
    - As a shipping method is automatically selected, user need to add shipping to the total amount, if 
          total is 60 Euro or more shipping will be free, and this will be stated in the column.
    - Shipping page does not contain footer nor header to make user focus on buying procces rather then give some extra thoughts or distractions.
    - The "Continue to payment" button leads the user to the payment page hosted by Stripe.

    <br/>

    ***

    3. **Payment**

    <br/>

    - The Stripe payment page includes a summary of what the user is buying, and fields to enter credit card information.
    - All the validation and messages to the user on this page are handled by stripe.
    - On clicking the "Pay" button and on successful completion of payment.
    - On the end a confirmation email is send to customer, thanking for shopping.
    
### Features for Future Releases

- Live Chat
- Sending an email to customer when their new order has been placed.
- Build staff pages to view all order and keep record of actual sale by seller.
    - Giving staff the ability to upsell and that could increase sale
    - Ability to print out reports of sale by seler so they could participae in upselling contest
    - Update order as  "we have recived your payment" after "pending" then  "ready for dispach"  and finnaly "shipped"  so that the customer is updated with this information until reciving products.
    - Integration with with delivery company while package is in transit.
    - "Call you back" in a minute button. Where user can request a call back for more info or to talk about product. Option only for registered customers only.
    
- Coupons and discount codes.
- Additional payment methods.
- Auto login when registering a new account
- Ability to build combo buys with items selected by seller
- Option to buy a gift vouchers

# Information Architecture

### Database Choice

- As a framework Django works with SQL databases. During development on my local machine I worked with the standard **sqlite3** database installed with Django.
- On deployment, the SQL database provided by Heroku is a **PostgreSQL** database. 

## Data Models

### User

The User model utilized for this project is the standard one provided by `django.contrib.auth.models`

### Products app model

Within the `products` app, the **Product** model holds all the data needed for the products in the shop.

**Product model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=100 | CharField
Shop category | category | choices=CATEGORY_CHOICES | CharField
Product id| id | primary_key=True | AutoField
Product name | name | max_length=255 | CharField
Product info | description | ---- | TextField
Price | price | max_digits=6, decimal_places=2, default=1 | DecimalField
Image | image | blank=True, null=True | ImageField
Description | description | ---- | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Currency | currency | max_length=3, default="EUR | CharField
Category | category | blank=True,null=True, on_delete=models.CASCADE | ForeignKey("products.ProductCategory")
Quantity | quantity | ---- | IntegerField

<br/>

**ProductCategory**
| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Id | id | primary_key=True | AutoField
Name | name | max_length=255 | CharField

<br/>

- The Product model uses Pillow to store all image files in an AWS S3 bucket.

### Cart app models
 
 <br/>

 **Cart(TimestampedModel)**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | User, on_delete=models.CASCADE | OneToOneField

<br/>

**CartItem**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Cart | cart | Cart, on_delete=models.CASCADE| ForeignKey
Product_id | product_id | ----- | IntegerField
Quantity | quantity | ---- | IntegerField

<br/>

### Accounts app model

<br/>

**Customer model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | OneToOneField to| User
Full Name | full_name | max_length=150 | CharField
Address line 1 | street_address1 | max_length=50, blank=True | CharField
Address line 2 | street_address2 | max_length=50, null=True, blank=True | CharField
Town / City | town_or_city | max_length=150 | CharField
County | county | max_length=20, blank=True | CharField
Postcode | postcode | max_length=10 | CharField
Date ordered | date_ordered | default=datetime.date.today | DateField
County | county | max_length=20 | CharField


### Checkout app models

<br/>

**Order model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
customer | customer | Customer, on_delete=models.CASCADE| ForeignKey
Total Cost | total_cost | decimal_places=2, max_digits=6 | DecimalField

    
- this model holds the user order history for admin panel
    
<br/>

**OrderItem model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order History | order_history | Order, on_delete=models.CASCADE| ForeignKey
Product | product | "products.Product", on_delete=models.CASCADE | ForeignKey
Quantity| quantity | ----- | IntegerField

<br/>

- this model holds the user order history item form admin panel

# Technologies Used

### Tools
- [Gitpod](https://gitpod.io/) is the IDE used for developing this project. 
- [Travis](https://travis-ci.org/) for continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Heroku](https://www.heroku.com/) for deployment


### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.



### Languages
- This project uses:
- HTML
- CSS
- JavaScript
- [Python](https://www.python.org/)

# Testing 

- Testing information can be found in every app in the folder "tests", where they seperated in to:
    - tests_view
    - tests_models
    - plus one test_unit in checkout app

- To run test simply write in CLI this commands:
    - to run test in all apps write in CLI:
        - python3 manage.py test
    - to run test in desired app write command in CLI:
        - coverage run --source=name of app manage.py test
    - to check coverage write this commandin CLI:
        - covearge report
    - to check what tests are missing and display it in html view write command in CLI:
        - coverage html
        
        <br/>

        - you need to open index.html which you will find in htmlcov file that will be auto created after installing coverage 
          in to your IDE. in that file you will be able to see what tests are missing in html view.

- MOST IMPORTANT: in order to run coverage tests you need to install coverage.
    - In order to install coverage write in CLI this command:
        - pip3 install covearge
            - this will generate htmlcov file in your IDE. 

## Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
- I used CLI to sort all my imports by using command  "isort -rc ."
- I used CLI to make sure line length is not going above 79 in one line by using command  "black --line-length=79"
- I used CLI to check all the errors in the code by using command  "flake8"
- I also removed some of the remaining errors manually

## Manual Testing

- I used Google Chrome's Development tools to constantly test each change that I<br/> 
made to my project and to ensure that it appeared in the desired way on different screen sizes. <br/>
- I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure <br/>
it appeared in the desired way on different devices.
- [Am I Responsive](http://ami.responsivedesign.is/#) - developer tried to use this website to check responsivnes,
however Django has build in protection that does not allow to do it.

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Gitpod](https://gitpod.io/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    
To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    - [emailjs](https://www.emailjs.com/)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions
1. Save a copy of the github repository located at https://github.com/tomciosegal/nutri-store by clicking the "download zip" button 
at the top of the page and extracting the zip file to your chosen folder. 
If you have Git installed on your system, you can clone the repository with the following command.
   
2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. 

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

      <br/>

    <div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/env.jpg" alt="TheNutristore github-download" aria-label="Nutristore" />
    </div>
    
    <br/>

    - In gitpod create env.py in file main directory, where you will keep all variables. In the file you need to import os.
    In order to do it write in first line: import os
  



    - If using an IDE that includes a bashrc file, open this file and enter all the environment variables listed above using the following format: 
    
    HOSTNAME="enter key here. in gitpod LOCALHOST"
    
    - HOSTNAME should be the local address for the site when running within your own IDE.
    - DEV environment variable is set only within the development environment, it does not exist in the deployed version, making it possible 
        to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on 
        the deployed site.

8. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

9. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

10. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

11. Once the program is running, go to the local link provided and add `/admin` to the end of the url. 



## Heroku Deployment

To deploy The Nutristore webshop to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. 
    Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
   For your convinience is recomended to set in heroku an autodeploy from github. This way every time you do push to github
   heroku will read changes and built up an app with latest push.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

    <br/>

    <div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/config-vars.jpg" alt="TheNutristore github-download" aria-label="Nutristore" />
    </div>

    <br/>


8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account.

# Credits

## Content
- Order Confirmation [Shopify](https://github.com/Cam/Shopify-HTML-Email-Templates/blob/master/Order%20Confirmation.html)

-  Inspiration was taken from fallowing websites:
    - [Organic Muscle](https://www.organicmuscle.com/)
    - [Bulk Powders](https://www.bulkpowders.ie/)
    - [Global Healing](https://globalhealing.com/natural-health/organic-supplements/)
    - [Shopify](https://en.shopify.nl/tools/policy-generator/terms-and-conditions)
    

- Text to about page was taken from [Organic Muscle](https://www.organicmuscle.com/)

## Images
- All product photography was taken from [Bulk Powders](https://www.bulkpowders.ie/).

## Text verification

- To check and verify entire vocabulary in Readme.md file developer used  [Spell Checker](https://www.reverso.net/spell-checker/english-spelling-grammar/)  

## Acknowledgements

- I received inspiration for the style of my project from [Bulk Powders](https://www.bulkpowders.ie/)
- Thanks to everybody on SLACK that help me when I was stuck and needed assistance. Thanks Tutors aswell. They help me to debug my Python code.

- Special thanks to my mentor [Ignatius Ukwuoma](https://github.com/ignatiusukwuoma) for his time, expertise and friendship through my entire journey through the CodeInstitute full stack web development course
Thank to his incredible knowledge and patience that helped me get so far.

<br/>

 <div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/mentor-ci.jpg" alt="TheNutristore master-yoda" aria-label="Nutristore" />
    </div>

<br/>


- Many thanks  [Simen Daehlin alias Yoda](https://github.com/Eventyret) for his time to give an extra review to my last project as his remarks are
more then professional, well know and lot appreciated in our Code Institute environment.

<br/>

 <div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/master-yoda.jpg" alt="TheNutristore master-yoda" aria-label="Nutristore" />
    </div>

<br/>

- With thanks also to my many coding tutors and slack friend for having patience with my question and issues thruout entire course, who have tested, helped troubleshoot and debug:
    - Tim
    - Micheal
    - Xavier
    - Cormac
    - Haley
    - Stephen
    - Anna 
    - Niel
    - Sammy
    - Scott 

<br/>

# And finally thanks to my wife who gave me precious time so I can work on my projects, she is biggest support I can imagine.


# Contact

To contact me feel free to email

tomaszcygal@yahoo.com

## This project is for educational purposes only.




    

  
