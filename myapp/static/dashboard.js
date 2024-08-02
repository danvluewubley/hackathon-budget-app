console.log("Is this file linked");


window.onload = function() {
        console.log("First check passed")
        let savings = document.getElementById("savingsbtn");
        savings.addEventListener('click', function(){
            const myModal = new bootstrap.Modal('#modal-s');
            myModal.show()
        })

        let wants = document.getElementById("wantBtn");
        wants.addEventListener('click', function() {
            const myModal = new bootstrap.Modal('#modal-w');
            myModal.show()
        })

        let necessities = document.getElementById("necessitiesbtn");
        necessities.addEventListener('click', function() {
            console.log("Its working")
            const myModal = new bootstrap.Modal('#modal-n');
            myModal.show()
        })

        let budget = document.getElementById("budgetbtn");
        budget.addEventListener("click", function () {
          console.log("Its working");
          const myModal = new bootstrap.Modal("#modal-b");
          myModal.show();
        });

        let custom = document.getElementById("custom");
        custom.addEventListener("change", function () {
          if (custom.value == 3){
            const myModal = new bootstrap.Modal("#modal-custom");
            myModal.show();
          }
        });

        let submit = document.getElementsByClassName("submit");
        
        for (let i = 0; i < submit.length; i++)
        submit[i].addEventListener('click', function(event){
            event.preventDefault()

            let type = document.getElementsByClassName("type").value
            let vars = {};
            
            if (type == "necessities") {
                vars[0] = document.getElementById("rent").value
                vars[1] = document.getElementById("groceries").value
                vars[2] = document.getElementById("other").value
            }
            else if (type == "savings") {
                vars[0] = document.getElementById("emergency").value
                vars[1] = document.getElementById("retirement").value
                vars[2] = document.getElementById("debts").value

            }
            else { 
                vars[0] = document.getElementById("vacation").value
                vars[1] = document.getElementById("clothing").value
                vars[2] = document.getElementById("other2").value
            }

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
                    if (type == "necessities"){
                        let rent = document.getElementById("rent-display");
                        rent.innerHTML = vars[0]
                        let groceries = document.getElementById("groceries-display");
                        groceries.innerHTML = vars[1]
                        let other = document.getElementById("other-display");
                        other.innerHTML = vars[2]
                    }
                    else if (type == "savings") {
                        let emergency = document.getElementById("emergency-display");
                        emergency.innerHTML = vars[0]
                        let retirement = document.getElementById("retirement-display");
                        retirement.innerHTML = vars[1]
                        let debt = document.getElementById("debt-display");
                        debt.innerHTML = vars[2]
                    }
                    else {
                        let vacation = document.getElementById("vacation-display");
                        vacation.innerHTML = vars[0]
                        let clothing = document.getElementById("clothing-display");
                        retirement.innerHTML = vars[1]
                        let other = document.getElementById("other2-display");
                        other.innerHTML = vars[2]
                    }
                })
            })

            fetch(`${window.origin}/budget`, {
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
              response.json().then(function (data) {});
            });
        })

        

    
}
