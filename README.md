# Django_Ecommerce_Website
  
### Features and Updates:  
- Added "On sale" feature for the product. If product "on sale", we can see red badge "Sale" on the picture and crossed out old price with a big red new price.
- Added 'Buy it Now' button  
- Created "List Orders" and "Order Details" pages. After successful payment you can go to your Account and view your list of orders  
- Implemented creation Order(new database elements) and deleting Shopping-Cart elements(from database) after payment
- Implemented PayPal Payments for order
- Finished "Checkout page"  
- Implemented a User Profile(One-to-One Relationships). Additionally to info from build-in User module added to User Profile(inherit from built-in User module) address fields and phone field. Added fields to UpdateUser Page. Implemented  feature "pre-filled fields" to fields on WebPage "UpdateUser" if there are some info in database.  
- Added the ability to view pictures from the "Product Description" in full size (full screen). Also we can close picture by clicking on it.  
- Added the ability to change the quantity in product details and directly in the cart
- Added pagination. On a full page - max 20 products
- Implemented Product Search System 
- Registration and Login system
- Implemented multi-categories system. We can add as many categories as we want and system will add it to Categories section (in nav bar) automatically  
- Implemented Cart system. Each user have a different cart. Information is saved in a database
  
## How it looks like now  
  
### Home page (Added "On sale" feature)  
  
![home](./!resources/media/home2.png)  
  
### Other products (also implemented paginator)  
  
![home](./!resources/media/other_products.png)  
  
### Sort products (Implemented search system)  
  
![home](./!resources/media/search.png)  
  
### Sort by category(old Feature, implemented before implementing search system)  
  
![home](./!resources/media/sort_by_category.png)  
  
  ### Product details
  
![home](./!resources/media/product_details.png)  
  
### View the picture in fill size  
  
![home](./!resources/media/view_pic.png)    
  
### Shopping Cart(for every user different shipping cart)  
  
![home](./!resources/media/cart.png)    
  
### Checkout Page (part 1)
  
![home](./!resources/media/checkout1.png)   
  
### Checkout Page (part 2)
  
![home](./!resources/media/checkout2.png)   
  
### Checkout Page (part 3)
  
![home](./!resources/media/payments.png)   
  
### After clicking button "Pay with PayPal"
  
![home](./!resources/media/paypal.png)   
  
### After Login in PayPal (implemented paypal sandbox - dummy payments)
  
![home](./!resources/media/pay_on_paypal.png)   
  
### "Order completed" page after successful payment
  
![home](./!resources/media/order_completed.png)   
  
### Click "View Order Details"
  
![home](./!resources/media/order_details.png)   
  
### Click "View List Orders" (also we have access to this page if click right top to "Hello, {name}" and select "View List Orders")  
  
![home](./!resources/media/list_orders.png)   
  
## Login System
    
### Sign Up  
  
![home](./!resources/media/sign_up.png)  
  
### Sign In  
  
![home](./!resources/media/log_in.png)  
  
  ### Logged in
  
![home](./!resources/media/logged_in.png)  
  
### Update profile  
(Implemented a user profile inherited from the built-in user module)  
  
![home](./!resources/media/update.png)    
  
  

### Project is still in progress (the basic part has been built. 90% done)    
  
Template from - https://startbootstrap.com/template/shop-homepage  
