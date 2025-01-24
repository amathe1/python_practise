

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Suraksha Setu</title>
     <link rel="icon" type="image/png" href="croppedimage.png">
    <style>
   body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #f1f1f1;
            background-image: linear-gradient(135deg, #ffffff 25%, #007ACC 75%);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            padding: 10px;
        }

        header {
    display: flex;
    align-items: center;
    position: absolute;
    top: 15px;
    left: 15px;
}

header img {
    width: 70px;
    height: auto;
    border-radius: 50%;
    animation: dropletAnimation 2s ease forwards;
}

header h1 {
    font-size: 1.8em;
    font-weight: bold;
    margin-left: 0px;
    padding-top: 30px;  /* Adjust this value to move the text down */
    color: #007ACC;
    text-transform: uppercase;
    white-space: nowrap;
}


        .login-section {
            width: 100%;
            max-width: 350px;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 122, 204, 0.2);
            box-shadow: 0 4px 30px rgba(0, 122, 204, 0.2);
            border-radius: 20px;
            text-align: center;
            animation: dropletAnimation 2s ease forwards;
            box-sizing: border-box;
        }

        .login-section h2 {
            color: #007ACC;
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 15px;
            text-transform: uppercase;
        }

        .login-section label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
            color: #333;
            text-align: left;
        }

        .login-section input[type="text"],
        .login-section input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 2px solid #B0C4DE;
            border-radius: 20px;
            font-size: 1rem;
            color: #333;
            box-sizing: border-box;
            transition: border-color 0.3s ease, background-color 0.3s ease;
        }

        .login-section input[type="text"]:focus,
        .login-section input[type="password"]:focus {
            border-color: #007ACC;
            background-color: rgba(0, 122, 204, 0.1);
        }

        .login-section button[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #007ACC;
            color: #fff;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
            text-transform: uppercase;
            border: none;
            border-radius: 20px;
            transition: background-color 0.3s ease-in-out, transform 0.3s ease;
        }

        .login-section button[type="submit"]:hover {
            background-color: #005fa3;
            transform: translateY(-2px);
        }

        .login-section p {
            margin-top: 15px;
            font-size: 0.9rem;
            color: #333;
        }

        .login-section a {
            color: #007ACC;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .login-section a:hover {
            color: #005fa3;
            text-decoration: underline;
        }

        @keyframes dropletAnimation {
            0% {
                transform: scale(0);
                opacity: 0;
            }
            50% {
                transform: scale(1.2);
                opacity: 1;
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }

    </style>
</head>
<body>

<header>
<img src="mainimage.png" alt="App Logo">
    <h1>Suraksha Setu</h1>
</header>

<div class="login-section">
    <h2>Create Account</h2>
    <form id="create-account-form" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <div class="input-group">
            <label for="create-username"></label>
            <input type="text" id="create-username" placeholder="Phone number, username or email address" name="create-username">
        </div>
        <div class="input-group">
            <label for="create-password"></label>
            <input type="password" id="create-password" placeholder="Password" name="create-password">
        </div>
        <div class="input-group">
            <label for="confirm-password"></label>
            <input type="password" id="confirm-password" placeholder="Confirm password" name="confirm-password">
        </div>
        <div class="button-group">
            <button type="submit" id="create-account-btn" name="create-account">Create Account</button>
        </div>
        <p><a href="login.php">Back to login!</a></p>
    </form>
</div>

<script>
    document.getElementById("create-account-form").addEventListener("submit", function(event) {
        // Get form data
        var username = document.getElementById("create-username").value;
        var password = document.getElementById("create-password").value;
        var confirmPassword = document.getElementById("confirm-password").value;

        // Validate form data
        if (username.trim() === "" || password.trim() === "" || confirmPassword.trim() === "") {
            alert("Please enter username and password.");
            event.preventDefault(); // Prevent form submission
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            event.preventDefault(); // Prevent form submission
            return;
        }
    });
</script>

</body>
</html>