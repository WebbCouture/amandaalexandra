# AmandaAlexandra – 3D Print Shop

## Project Overview

AmandaAlexandra is an e-commerce platform for selling custom 3D printed products.
The website allows users to browse products, create accounts, and securely
purchase items online using Stripe.

The target audience is individuals interested in unique, aesthetic, and custom
3D printed accessories and decorations.

The platform is designed to support small-scale digital manufacturing and
provide customers with personalized products.

---

## User Goals

- Easily browse and purchase 3D printed products
- View clear product images and descriptions
- Complete secure online payments
- Access order history through a personal account
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
- As a shopper, I want to search and filter products so that I can find products easily.
- As a shopper, I want to view product details so that I can make informed decisions.

### Account Management
- As a user, I want to register and log in so that I can access my profile.
- As a user, I want to view my order history so that I can track my purchases.
- As a user, I want to reset my password if I forget it.

### Purchasing
- As a shopper, I want to add items to my cart so that I can purchase multiple products.
- As a shopper, I want to securely pay for my order using Stripe.
- As a shopper, I want to checkout as a guest so that I can purchase without creating an account.

### Administration
- As a site owner, I want to add, edit, and delete products so that I can manage my store.
- As a site owner, I want to view customer orders.

---

## User Experience (UX)

### Strategy Plane
The website is designed for users who want to purchase stylish and custom 3D printed
products online. The main goal is to provide a simple, secure, and visually appealing
shopping experience.

Accessibility and ease of use were considered to ensure the website can be used by a wide audience.

### Scope Plane
The main features include:
- User authentication system
- Product listings and categories
- Shopping cart functionality
- Stripe payment integration
- User profiles and order history
- Admin product management
- Responsive design

### Structure Plane
The website is structured using a clear navigation system:
- Home
- Shop
- Product Detail
- Cart / Checkout
- Profile
- Contact

This structure ensures users can easily find what they need.

### Skeleton Plane
Wireframes were created for mobile, tablet, and desktop views to plan the layout and
responsiveness of the website before development.

These wireframes guided the placement of navigation, product grids, and buttons.

### Surface Plane
The visual design uses a ÄNDRA SEN FÄRG HÄR? soft pink and purple color scheme to reflect the
AmandaAlexandra brand identity. The layout is clean and modern, with clear buttons
and readable typography.

---
## Design and Visual Customisation

The website design was inspired by the course material but has been customised to reflect the AmandaAlexandra brand identity.

A custom Google Font (Inter) was implemented instead of the default course font to create a more modern and minimal aesthetic.

The homepage layout and header structure were adapted to improve usability and readability across different screen sizes.

Media queries were used to ensure that the layout remains responsive on mobile, tablet, and desktop devices.

Special attention was given to spacing, typography, and button styling to create a clean and professional shopping experience.


## Wireframes

### Home Page (Mobile, Tablet, Desktop)
![Home Wireframe](docs/readme-img/wireframes/home_responsive.png)



### Shop Page (Mobile, Tablet, Desktop)
![Shop Wireframe](docs/readme-img/wireframes/shop_responsive.png)



### Product Page (Mobile, Tablet, Desktop)
![Product Wireframe](docs/readme-img/wireframes/product_responsive.png)



### Cart, Checkout & Profile Pages (Mobile, Tablet, Desktop)
![Other Pages Wireframe](docs/readme-img/wireframes/other_pages_responsive.png)


---

## Features

- User registration and login system
- Product browsing and filtering
- Shopping cart
- Secure Stripe checkout
- User profile with order history
- Admin dashboard for managing products
- Responsive layout
- Custom 3D printing product catalogue created specifically for this project
- Manually curated categories and products (not default course data)
- Product data managed via Django admin and fixtures

---

## Data Model

The main database models include:

- User (Django default user model)
- Product
- Category
- Order
- OrderItem
- UserProfile

Relationships are designed to ensure data integrity and efficient querying.

---

## Technologies Used

- HTML, CSS, JavaScript
- Python, Django
- Stripe
- PostgreSQL
- GitHub
- Heroku

---

## Testing

Manual testing was conducted throughout development to ensure:

- Navigation links function correctly
- Forms validate input properly
- Checkout process works as expected
- Responsive design works on multiple screen sizes
- Cross-browser compatibility

Validation tools and Lighthouse audits were used to improve performance and accessibility.

All major bugs encountered during development are documented and resolved.

---
## Local Setup (Development)

To run the project locally:

## Clone the repository

```bash
git clone https://github.com/AmandaAlexandraStudio/3DPrints.git
cd 3DPrints
python -m venv .venv

# Mac / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```


## Deployment

The project is deployed using Heroku.

### Local Deployment

1. Clone the repository (see "Local Setup" section above)
2. Create a virtual environment
3. Install dependencies
4. Run migrations
5. Start the development server

### Heroku Deployment

1. Create a Heroku application
2. Configure environment variables
3. Connect GitHub repository
4. Deploy the main branch
5. Set up PostgreSQL database
```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic
```



---

## Security

- Sensitive keys are stored in environment variables
- Django DEBUG mode is disabled in production
- User passwords are securely hashed
- Payment processing is handled securely via Stripe

---

## Credits

- Django Documentation
- Stripe Documentation
- Code Institute learning materials
- Wireframes created by AmandaAlexandra
- All product images and content created or licensed by the site owner
