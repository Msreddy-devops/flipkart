<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dummy Flipkart Homepage</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f1f3f6;
    }
    header {
      background: #2874f0;
      color: white;
      padding: 15px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    header h1 {
      margin: 0;
      font-size: 24px;
    }
    nav a {
      color: white;
      margin: 0 15px;
      text-decoration: none;
      font-weight: bold;
    }
    .categories {
      display: flex;
      justify-content: space-around;
      margin: 20px;
    }
    .category {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      width: 30%;
      text-align: center;
    }
    .category img {
      width: 100px;
      height: 100px;
    }
    .category h2 {
      margin: 15px 0 10px;
    }
    .footer {
      background: #172337;
      color: white;
      text-align: center;
      padding: 15px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Flipkart</h1>
    <nav>
      <a href="#clothing">Clothing</a>
      <a href="#mobiles">Mobiles</a>
      <a href="#grocery">Grocery</a>
    </nav>
  </header>

  <section class="categories">
    <div class="category" id="clothing">
      <img src="https://cdn-icons-png.flaticon.com/512/892/892458.png" alt="Clothing">
      <h2>Clothing</h2>
      <p>Trendy and stylish outfits for men, women, and kids.</p>
    </div>
    <div class="category" id="mobiles">
      <img src="https://cdn-icons-png.flaticon.com/512/2948/2948035.png" alt="Mobiles">
      <h2>Mobiles</h2>
      <p>Latest smartphones with amazing deals.</p>
    </div>
    <div class="category" id="grocery">
      <img src="https://cdn-icons-png.flaticon.com/512/3081/3081559.png" alt="Grocery">
      <h2>Grocery</h2>
      <p>Fresh and quality groceries at your doorstep.</p>
    </div>
  </section>

  <div class="footer">
    <p>&copy; 2025 Dummy Flipkart Homepage | All Rights Reserved</p>
  </div>
</body>
</html>
