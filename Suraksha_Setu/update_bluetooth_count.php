<?php
include 'config.php';

// Check if POST request
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $newCount = intval($_POST['count']); // Retrieve count from POST request

    // Update the count in the database
    $sql = "UPDATE bluetooth_count SET count = ? WHERE id = 1";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $newCount);

    if ($stmt->execute()) {
        // Redirect to the update_count_form.html page after successful update
        header('Location: update_count_form.html');
        exit(); // Ensure no further code is executed
    } else {
        echo "Error updating count: " . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>
