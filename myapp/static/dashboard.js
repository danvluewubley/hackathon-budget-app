console.log("Is this file linked");


window.onload = function() {
  var myModal;
        console.log("First check passed")
        let savings = document.getElementById("savingsbtn");
        savings.addEventListener('click', function(){
            myModal = new bootstrap.Modal('#modal-s');
            myModal.show()
        })

        let wants = document.getElementById("wantBtn");
        wants.addEventListener('click', function() {
            myModal = new bootstrap.Modal('#modal-w');
            myModal.show()
        })

        let necessities = document.getElementById("necessitiesbtn");
        necessities.addEventListener('click', function() {
            myModal = new bootstrap.Modal('#modal-n');
            myModal.show()
        })

        let budget = document.getElementById("budgetbtn");
        budget.addEventListener("click", function () {
          myModal = new bootstrap.Modal("#modal-b");
          myModal.show();
        });

        let custom = document.getElementById("custom");
        custom.addEventListener("change", function () {
          if (custom.value == 3){
            myModal.hide();
            myModal = new bootstrap.Modal("#modal-custom");
            myModal.show();
          }
        });

        let submitw = document.getElementById("submit-w");
        let submitn = document.getElementById("submit-n")
        let submits = document.getElementById("submit-s")
        
        submitw.addEventListener('click', function(event){
            event.preventDefault()

            let type = document.getElementsByClassName("type").value;
            let vars = {};
            
            
            
            vars[0] = document.getElementById("vacation").value
            vars[1] = document.getElementById("clothing").value
            vars[2] = document.getElementById("other2").value
            
            fetch(`${window.origin}/dashboard`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify({
                    vars: vars,
                    type: type,
                    location: "specifics"
                }),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json",
                    //"X-CSRF-Token": csrf_token,
                })
            })
            .then(function(response) {
                if (response.status !== 200){
                    console.log("Failure")
                    return ;
                }
                response.json().then(function (data) {
                    let vars = data['vars']
                    let type = data['type']
                    
                    let vacation = document.getElementById("vacation-display");
                    vacation.innerHTML = vars[0]
                    let clothing = document.getElementById("clothing-display");
                    retirement.innerHTML = vars[1]
                    let other = document.getElementById("other2-display");
                    other.innerHTML = vars[2]
                    
                })
            })
        })
        submits.addEventListener('click', function(event){
          event.preventDefault()

          let type = document.getElementsByClassName("type").value;
          let vars = {};
          
          
  
          vars[0] = document.getElementById("emergency").value
          vars[1] = document.getElementById("retirement").value
          vars[2] = document.getElementById("debts").value


          fetch(`${window.origin}/dashboard`, {
              method: "POST",
              credentials: "include",
              body: JSON.stringify({
                  vars: vars,
                  type: type,
                  location: "specifics"
              }),
              cache: "no-cache",
              headers: new Headers({
                  "content-type": "application/json",
                  //"X-CSRF-Token": csrf_token,
              })
          })
          .then(function(response) {
              if (response.status !== 200){
                  console.log("Failure")
                  return ;
              }
              response.json().then(function (data) {
                  let vars = data['vars']
                  let type = data['type']
              
                  
                  let emergency = document.getElementById("emergency-display");
                  emergency.innerHTML = vars[0]
                  let retirement = document.getElementById("retirement-display");
                  retirement.innerHTML = vars[1]
                  let debt = document.getElementById("debt-display");
                  debt.innerHTML = vars[2]
              })
          })
      })
      submitn.addEventListener('click', function(event){
        event.preventDefault()

        let type = document.getElementsByClassName("type").value;
        let vars = {};
        vars[0] = document.getElementById("rent").value
        vars[1] = document.getElementById("groceries").value
        vars[2] = document.getElementById("other").value

        fetch(`${window.origin}/dashboard`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify({
                vars: vars,
                type: type,
                location: "specifics"
            }),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json",
                //"X-CSRF-Token": csrf_token,
            })
        })
        .then(function(response) {
            if (response.status !== 200){
                console.log("Failure")
                return ;
            }
            response.json().then(function (data) {
                let vars = data['vars']
                let type = data['type']
                let rent = document.getElementById("rent-display");
                rent.innerHTML = vars[0]
                let groceries = document.getElementById("groceries-display");
                groceries.innerHTML = vars[1]
                let other = document.getElementById("other-display");
                other.innerHTML = vars[2]
                
            })
        })
    })

      let budgetBtn = document.getElementById('submit-b');
      budgetBtn.addEventListener('click', function() {
        let plan = document.getElementById('budget-options');
        if (plan.value == 3) {
          let necessities = document.getElementById('necessities');
          let savings = document.getElementById('savings');
          let wants = document.getElementById('wants');
          
          fetch(`${window.origin}/budget`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify({
              type: 3,
              wants: wants/100,
              necessities: necessities/100,
              savings: savings/100,
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

        }
        else {
          fetch(`${window.origin}/budget`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify({
              type: plan.value,
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
              budgetPlan = data.budgetPlan
          });
        }
      })

        

    
}
