<?php
// Include the database configuration file
include 'config.php';

// Check if ID parameter is received via POST
if (isset($_POST['id'])) {
    // Sanitize the ID to prevent SQL injection
    $id = mysqli_real_escape_string($conn, $_POST['id']);

    // SQL query to delete record with the given ID
    $sql = "DELETE FROM needs WHERE id = '$id'";

    // Attempt to execute the query
    if ($conn->query($sql) === TRUE) {
        // Return a success message or status code
        http_response_code(200); // Success
        echo "Record deleted successfully";
    } else {
        // Return an error message or status code
        http_response_code(500); // Internal Server Error
        echo "Error: " . $conn->error;
    }
} else {
    // Return an error response if ID parameter is missing
    http_response_code(400); // Bad Request
    echo "ID parameter is missing";
}

// Close database connection
$conn->close();
?>