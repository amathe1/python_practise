<?php
// Enable error reporting and display errors (for debugging purposes)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define the path to the error log file
$errorLogFilePath = 'error.log';

// Custom function to log errors
function logError($message) {
    global $errorLogFilePath;
    error_log($message . PHP_EOL, 3, $errorLogFilePath);
}

// Example usage:
try {
    // Your code that might throw an error
    $result = 1 / 0; // Example division by zero to trigger an error
} catch (Exception $e) {
    // Catch any exceptions and log the error
    logError('Caught exception: ' . $e->getMessage());
}

// Example error log message
logError('This is a custom error log message.');

// Example logging for debugging
$logMessage = 'Debugging information: ' . var_export($_POST, true); // Log POST data
logError($logMessage);

// Example logging an error message if login fails
if ($loginFailed) {
    logError('Login attempt failed: Invalid username or password.');
}
?>