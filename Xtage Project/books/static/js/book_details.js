// document.addEventListener("DOMContentLoaded", function() {
//     var hearts = document.querySelectorAll(".heart");
    
//     hearts.forEach(function(heart) {
//         heart.addEventListener("click", function() {
//             this.classList.toggle("is-active");
//         });
//     });
// });



document.addEventListener('DOMContentLoaded', function() {
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    const bookmarkIcon = bookmarkBtn.querySelector('i');
  
    bookmarkBtn.addEventListener('click', function() {
      bookmarkBtn.classList.toggle('active');
      
      if (bookmarkBtn.classList.contains('active')) {
        bookmarkIcon.classList.remove('bi-bookmark');
        bookmarkIcon.classList.add('bi-bookmark-fill');
      } else {
        bookmarkIcon.classList.remove('bi-bookmark-fill');
        bookmarkIcon.classList.add('bi-bookmark');
      }
  
      bookmarkIcon.classList.add('bookmark-pop');
      setTimeout(() => {
        bookmarkIcon.classList.remove('bookmark-pop');
      }, 300);
    });
  });


  document.addEventListener("DOMContentLoaded", function() {
    const hearts = document.querySelectorAll(".heart");
    const likeCount = document.querySelector('.like-count');

    hearts.forEach(function(heart) {
        heart.addEventListener("click", function() {
            const bookId = document.getElementById("div-book-ID").innerText;
            fetch(`/collection/like/${bookId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    heart.classList.add("is-active");
                } else {
                    heart.classList.remove("is-active");
                }
                likeCount.textContent = `${data.likes_count} likes`;
            });
        });
    });

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
});


document.addEventListener('DOMContentLoaded', function() {
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    const bookmarkIcon = bookmarkBtn.querySelector('i');
    const bookmarkText = bookmarkBtn.querySelector('span');

    bookmarkBtn.addEventListener('click', function() {
        const bookId = document.getElementById("div-book-ID").innerText;  // Make sure this element exists and contains the book ID
        fetch(`/collection/save/${bookId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.saved) {
                bookmarkBtn.classList.add('active');
                bookmarkIcon.classList.remove('bi-bookmark');
                bookmarkIcon.classList.add('bi-bookmark-fill');
                bookmarkText.textContent = 'Saved!';
            } else {
                bookmarkBtn.classList.remove('active');
                bookmarkIcon.classList.remove('bi-bookmark-fill');
                bookmarkIcon.classList.add('bi-bookmark');
                bookmarkText.textContent = 'Save Book';
            }
        });
    });

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
});


  document.addEventListener('DOMContentLoaded', function () {
    const likeBtn = document.querySelector('.heart');
    const likeCount = document.querySelector('.like-count');
    const commentBtn = document.getElementById('commentBtn');
    const commentText = document.getElementById('floatingTextarea2');
    const commentSection = document.querySelector('.comments-section');
    const saveBtn = document.getElementById('bookmarkBtn');

    // if (likeBtn) {
    //     likeBtn.addEventListener('click', function () {
    //         const bookId = document.getElementById("div-book-ID").innerText;
    //         fetch(`/collection/like/${bookId}/`, {
    //             method: 'POST',
    //             headers: {
    //                 'X-CSRFToken': getCookie('csrftoken')
    //             }
    //         })
    //             .then(response => response.json())
    //             .then(data => {
    //                 if (data.liked) {
    //                     likeBtn.classList.add('liked');
    //                 } else {
    //                     likeBtn.classList.remove('liked');
    //                 }
    //                 likeCount.textContent = `${data.likes_count} likes`;
    //             });
    //     });
    // }

    if (commentBtn) {
        commentBtn.addEventListener('click', function () {
            const bookId = document.getElementById("div-book-ID").innerText;
            fetch(`/collection/comment/${bookId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: `text=${encodeURIComponent(commentText.value)}`
            })
                .then(response => response.json())
                .then(data => {
                    if (data.comment) {
                        const comment = document.createElement('div');
                        comment.classList.add('comment');
                        comment.innerHTML = `
                            <p class="comment-text">${data.comment.text}</p>
                            <span class="comment-timestamp">Posted on: ${data.comment.timestamp} by ${data.comment.user}</span>
                        `;
                        commentSection.appendChild(comment);
                        commentText.value = '';
                    } else {
                        alert(data.error);
                    }
                });
        });
    }

    // if (saveBtn) {
    //     saveBtn.addEventListener('click', function () {
    //         const bookId = document.getElementById("div-book-ID").innerText;
    //         fetch(`/collection/save/${bookId}/`, {
    //             method: 'POST',
    //             headers: {
    //                 'X-CSRFToken': getCookie('csrftoken')
    //             }
    //         })
    //             .then(response => response.json())
    //             .then(data => {
    //                 if (data.saved) {
    //                     saveBtn.classList.add('saved');
    //                 } else {
    //                     saveBtn.classList.remove('saved');
    //                 }
    //             });
    //     });
    // }

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
});
