<?php
// Include the database configuration file
include 'config.php';

// Initialize variables to store form data
$name = $mobile = $state = $district = $address = $essentials = $extra_needs = '';
$other_essentials = []; // Initialize as array for multiple other essentials

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    function sanitize_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    // Retrieve and sanitize form data
    $name = isset($_POST["name"]) ? sanitize_input($_POST["name"]) : '';
    $mobile = isset($_POST["mobile"]) ? sanitize_input($_POST["mobile"]) : '';
    $state = isset($_POST["state"]) ? sanitize_input($_POST["state"]) : '';
    $district = isset($_POST["district"]) ? sanitize_input($_POST["district"]) : '';
    $address = isset($_POST["address"]) ? sanitize_input($_POST["address"]) : '';
    $essentials = isset($_POST["essentials"]) ? $_POST["essentials"] : [];
    $extra_needs = isset($_POST["extraNeeds"]) ? sanitize_input($_POST["extraNeeds"]) : '';

    // Check if otherEssentials is set and not empty
    if (isset($_POST["otherEssentials"]) && !empty($_POST["otherEssentials"])) {
        $other_essentials = sanitize_input($_POST["otherEssentials"]);
        // Add other essentials to essentials array
        $essentials[] = $other_essentials;
    }

    // Convert essentials array to comma-separated string
    $essentials_str = implode(', ', $essentials);

    // Prepare SQL insert statement using prepared statements
    $sql = "INSERT INTO needs (name, mobile, state, district, address, essentials, extra_needs) 
            VALUES (?, ?, ?, ?, ?, ?, ?)";

    // Prepare and bind parameters
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("sssssss", $name, $mobile, $state, $district, $address, $essentials_str, $extra_needs);

        // Execute the statement
        if ($stmt->execute()) {
            echo "success";
        } else {
            echo "Error: " . $stmt->error;
        }

        // Close statement
        $stmt->close();
    } else {
        echo "Error: " . $conn->error;
    }

    // Close connection
    $conn->close();
} else {
    echo "Invalid request.";
}
?>