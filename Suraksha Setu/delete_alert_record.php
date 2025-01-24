<?php
include 'config.php'; // Include your database connection configuration

// Check if 'id' is set and is a valid integer
if (isset($_POST['id']) && filter_var($_POST['id'], FILTER_VALIDATE_INT)) {
    $id = $_POST['id'];

    // Prepare and execute delete query
    $sql = "DELETE FROM alert_history WHERE id = ?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("i", $id);

        if ($stmt->execute()) {
            echo "Alert record deleted successfully.";
        } else {
            echo "Error deleting alert record: " . htmlspecialchars($stmt->error);
        }

        $stmt->close();
    } else {
        echo "Error preparing statement: " . htmlspecialchars($conn->error);
    }
} else {
    echo "Invalid or missing ID.";
}

$conn->close();
?>
