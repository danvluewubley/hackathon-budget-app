window.onload = function () {
  console.log("First check passed");
  let login = document.getElementById("loginbtn");
  login.addEventListener("click", function () {
    const myModal = new bootstrap.Modal("#modal-log");
    myModal.show();
  });
  

  let loginBtn = document.getElementById("submitBtn");
  loginBtn.addEventListener("click", function () {
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;
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
        //"X-CSRF-Token": csrf_token,
      }),
    }).then(function (response) {
      if (response.status !== 200) {
        console.log("Failure");
        return;
      }
      response.json().then(function (data) {});
    });
  });
};
