<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);


include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['gov-username'];
    $security_token = $_POST['gov-security_token'];

    // Prepare and execute the SQL query
    $sql = "SELECT * FROM government_users WHERE username=? AND security_token=?";
    $stmt = $conn->prepare($sql);

    if (!$stmt) {
        echo "Error preparing statement: " . $conn->error;
        exit();
    }

    $stmt->bind_param("ss", $username, $security_token);

    if (!$stmt->execute()) {
        echo "Error executing statement: " . $stmt->error;
        exit();
    }

    $result = $stmt->get_result();

    // Check if any rows are returned
    if ($result->num_rows > 0) {
        // If login succeeds, redirect to dashboard.php
        header("Location: adminpanel.html");
        exit();
    } else {
        // If login fails, redirect back to the login page with an error message
        header("Location: login.php?error=invalid_credentials");
        exit();
    }

    $stmt->close();
}
?>
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
            text-align: center;
            margin-top: 10px;
            display: flex;
            align-items: center;
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
        }

        header img {
            width: 70px;
            height: auto;
            border-radius: 50%;
            animation: dropletAnimation 2s ease forwards;
        }

        header h1 {
            font-size: 1.5em;
            font-weight: bold;
            margin-left: 10px;
            color: #007ACC;
            text-transform: uppercase;
            position: justify;
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

<main>
    <section class="login-section" id="gov-login">
        <h2>Government Login</h2>
        <form id="govLoginForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post"> <!-- Point to the PHP file that handles login validation -->
            <label for="gov-username"></label>
            <input type="text" id="gov-username" placeholder="Login id" name="gov-username" required aria-label="Username">
            <br>
            <label for="gov-token"></label>
            <input type="text" id="gov-security_token" placeholder="Security token" name="gov-security_token" required aria-label="Security Token">
            <br>
            <button type="submit" name="gov-login">Login</button>
        </form>
        <p><a href="login.php">Back to Public Login</a></p>
    </section>
</main>
<script>
    $(document).ready(function() {
        $('#govLoginForm').submit(function(event) {
            event.preventDefault(); // Prevent default form submission

            var username = $('#gov-username').val();
            var token = $('#gov-security_token').val();

            $.ajax({
                type: 'POST',
                url: '<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>',
                data: {
                    'gov-username': username,
                    'gov-security_token': token
                },
                success: function(response) {
                    if (response.trim() === 'success') {
                        alert('Login successful!');
                        window.location.href = 'adminpanel.html'; 
                    } else {
                        alert(response); 
                    }
                },
                error: function(xhr, status, error) {
                    alert('An error occurred: ' + error); 
                }
            });
        });
    });
</script>
</body>
</html>