gsap.from(".nav-link", {
  opacity: 0,
  y: 50,
  duration: 1,
});

gsap.from(".banner-disp-txt", {
  opacity: 0,
  x: 50,
  duration: 1,
  onComplete: gsap.from(".banner-img", {
    y: 50,
    opacity: 0,
    duration: 1,
  }),
});





// Fetch Cookie value

// Function to get the CSRF token from the cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const searchValue = document.getElementById("searchBar").value;

function fetchWithPostRequest(searchValue) {
    const csrfToken = getCookie('csrftoken');
    fetch('/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ data: searchValue }),
        redirect: 'follow'
    })
    .then(response => {
        console.log('Response status:', response.status);
        console.log('Final URL:', response.url);
        if (response.redirected) {
            window.location.href = response.url;
        } else if (response.headers.get("content-type")?.includes("application/json")) {
            return response.json();
        } else {
            console.log('Unexpected response type:', response.headers.get("content-type"));
            return null;
        }
    })
    .then(data => {
        if (data) {
            console.log('Response data:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.getElementById("searchBtn").addEventListener("click", (e) => {
  e.preventDefault();
  const searchValue = document.getElementById("searchBar").value;

  fetchWithPostRequest(searchValue);
});