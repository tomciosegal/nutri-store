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
Every athlete knows healthy food is 70% of success and supplements fill the rest to suplly vitamins and nutrition's. supplements most of thetime dont come from 
the nature they are Lab built, therefore using and promoting organic and vegan supplements can help reduce intake of unwantedsubstances.
This website is designed to create an impression of cleanness  and richness of the product accompanied with smooth and effortless online shopping experience. 
Specifically targeted at customers who want to support they effort with the cleanest, pure, raw materials, to provide pure clean recovery to their body. 

All images displayed are stored in an [AWS S3](https://aws.amazon.com/s3/) bucket, as are static files like CSS, icons and user-uploaded profile pictures.

The project is hosted at [Heroku](https://www.heroku.com/). A [Postgresql](https://www.postgresql.org/) database, also hosted at Heroku, is used to store image data and user data.

# UX

## Goals

### Visitor Goals

The central target audience for Nutristore are:
- People who are looking for supplements free of artificial fillers and excipients.
- Athletes who will experience better taste & nutrient absorption.
- People who value supplements with no toxic chemicals or harmful toxins.
- Visitors to the site are interested in how the product was produced and where it came from.

User goals are:
- Find a supplements that wont harm your body.
- Find a product that will provide cleanest source of nutrition's.
- Enjoy the amazing taste and flavor.
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
- Build brand awareness by including all the colors, fonts and logo associated with The Nutristore.
- Build The Nutristore newsletter subscriptions.
- Fast and efficient delivery.
- Make sales of products easy for buyers to increase sales conversion.
- The presentation and layout of the site may not cause consternation, loss, or a desire to resign from shopping.

## User Stories

A Visitor to The Nutristore website  expects/wants/needs:

1. As user I want The site to be easy to navigate from any device, desktop, tablet or phone. For the content to look good and be usable on all of these devices.

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

The Nutristore website has an overall Lab style, where viewer can feel cleanness  of the product and used clean ingredients
to build formula.

### Fonts
- The primary font [Work Sans](https://fonts.google.com/specimen/Work+Sans?selection.family=Roboto:wght@400;700&query=work) was chosen for the main text of the site because of it clear readability.

### colors

- light green: #79ba18;
- green: #008000
- light grey: #e3e1e1

- The brand colors for this project were chosen to make to create the impression of a clean, sterile room where natural supplements are produced. thus, we want to ensure a potential customer about the purity of our product.
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

- In the middle of the header user can find a useful search box where you look for desired item for example "protein"
  
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
    the navigation bar changes to drop downtoggle with categories to choose from.

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

- In the center of the footer icons with ways of payment accepted ways to finalize transaction. 

- A social media icons are listed on the right hand side of the footer. Under media icons visitor can find
  useful info about store (opening times phone number location)

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

- The home page comprises of two rows of products divided on 4 columns in each row, and it will display maximum of
  8 products per page. 

- Every product is wrapped in panel-body that nicely hovers when mouse on.

- When clicking on the image or product name user will be directed to product details where more info will be displayed.

## Bottom of Home Page

<br/>

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/main-page-bottom.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

<br/>


- At the bottom of the page user will find pagination that is responsible for displaying maximum of 8 products per page,
mobile and tablet same same feature provided.

- Directly under pagination visitor will find subscription button for customers willing to get most updated offers.
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

- The about page features a The Nutristore logo and a information's that will bring a customer closer to a process of
  manufacturing and ingredients used and chemical free produce.
***
<br/>


### Contact Page

<br/>

- The contact page contains a form for the user to fill in to send the shop owner an email.
- Name, email address and message are all required fields so that the shop owner receives all the information she needs to respond.
- If the user is logged in then their email address will already be populated in the email field.
- When the user clicks "send" the email is processed and sent via emailjs to The House of Mouse email address.
***
<br/>


### Register Page

<br/>


- A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields. 
- Information about what characters are accepted by these fields is displayed with the form.
- If a user who is already logged in tries to access this page, they are redirected to the home page.

***
<br/>


### Login Page

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
    This changes will be visible with the next checkout process as input will be auto populated.

- **My Orders**, where a user can see a summary of all their previous orders and all orders are populated by date for easier search. 
***
<br/>

### Log out page
- Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared. 
  The message on top page will inform the user what action was made. After login back in the users cart will still remain
  with all items previously selected to buy.
***
<br/>


### Checkout

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

- The total amount and cart view is available to see in top right corner of the page.

- A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change.

- User can avail 10% discount when spending at least 50 Euro, and this message will be populated under summary order
  center of the page with exact amount saved depending on total amount.

- User that is not logged in will be directed to login page that also gives option to register. Only registered customer will be able to proceed to the checkout page. 

- Very important feature that starts in cart is that the user always have a two buttons to click KEEP SHOPPING or
 CONTINUE to Payment, this way user is never forced to use back button in the browser.

<br/>

- Here customer is introduced to items selected during shopping and total price.
- If applicable, amount saved thanks to discount provided will be displayed next to total.
- Here the user has option to:
    - amend amount of items purchased
    - delete item if necessary 
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
    - Shipping page does not contain footer nor header to make user focus on buying processes rather then give some extra thoughts or distractions.
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
    - Giving staff the ability to up selland that could increase sale
    - Ability to print out reports of sale by seler so they could participate in up selling contest
    - Update order as  "we have received your payment" after "pending" then  "ready for dispatch"  and finally "shipped".
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

- Testing information can be found in every app in the folder "tests", where they separated in to:
    - tests_view
    - tests_models
    - plus one test_unit in checkout app

- To run test simply write in CLI this commands:
    - to run test in all apps write in CLI:
        - python3 manage.py test
    - to run test in desired app write command in CLI:
        - coverage run --source=name of app manage.py test
    - to check coverage write this command in CLI:
        - coverage report
    - to check what tests are missing and display it in html view write command in CLI:
        - coverage html
        
        <br/>

        - you need to open index.html which you will find in htmlcov file that will be auto created after installing coverage 
          in to your IDE. in that file you will be able to see what tests are missing in html view.

- MOST IMPORTANT: in order to run coverage tests you need to install coverage.
    - In order to install coverage write in CLI this command:
        - pip3 install coverage
            - this will generate htmlcov file in your IDE. 

## Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognize the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
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
- [Am I Responsive](http://ami.responsivedesign.is/#) - developer tried to use this website to check responsiveness,
however Django has build in protection that does not allow to do it.

<br/>

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used use the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `.bashrc` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and paste all of the default variables from env.py  in to Heroku's Config Vars section.

| Default quote | Your key | 
--- | --- 
os.environ.setdefault | "EMAIL_ADDRESS","your_mail@gmail.com" | 
os.environ.setdefault | EMAIL_PASSWORD", "your_password" | 
os.environ.setdefault | "DATABASE_URL", "postgres://your postgres key, you get it from heroku") | 
os.environ.setdefault | "STRIPE_PUBLISHABLE", "pk_test_your_key_goes_here" | 
os.environ.setdefault | "STRIPE_SECRET", "sk_test_dtripe_key_goes_here" | 
os.environ.setdefault | "SECRET_KEY", "secret_key_goes_here" | 
os.environ.setdefault | "AWS_ACCESS_KEY_ID", "access_key_goes_here" | 
os.environ.setdefault | "AWS_SECRET_ACCESS_KEY","secret_access_key_goes_here" |  

7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in the `.bashrc` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.
11. Went to the **S3** section of AWS and created a new S3 bucket.
12. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    ```
13. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
14. Updated the `settings.py` file with the relevant configuration for static and media file storage.
15. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
16. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

17. Created a Procfile using the following command in the terminal window:

    ```web: gunicorn nutristore.wsgi:application> Procfile```

18. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Nutristore](https://nutristore-cygal.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Nutristore GitHub Repository](https://github.com/tomciosegal/nutri-store)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository]https://github.com/tomciosegal/nutri-store)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env,py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

13. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
14. Set the following config vars in heroku :

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/config-vars.jpg" alt="TheNutristore github-download" aria-label="Nutristore" />
</div>

<br/>

Once the migrations are completed and the super user has been created successfully, the site should be running locally.

### Media And Static Folders

During development, my `static` and `media` folders weren't pushed to GitHub only in the early parts of the project.
During the progress developer was instructed to keep them in .gitignore file, as they are hosted in my S3 bucket for 
the live version of the site.


  
To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    - [emailjs](https://www.emailjs.com/)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.


### In Gitpod you create env.py file in main directory and write in first line: import os. Use table below to copy required fields.

<br/>


| Default quote | Your key | 
--- | --- 
os.environ.setdefault | "EMAIL_ADDRESS","your_mail@gmail.com" | 
os.environ.setdefault | EMAIL_PASSWORD", "your_password" | 
os.environ.setdefault | "DATABASE_URL", "postgres://your postgres key, you get it from heroku") | 
os.environ.setdefault | "STRIPE_PUBLISHABLE", "pk_test_your_key_goes_here" | 
os.environ.setdefault | "STRIPE_SECRET", "sk_test_dtripe_key_goes_here" | 
os.environ.setdefault | "SECRET_KEY", "secret_key_goes_here" | 
os.environ.setdefault | "AWS_ACCESS_KEY_ID", "access_key_goes_here" | 
os.environ.setdefault | "AWS_SECRET_ACCESS_KEY","secret_access_key_goes_here" |  

<br/>

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

- Special thanks to my mentor [Ignatius Ukwuoma](https://github.com/ignatiusukwuoma) for his time, expertise and friendship through my entire journey through the Code Institute full stack web development course
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




    

  
