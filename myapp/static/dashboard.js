
window.onload() = function(){

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

    let necessities = document.getElementById("necessitiesBtn");
    necessities.addEventListener('click', function() {
        const myModal = new bootstrap.Modal('#modal-n');
        myModal.show()
    })

    let submit = document.getElementById("submitBtn");
    

    submit.addEventListener('click', function(event){
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
                
            })
        })
    })

    

    
}