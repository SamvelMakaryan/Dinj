const submitButton = document.getElementById('submit-button');
const email = document.getElementById('email');
const password = document.getElementById('password');

submitButton.addEventListener('click', () => {
  const data = {
    email: email.value,
    password: password.value,
  };
  fetch('http://localhost:5000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(responseData => {
    // Check the response data to determine if registration was successful
    if (responseData.success) {
      // Registration was successful
      alert('Registration successful!');
      // Redirect to a different page
      window.location.href = 'main-page.html'; // Change to the desired URL
    } else {					
      // Registration failed, handle the error
      alert('Registration failed: ' + responseData.error);
    }
  })
  .catch(error => {
    // Handle network errors or other exceptions here
    console.error('Error:', error);
  });
});
