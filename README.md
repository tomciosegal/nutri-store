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

- The header features The Nutristore logo on the far left, which links to the home page of the site.

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

- The navbar features on every page, however developer would like to implement a functionality where footer nabar are not rendering oon checkout pages,
    unfortnatelly could not find proper guindence to do it.
- In desktop view on the left side of the navbar is a list of the categories:View All, Protein, Carbs, Merch.


<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-tablet.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>


<div align="center">
    <img src="https://nutri-store.s3-eu-west-1.amazonaws.com/media/images/navbar-mobile.jpg" alt="TheNutristore Header on desktop devices" aria-label="Nutristore" />
</div>




