[![Build Status](https://travis-ci.org/tomciosegal/nutri-store.svg?branch=master)](https://travis-ci.org/tomciosegal/nutri-store)

## Overview
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

1. The site to be easy to navigate from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information.

1. Not to be confused by the layout or process of payment, and be able to easy find what i am looking for.

1. The information presented on the site must be clear and easy to understand. they cannot cause misinformation

1. To be able to subscribe for the newest products and promotions.

1. All information and photos must be arranged in a clear and eye-catching manner, regardless of the size of the screen I use

1. In order to avoid unawareness of purchase, product information must be sufficiently clear to understand.

1. A clear terms and conditions and privacy policy.

1. A text search function so that I can quickly narrow down my search when looking for something specific.

1. To be able to see a summary of my order on every page of the checkout process.

1. When I am logged in I can access my account details and update them if I need to. 

1. To be able to find information on my past orders. 

1. To be able to easily get in contact with the shop owner via a contact form.


## Design Choices

The Nutristore website has an overall Lab style, where viewer can feel cleanneses of the product and used clean ingredients
to build formula.

### Fonts
- The primary font 'Work Sans' was chosen for the main text of the site because of it clear readability.

### Colours

- light green: #77ac3c;
- green: #79b03e
- light grey: #e3e1e1

- The brand colours for this project were chosen to make to create the impression of a clean, sterile room where natural supplements are produced. thus, we want to ensure a potential customer about the purity of our product.
- The grenn was chosen to provide a highlighting contrast for links, prices and important buttons for the user such as "add to cart" and "checkout now".

## Wireframes

- [Home](https://nutri-store.s3-eu-west-1.amazonaws.com/media/wireframes/lg-screen-nutristore.jpg)
- [About](https://nutri-store.s3-eu-west-1.amazonaws.com/media/wireframes/about.jpg)
- [Profile](https://nutri-store.s3-eu-west-1.amazonaws.com/media/wireframes/profile.jpg)
- [Contact](https://nutri-store.s3-eu-west-1.amazonaws.com/media/wireframes/contact.jpg)

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


#### Navbar:

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar.jpg" alt="TheNutristore Navbar on desktop devices" aria-label="Nutristore" />
</div>

- The navbar features on every page  but along with header does not display on checkout pages in order to
  to remove distractions and links that would take the user away from their cart once they decide to start the checkout process.

- In desktop view on the left side of the navbar is a list of the categories:View All, Protein, Carbs, Merch.


<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-tablet.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

- In tablet view the logo remains in the left side of the navigation bar, where users would expect it to be.


<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-mobile.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

- In mobile view the logo moves to the top center of the page, search input is not displayed to save room on small screens
    the navigation bar changes to dropdown toggle with categories to choose from.



#### Footer

![Footer]
(https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/footer-lg-screen.jpg)

- The footer background of grey was chosen to provide same contrast as navbar. The Headings are displayed same color as navbar.

- The footer features the copyright information for The Nutristore.

- In the center of the footer icons with ways of payment swoing acceped ways to finalise trnasaction. 

- A social media icons are listed on the right hand side of the footer. Under media icons visitor can find
  usefull info about store (opening times phone number location)

- Footer also contains about, delivery information, return policy, contact pages where user would expect to find important
    information about policy and store it self.


<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/footer-mobile.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

- In the mobile view footer aligns all features one under another one.

### Home Page

![Top of Home Page]

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/main-page.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>


- The home page comprises of two rows of products devided on 4 colums in each row, and it will display maximum of
  8 products per page. 

- Every product is wrapped in panel-body that nicely hovers when mouse on.

- When clicking on the image or product name user will be directed to product details where more info will be displayed.

![Bottom of Home Page]

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/main-page-bottom.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>


- At the bottom of the page user will find paginator that is responsible for dispalying maximum of 8 products per page,
mobile and tablet same same feature provided.

- Directly under paginator visitor will find subscribtion button for customers willing to get most updated offers.

**Product details**
- The product **title, price and description** are all clearly visible on top of the product panel.
- Larger image gives a customer an better overview what is about to buy
- Next to the product image is standard information that is applicable to all products in the shop. 
- From this point customer can either add desired item to basket go back shopping or  do checkout if any items in cart. 

<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/product-details.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>

### About page

- The about page features a The Nutristore logo and a informations that will bring a customer closer to a process of
  manufactiuring and ingredients used and chemical free produce.

### Contact Page

- The contact page contains a form for the user to fill in to send the shop owner an email.
- Name, email address and message are all required fields so that the shop owner receives all the information she needs to respond.
- If the user is logged in then their email address will already be populated in the email field.
- When the user clicks "send" the email is processed and sent via emailjs to The House of Mouse email address.

### Register Page

![Register page on different screen sizes](https://i.ibb.co/TvR9Rn8/register-responsive.png)

- A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields. 
- Information about what characters are accepted by these fields is displayed with the form.
- If a user who is already logged in tries to access this page, they are redirected to the home page.

### Login Page
- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and relevant feedback is sent to the user when they sign in.

### Account Page

![Account page on different screen sizes](https://i.ibb.co/27GrNtP/account-responsive.png)

- The users account page can only be accessed by a logged in user. Any user not logged in who tries to access this page will be redirected to the login page.
- The account page is split into two sections:
    - **Profile Info**, where the user can update their username and email address, and where they can add or update their first and last name.
    - **My Orders**, where a user can see a summary of all their previous orders. request a cancellation, and view the order status. 

### Log out page
- Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared. They are taken to a page that informs them that they have been logged out and provides a link to log back in if they wish.

### Cart page

- The shopping cart page features a summary of all the items the user has added to their cart.
- Each list item includes a picture of the item, the item title and price.
- A cross symbol at the top right of each list item gives the user the ability to delete that item from their cart.
- A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change.
- Information is provided for the user to tell them that tax is already included in the price they saw, and that the shipping cost will be calculated during checkout.

#### Checkout

![Checkout page on different screen sizes]

(https://i.ibb.co/vV2r6NL/checkout-responsive.png)

- Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity. A link is provided at the top of this for the user to return to the cart page to make changes to the order.
    - On mobile devices this order summary is part of a closed accordian, the top part of which displays the total cost. It can be clicked to open the full order details. This was done to save space on a smaller screen.
    - On tablet devices and larger screens, the order summary is displayed in full on the right side of the screen on all checkout pages.

- The checkout process is broken up into 4 stages. The reason for this was to break up the process into small steps as is common in online shops.

    1. **Info**
        - Here the user is asked to provide the shipping name and address to send their order to. They are also asked to select the country their order will go to, this is used to calculate the shipping price.
        - Not every country in the world is currently included on the list of shipping destinations. This was done in part to save time in making multiple entries into the database, and also because after running this shop for over 10 years the owner knows which destinations her products are usually shipped to. 
        - For the unlikely case that someone wishes to ship to a country not in the list, a link at the bottom of the form says "My country is not on the list?" and opens a modal encouraging the user to request their country be added to the shipping destinations.
        - The "Continue to shipping" button leads the user to the shipping page.

    2. **Shipping**
        - The shipping page includes all the information that the user has provided so far: Their contact email address (taken from when they created their account), the shipping name and address, and their order summary. A link is provided where the shipping address is displayed so that the user can return to the info page to update it.
        - This page provides the user with shipping options to choose from. At this point there is only one shipping option available, however this page and functionality have been left in so that other options such as expedited shipping may be added with a future release.
        - As a shipping method is automatically selected, the order summary now reflects the total cost including shipping. 
        - The "Continue to payment" button leads the user to the payment page hosted by Stripe.

    3. **Payment**
        - As stripe now offer a pre-built checkout in their latest version 3, I opted to use this as my payment page, as it hands over much of the back end coding needed for making payment to Stripe.
        - The Stripe payment page includes a summary of what the user is buying, and fields to enter credit card information.
        - All the validation and messages to the user on this page are handled by stripe.
        - On clicking the "Pay" button and on successful completion of payment, the user is redirected to the order confirmation page back on The House of Mouse website.

    4. **Confirmation of order**
        - The order confirmation page gives the customer all the information they need going forward. The shipping address and expected shipping time are provided. As well as links to the users account page and the contact page should they need to get in touch with the shop owner.
        - Finally the user is invited to return to the shop with a call to action button at the bottom of the page.

#### Terms and Conditions / Privacy Policy pages

- Every trustworthy online shop provides the legal documentation expected by the user on their site. Although these documents are a legal requirement of any online shop, including them also helps users to feel they can trust the outlet.















