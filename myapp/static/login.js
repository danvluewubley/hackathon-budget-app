window.onload = function () {
  let myModal;
  let login = document.getElementById("loginbtn");
  login.addEventListener("click", function () {
    myModal = new bootstrap.Modal("#modal-log");
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
        // "X-CSRF-Token": csrf_token,
      }),
    })
      .then(function (response) {
        if (response.ok) {
          // If login is successful, redirect to the dashboard
          myModal.hide();
          window.location.href = "/dashboard"; // Change this to your actual dashboard URL
        } else {
          response.json().then(function (data) {
            console.log(data.message); // Handle error message
            // You might want to display this message in the modal
          });
        }
      })
      .catch(function (error) {
        console.error("Error:", error); // Handle network error
      });
  });
};
