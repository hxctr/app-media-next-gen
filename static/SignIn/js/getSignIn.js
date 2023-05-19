let headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS');

function getSignIn() {
	//Obtener el valor de los inputs
	var username = document.querySelector("#username").value;
	var password = document.querySelector("#password").value;
	//Mando a hacer la peticion
	fetch('http://localhost:5000/postLogin', {
		method: 'POST',
		headers: headers,
		body: `{
    				"username":"${username}",
        			"password":"${password}"
                     }`,
	})

		.then(response => response.json())
		.then(data => {
			if (data.data == "admin") {
				alert('Sign In as admin')
				window.location.replace('http://localhost:5000/admin')
			}
			else if (data.data == "true") {
				console.log(data.username)
				window.location.replace('http://localhost:5000/dashboard')
			} else {
				alert('Invalid credentials')
			}

		})
		.catch((error) => {
			console.error('Error:', error);
		});

}
