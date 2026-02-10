# AmandaAlexandra – 3D Print Shop

Live Site: https://fast-peak-51750-1269072e4677.herokuapp.com/

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Stories](#user-stories)
- [User Experience (UX)](#user-experience-ux)
- [Design and Visual Customisation](#design-and-visual-customisation)
- [Wireframes](#wireframes)
- [Features](#features)
- [Improvements Beyond Course Material](#improvements-beyond-course-material)
- [Shopping Bag](#shopping-bag)
- [CRUD Functionality](#crud-functionality)
- [Checkout & Orders](#checkout--orders)
- [Form Validation](#form-validation)
- [Payments](#payments)
- [Data Model](#data-model)
- [Relationships](#relationships)
- [Technologies Used](#technologies-used)
- [Technical Notes](#technical-notes)
- [Python Logic](#python-logic)
- [Apps](#apps)
- [Testing](#testing)
- [Local Setup](#local-setup-development)
- [Deployment](#deplo)
- [Security](#)
- [Known Issues](#known-issues)
- [Bugs Fixed](#bugs-fixed)
- [Credits](#credits)

---

## Project Overview

AmandaAlexandra is an e-commerce platform for selling custom 3D printed products.
The website allows users to browse products, create accounts, and securely
purchase items online using Stripe.

The platform is designed to support small-scale digital manufacturing and
provide customers with personalized products.

---

## Tech Stack

- Python 3.x
- Django 3.2
- PostgreSQL (production) / SQLite (development)
- HTML, CSS, JavaScript
- Stripe API
- Heroku

---

## User Goals

- Easily browse and purchase 3D printed products
- View clear product images and descriptions
- Search, filter, and sort products efficiently
- Complete secure online payments
- Use the website on mobile, tablet, and desktop devices
- Feel confident using a secure and reliable platform

---

## Site Owner Goals

- Sell 3D printed products online
- Manage products and categories
- Track customer orders
- Build the AmandaAlexandra brand
- Provide a smooth and professional shopping experience
- Create a scalable online business

---

## User Stories

### Viewing and Navigation
- As a shopper, I want to view a list of products so that I can choose items to purchase.
- As a shopper, I want to view product details so that I can make informed decisions.
- As a shopper, I want to search products by keyword so that I can find items quickly.
- As a shopper, I want to filter products by category so that I can narrow down my choices.
- As a shopper, I want to sort products by price, rating, or category so that I can browse efficiently.

### Account Management
- As a user, I want to register and log in so that I can access my profile.
- As a user, I want to reset my password if I forget it.

### Authentication

The website includes a user authentication system implemented with
django-allauth. Users can register, log in, and log out. Authentication
state is reflected in the navigation menu across the site.

### Purchasing
- As a shopper, I want to add items to my cart so that I can purchase multiple products.
- As a shopper, I want to securely pay for my order using Stripe.

---

## User Experience (UX)

### Strategy Plane
The website is designed for users who want to purchase stylish and custom 3D printed
products online.

### Scope Plane
- User authentication system
- Product listings with search, filtering, and sorting
- Shopping cart functionality
- Stripe payment integration

### Structure Plane
- Home
- Shop
- Cart / Checkout
- Profile

### Skeleton Plane
Wireframes were created for mobile, tablet, and desktop views.

### Surface Plane
The visual design uses a soft pink and purple color scheme to reflect the
AmandaAlexandra brand identity.

---

## Design and Visual Customisation

The website design was inspired by the course material but customised to reflect
the AmandaAlexandra brand identity.

---

## Wireframes

See images in `docs/readme-img/wireframes/`.

---

## Features

- User registration and login system
- Product listing with category filtering
- Search and sorting
- Secure Stripe checkout
- Responsive design
- Admin dashboard

---

## Improvements Beyond Course Material

- Robust image handling
- Improved user feedback
- Defensive coding practices

---

## Shopping Bag

- Session-based shopping bag
- Quantity update and removal
- Free delivery threshold

---

## CRUD Functionality

- Create: add products to bag
- Read: view bag contents
- Update: change quantities
- Delete: remove items

---

## Checkout & Orders

- Order model with automatic order numbers
- Stripe integration
- Django signals for totals

---

## Form Validation

Checkout uses Django forms with server-side validation.

---

## Payments

Stripe is integrated using PaymentIntents and webhooks.

---

## Data Model

- User
- UserProfile
- Category
- Product
- Order
- OrderItem

---

## Relationships

- User → UserProfile
- Category → Product
- Order → OrderItem
- Product → OrderItem

---

## Technologies Used

- Python, Django
- PostgreSQL
- Stripe
- Heroku
- GitHub

---

## Technical Notes

- Automatic total calculations
- Django signals
- Centralized delivery logic

---

## Python Logic

- Conditional delivery logic
- Loops for totals
- Signal-based updates

---

## Apps

- home
- accounts
- products
- bag
- checkout
- profiles

---

## Testing

Manual and responsive testing performed throughout development.

---

## Local Setup (Development)

```bash
git clone https://github.com/AmandaAlexandraStudio/3DPrints.git
cd 3DPrints
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## Deployment

The project is deployed using Heroku and connected to a Heroku Postgres database.

---

### Heroku Deployment Steps

1. Create a Heroku application  
2. Configure environment variables  
3. Connect GitHub repository  
4. Deploy the main branch  
5. Set up PostgreSQL database  

```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic
```

The live site is continuously deployed from GitHub.

Security

Sensitive keys are stored in environment variables

Django DEBUG mode is disabled in production

User passwords are securely hashed

Payment processing is handled securely via Stripe

Known Issues

Email confirmation is displayed in the console during local development.

Some admin features are restricted to superusers only.

No critical bugs are currently known.

Bugs Fixed

Fixed duplicate "My Profile" entries in the account dropdown menu

Corrected delivery cost calculation to ensure free delivery is applied above the threshold

Ensured order totals update correctly when order line items are modified or deleted

Resolved admin interface issues where calculated fields were incorrectly editable

Credits

Django Documentation

Stripe Documentation

Online developer communities and forums

Brian Macharia, mentor

Wireframes and design created by AmandaAlexandra

All product images and content created or licensed by the site owner

Project created and developed by Amanda Alexandra (2026)


