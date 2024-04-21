// JavaScript code for the dashboard

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission
    const passengerName = document.getElementById('passenger-name').value;
    searchBooking(passengerName); // Call function to search booking details
}

// Function to search booking details by passenger name
function searchBooking(passengerName) {
    // Perform AJAX request to search for booking details
    // Replace this with your actual backend endpoint
    // For demonstration purposes, let's just log the search query
    console.log(`Searching booking details for passenger: ${passengerName}`);
    // Update the output section with the search results
    const outputDiv = document.querySelector('.output');
    outputDiv.innerHTML = `<p>Searching booking details for passenger: ${passengerName}</p>`;
}

// Add event listener to the form for form submission
const searchForm = document.getElementById('search-form');
searchForm.addEventListener('submit', handleFormSubmit);
