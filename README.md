# AmandaAlexandra – 3D Print Shop

Live Site: https://fast-peak-51750-1269072e4677.herokuapp.com/

---

## Project Overview

AmandaAlexandra is a full-stack e-commerce platform for selling custom 3D printed products.
Users can browse products, create accounts, and complete secure online purchases using Stripe.

The platform is designed for small-scale digital manufacturing and focuses on usability,
security, and responsive design.

This project was developed as part of the Code Institute Diploma in Full Stack Software Development.

---

## Table of Contents

- Project Overview
- Tech Stack
- User Goals
- Site Owner Goals
- User Experience (UX)
- Agile Development
- Features
- CRUD Functionality
- Shopping Bag
- Checkout & Orders
- Payments
- Data Model
- Testing and Validation
- Local Setup
- Deployment
- Security
- Known Issues
- Bugs Fixed
- Credits

---

## Tech Stack

- Python 3
- Django 3.2
- PostgreSQL (Production)
- SQLite (Development)
- HTML, CSS, JavaScript
- Stripe API
- Heroku
- GitHub

---

## User Goals

- Browse and purchase products easily
- Create and manage personal accounts
- Track order history
- Complete secure payments
- Use the site on all devices

---

## Site Owner Goals

- Sell 3D printed products online
- Manage products and categories
- Track customer orders
- Maintain brand identity
- Provide a professional shopping experience

---

## User Experience (UX)

The site follows standard e-commerce design patterns to ensure a simple and intuitive user journey.

Main sections:

- Home
- Products
- Shopping Bag
- Checkout
- Profile
- Admin Panel

The interface uses soft brand colours and responsive layouts.

---

## Agile Development

The project was developed using an iterative Agile-inspired approach.

Development was managed through GitHub commits and incremental feature implementation.
Features were built, tested, and refined continuously throughout development.

---

## Features

- User authentication using django-allauth
- Product browsing, filtering, and sorting
- Search functionality
- Shopping bag with live totals
- Stripe checkout
- Order confirmation
- Profile page with order history
- Admin product management
- Responsive layout

---

## CRUD Functionality

CRUD operations are implemented across the platform.

### Products (Admin)
- Create: Add products
- Read: View products
- Update: Edit products
- Delete: Remove products

### Shopping Bag
- Create: Add items
- Read: View bag
- Update: Change quantities
- Delete: Remove items

---

## Shopping Bag

- Session-based shopping bag
- Quantity adjustment
- Item removal
- Automatic total calculation
- Free delivery threshold logic

---

## Checkout & Orders

- Secure checkout with Stripe
- Automatic order numbers
- Order summary
- Order confirmation
- Profile order history
- Django signals used for updates

---

## Payments

Stripe PaymentIntents and webhooks are used for secure payments.

### Stripe Testing

Test Card Details:

- Card Number: 4242 4242 4242 4242
- Expiry Date: Any future date
- CVC: Any 3 digits

These credentials can be used to test the checkout process.

---

## Data Model

The application uses a relational PostgreSQL database.

Main models:

- User
- UserProfile
- Category
- Product
- Order
- OrderLineItem

### Relationships

- One User → One UserProfile
- One Category → Many Products
- One Order → Many OrderLineItems
- One Product → Many OrderLineItems

This structure ensures data integrity and efficient querying.

---

## Testing and Validation

### Validation Screenshots

Due to a database and deployment crash shortly before submission,
full documentation screenshots could not be recreated in time.

However, all validation and testing was completed during development.

### Testing Summary Table

All validation and testing tools were used according to course requirements.

| Test Type        | Tool Used                | Files / Pages Tested                         | Result        |
|------------------|--------------------------|----------------------------------------------|---------------|
| HTML Validation  | W3C Markup Validator     | Home, Products, Bag, Checkout, Profile        | Passed        |
| CSS Validation   | W3C CSS Validator        | base.css                                     | Passed        |
| JavaScript Test  | JSHint                   | bag.js, stripe_elements.js, countryfield.js  | Passed        |
| Python Validation| Manual Review / Flake8   | Views, Models, Forms                          | Passed        |
| Performance Test | Google Lighthouse        | Home, Products, Checkout, Profile             | Passed        |
| Manual Testing   | Browser Testing          | All User Journeys                             | Passed        |

All tests were completed successfully with no critical issues found.


#### HTML Validation

All main templates were validated using the W3C Markup Validator.

Validated pages:
- Home
- Products
- Product Detail
- Shopping Bag
- Checkout
- Profile
- Authentication pages

No critical errors were found.

#### CSS Validation

The main stylesheet (base.css) was validated using the W3C CSS Validator.
Only minor warnings related to vendor prefixes were reported.

#### JavaScript Validation

JavaScript files were tested using JSHint.

Validated files:
- bag.js
- stripe_elements.js
- countryfield.js

No critical errors were detected.

#### Lighthouse Testing

Google Lighthouse audits were performed on key pages:

- Home page
- Products page
- Checkout page
- Profile page

All pages achieved acceptable scores for:

- Performance
- Accessibility
- Best Practices
- SEO

These tests confirm that the application meets modern web standards.


### Manual Testing

All core user journeys were manually tested on desktop and mobile devices.

Verified functionality:

- Registration, login, logout
- Product browsing and filtering
- Bag operations
- Checkout process
- Order confirmation
- Profile updates
- Admin management

Testing was performed using Google Chrome and Microsoft Edge on Windows 10,
as well as mobile simulation via Chrome DevTools.

### HTML Validation

Templates were validated using the W3C Markup Validator.
Django template tags were temporarily removed.
No critical errors were found.

### CSS Validation

The main stylesheet was validated using the W3C CSS Validator.
Minor warnings were noted.

### JavaScript Validation

JavaScript files were tested using JSHint.
No critical issues were detected.

### Lighthouse Testing

Lighthouse audits confirmed acceptable performance,
accessibility, SEO, and best practices.

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

## Deployment

The project is deployed on Heroku using PostgreSQL.

### Deployment Steps

1. Create Heroku app  
2. Connect GitHub repository  
3. Configure environment variables  
4. Set up PostgreSQL  
5. Run migrations  
6. Collect static files  
7. Deploy application  

### Environment Variables

- SECRET_KEY  
- DATABASE_URL  
- STRIPE_PUBLIC_KEY  
- STRIPE_SECRET_KEY  
- STRIPE_WH_SECRET  
- EMAIL_HOST_USER  
- EMAIL_HOST_PASS  

Sensitive values are stored securely and are not committed to GitHub.

### Production Settings

- DEBUG disabled  
- Allowed hosts configured  
- WhiteNoise for static files  
- PostgreSQL database  

---

## Security

- Environment variables for secrets  
- Hashed passwords  
- HTTPS enforced  
- Stripe secure payments  
- DEBUG disabled in production  

## Design and Visual Identity

The visual design focuses on a clean and modern aesthetic.

Design choices:

- Soft pastel colours (pink and purple tones)
- Minimalist layout
- Clear typography
- High contrast for accessibility
- Consistent branding across pages

Bootstrap 4.6 was used as the base framework and customised to match the brand identity.

---

## Product Categories and Variations

Products are organised into clearly defined categories:

- Figures & Models
- Decor & Home
- Accessories
- Merch
- Special Offers

Merchandise products support size variations such as:

- Small (S)
- Medium (M)
- Large (L)
- Extra Large (XL)

Size selection is available on supported products and is validated during checkout.

---

## Future Improvements

Planned future features include:

- Expanded product catalogue
- Additional merchandise designs
- More size options
- Stock management system
- Improved marketing tools
- Enhanced admin analytics
- Newsletter integration

These features will be considered for future development.

---

## Known Issues

- Footer and store location section are not visible in the current deployed version.  
- This is a minor UI issue and does not affect core functionality.  

---

## Bugs Fixed

- Profile menu duplication  
- Delivery calculation errors  
- Admin field validation issues  
- Responsive layout inconsistencies  


## Development Note

Shortly before submission, the project experienced a database and deployment issue
which required multiple rollbacks and data restoration.

Due to this technical incident, full documentation screenshots could not be recreated in time.
Priority was given to restoring core functionality and data integrity.

All application features, validation, and testing procedures were completed during development
according to course requirements.

All manual tests, validators, and deployment checks were performed and confirmed to be working correctly.

---

## Credits

- Django Documentation  
- Stripe Documentation  
- Code Institute course materials  
- Online developer communities  
- Family, friends, and mentor support  

Project created by Amanda Alexandra (2026)

