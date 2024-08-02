window.onload = function () {
  console.log("First check passed");
  let savings = document.getElementById("loginbtn");
  savings.addEventListener("click", function () {
    const myModal = new bootstrap.Modal("#modal-log");
    myModal.show();
  });
};
