window.onload = function () {
  var myModal;

  let savings = document.getElementById("savingsbtn");
  savings.addEventListener("click", function () {
    myModal = new bootstrap.Modal("#modal-s");
    myModal.show();
  });
  let wants = document.getElementById("wantBtn");
  wants.addEventListener("click", function () {
    myModal = new bootstrap.Modal("#modal-w");
    myModal.show();
  });
  let necessities = document.getElementById("necessitiesbtn");
  necessities.addEventListener("click", function () {
    myModal = new bootstrap.Modal("#modal-n");
    myModal.show();
  });
  let budget = document.getElementById("budgetbtn");
  budget.addEventListener("click", function () {
    myModal = new bootstrap.Modal("#modal-b");
    myModal.show();
  });
  let custom = document.getElementById("custom");
  custom.addEventListener("change", function () {
    if (custom.value == 3) {
      myModal.hide();
      myModal = new bootstrap.Modal("#modal-custom");
      myModal.show();
    }
  });
  let submitw = document.getElementById("submit-w");
  let submitn = document.getElementById("submit-n");
  let submits = document.getElementById("submit-s");

  submitw.addEventListener("click", function (event) {
    event.preventDefault();
    let type = "wants";
    let vars = {};

    vars["0"] = document.getElementById("vacation").value;
    vars["1"] = document.getElementById("clothing").value;
    vars["2"] = document.getElementById("other2").value;

    fetch(`${window.origin}/dashboard`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({
        vars: vars,
        type: type,
        location: "specifics",
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
      response.json().then(function (data) {
        let vars = data["vars"];
        let type = data["type"];

        let vacation = document.getElementById("vacation-display");
        vacation.innerHTML = "Vacation: $" + vars[0];
        let clothing = document.getElementById("clothing-display");
        clothing.innerHTML = "Clothing: $" + vars[1];
        let other = document.getElementById("other2-display");
        other.innerHTML = "Other: $" + vars[2];
      });
    });
    myModal.hide();
  });
  submits.addEventListener("click", function (event) {
    event.preventDefault();
    let type = "savings";
    let vars = {};

    vars["0"] = document.getElementById("emergency").value;
    vars["1"] = document.getElementById("retirement").value;
    vars["2"] = document.getElementById("debts").value;
    fetch(`${window.origin}/dashboard`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({
        vars: vars,
        type: type,
        location: "specifics",
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
      response.json().then(function (data) {
        let vars = data["vars"];
        let type = data["type"];

        let emergency = document.getElementById("emergency-display");
        emergency.innerHTML = "Emergency Funds: $" + vars[0];
        let retirement = document.getElementById("retirement-display");
        retirement.innerHTML = "Retirement: $" + vars[1];
        let debt = document.getElementById("debt-display");
        debt.innerHTML = "Debts: $" + vars[2];
      });
    });
    myModal.hide();
  });
  submitn.addEventListener("click", function (event) {
    event.preventDefault();
    let type = "necessities";
    let vars = {};
    vars["0"] = document.getElementById("rent").value;
    vars["1"] = document.getElementById("groceries").value;
    vars["2"] = document.getElementById("other").value;
    fetch(`${window.origin}/dashboard`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({
        vars: vars,
        type: type,
        location: "specifics",
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
      response.json().then(function (data) {
        let v = document.getElementsByClassName("");
        let vars = data["vars"];
        let type = data["type"];
        let rent = document.getElementById("rent-display");
        rent.innerHTML = "Rent: $" + vars[0];
        let groceries = document.getElementById("groceries-display");
        groceries.innerHTML = "Groceries: $" + vars[1];
        let other = document.getElementById("other-display");
        other.innerHTML = "Other: $" + vars[2];
      });
    });
    myModal.hide();
  });

  let budgetBtn = document.getElementById("submit-b");
  let customModal = new bootstrap.Modal(
    document.getElementById("modal-custom")
  );

  budgetBtn.addEventListener("click", function (event) {
    event.preventDefault();
    let plan = document.getElementById("custom");

    if (plan.value === "third") {
      // Show the custom modal when "Custom" is selected
      customModal.show();
    } else {
      // Handle default plans
      fetch(`${window.origin}/budget`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({
          type: plan.value,
        }),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json",
        }),
      })
        .then(function (response) {
          if (response.status !== 200) {
            console.log("Failure");
            return;
          }
          return response.json(); // Return the response to the next `.then`
        })
        .then(function (data) {
          let budgetPlan = data.budgetPlan;
          let ndisplay = document.getElementById("necessities-display");
          let sdisplay = document.getElementById("savings-display");
          let wdisplay = document.getElementById("wants-display");
          ndisplay.innerHTML = "Necessities: $" + parseFloat(budgetPlan["necessities"]).toFixed(2);
          sdisplay.innerHTML = "Savings: $" + parseFloat(budgetPlan["savings"]).toFixed(2);
          wdisplay.innerHTML = "Wants: $" + parseFloat(budgetPlan["wants"]).toFixed(2);
        });
    }
  });

  // Handle submission in custom modal
  document
    .getElementById("submit-c")
    .addEventListener("click", function (event) {
      event.preventDefault();

      let necessities = document.getElementById("necessities");
      let savings = document.getElementById("savings");
      let wants = document.getElementById("wants");

      // Send custom data when submitting
      fetch(`${window.origin}/budget`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({
          type: 3,
          wants: parseFloat(wants.value) / 100, // Convert to decimal
          necessities: parseFloat(necessities.value) / 100,
          savings: parseFloat(savings.value) / 100,
        }),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json",
        }),
      })
        .then(function (response) {
          if (response.status !== 200) {
            console.log("Failure");
            return;
          }
          return response.json(); // Return the response to the next `.then`
        })
        .then(function (data) {
          let budgetPlan = data.budgetPlan;
          let ndisplay = document.getElementById("necessities-display");
          let sdisplay = document.getElementById("savings-display");
          let wdisplay = document.getElementById("wants-display");
          ndisplay.innerHTML = "Necessities: $" + parseFloat(budgetPlan["necessities"]).toFixed(2);
          sdisplay.innerHTML = "Savings: $" + parseFloat(budgetPlan["savings"]).toFixed(2);
          wdisplay.innerHTML = "Wants: $" + parseFloat(budgetPlan["wants"]).toFixed(2);
          customModal.hide(); // Hide the custom modal after submission
        });
    });
};
