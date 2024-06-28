function sendBookId(bookID) {
    // Get the book ID from the argument
    const bookId = bookID;
    
    // Create the request URL
    const url = '/api/by_id';

    // Create the fetch request
    fetch(url, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ bookId: bookId }) // Send the bookId in JSON format
    })
    .then(response => {
        if (response.ok) {
            // Redirect to the book details page if the request is successful
            window.location.href = '/book_details/' + bookId;
        } else {
            // Handle errors or unsuccessful responses
            console.error('Failed to fetch details for book ID:', bookId);
            alert('Failed to fetch book details.');
        }
    })
    .catch(error => {
        // Handle network errors
        console.error('Network error:', error);
        alert('Network error occurred. Please try again.');
    });
}
