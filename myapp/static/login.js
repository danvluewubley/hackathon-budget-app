window.onload = function () {
  let myModal;
  console.log("First check passed");
  let login = document.getElementById("loginbtn");
  login.addEventListener("click", function () {
    myModal = new bootstrap.Modal(document.getElementById("modal-log"));
    myModal.show();
  });

  let loginBtn = document.getElementById("submitBtn");
  loginBtn.addEventListener("click", function () {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(`${window.origin}/login`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({
        email: email,
        password: password,
      }),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json",
      }),
    })
      .then(function (response) {
        response.json().then(function (data) {
          const flashMessageDiv = document.getElementById("flash-message");
          flashMessageDiv.innerHTML = ""; // Clear any previous messages
          if (data.success) {
            flashMessageDiv.innerHTML = `<div class="alert alert-success alert-dismissible fade show" role="alert">Login successful!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;
            flashMessageDiv.style.display = "block"; // Show the message
            myModal.hide();
            setTimeout(function () {
              window.location.href = "/dashboard"; // Redirect after successful login
            }, 1000);
          } else {
            flashMessageDiv.innerHTML = `<div class="alert alert-danger alert-dismissible fade show" role="alert">Please check your login details and try again.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;
            flashMessageDiv.style.display = "block"; // Show the message
          }
        });
      })
      .catch(function (error) {
        console.error("Error:", error); // Handle network error
      });
  });
};
