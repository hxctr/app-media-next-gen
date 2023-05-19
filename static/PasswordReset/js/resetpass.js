let headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS');

function searchPass() {

    //Obteniendo la data para el registro
    let username = document.getElementById("username").value;
    //Mando a hacer la peticion
    fetch('http://localhost:5000/getPassword/' + username, {
        method: 'POST',
        headers: headers,
        body: `{  
              "username":"${username}"
                       }`,
    })
        //Aca espero a mi respuesta
        .then(response => response.json())
        //Aca yo ya trabajo con la respuesta
        .then(data => {
            alert("Your password is: " + data['password'])
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}