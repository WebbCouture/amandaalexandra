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
- [Deployment](#deployment)
- [Security](#security)
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

- View product lists
- View product details
- Search products
- Filter by category
- Sort by price and rating

### Account Management

- Register and log in
- Reset password

### Authentication

Authentication is implemented using django-allauth.

### Purchasing

- Add items to bag
- Checkout securely with Stripe

---

## User Experience (UX)

### Strategy Plane

Simple and secure shopping experience.

### Scope Plane

- Authentication
- Product browsing
- Shopping cart
- Payments

### Structure Plane

- Home
- Shop
- Cart
- Checkout
- Profile

### Skeleton Plane

Wireframes used for layout planning.

### Surface Plane

Soft pink and purple brand styling.

---

## Design and Visual Customisation

Customised UI based on course material and branding.

---

## Wireframes

Located in `docs/readme-img/wireframes/`.

---

## Features

- Authentication system
- Product filtering
- Search and sorting
- Stripe checkout
- Responsive design
- Admin dashboard

---

## Improvements Beyond Course Material

- Improved image handling
- Enhanced user feedback
- Defensive coding

---

## Shopping Bag

- Session-based bag
- Quantity updates
- Removal
- Free delivery threshold

---

## CRUD Functionality

- Create: add to bag
- Read: view bag
- Update: modify quantity
- Delete: remove item

---

## Checkout & Orders

- Automatic order numbers
- Stripe integration
- Django signals

---

## Form Validation

Django forms validate checkout data.

---

## Payments

Stripe PaymentIntents and webhooks.

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

- Python
- Django
- PostgreSQL
- Stripe
- Heroku
- GitHub

---

## Technical Notes

- Automatic totals
- Django signals
- Centralized delivery logic

---

## Python Logic

- Conditional delivery
- Loop calculations
- Signal updates

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

Manual and responsive testing performed.

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
```

---

## Deployment

Deployed on Heroku with PostgreSQL.

### Heroku Steps

```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic
```

---

## Security

- Environment variables for secrets
- DEBUG disabled in production
- Secure password hashing
- Stripe payments

---

## Known Issues

- Email confirmation shown in console

---

## Bugs Fixed

- Profile menu duplication
- Delivery calculation bugs
- Admin field issues

---

## Credits

- Django Documentation
- Stripe Documentation
- Developer communities and online forums
- Family, friends, and Brian Macharia, my mentor
- Project created by Amanda Alexandra (2026)
