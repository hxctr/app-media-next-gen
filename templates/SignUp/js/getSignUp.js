let headers = new Headers();
		headers.append('Content-Type', 'application/json');
		headers.append('Accept', 'application/json');
		headers.append('Access-Control-Allow-Origin', 'http://localhost:8000');
		headers.append('Access-Control-Allow-Credentials', 'true');
		headers.append('GET', 'POST', 'OPTIONS');
		function getSignUp(){
			//Obteniendo la data para el registro
			var name = document.querySelector("#username").value;
			var lastName = document.querySelector("#lastname").value;
			var username = document.querySelector("#username").value;
			var password = document.querySelector("#password").value;
			//Mando a hacer la peticion
			fetch('http://localhost:8000/addUser', {
  				method: 'POST',
  				headers: headers,
  				body: `{  
					"nombre":"${name}",
					"apellido":"${lastName}",
    				"username":"${username}",
        			"password":"${password}"
                     }`,
				})
			//Aca espero a mi respuesta
			.then(response => response.json())
			//Aca yo ya trabajo con la respuesta
			.then(data => {
				alert(data.data)
			})
			.catch((error) => {
  				console.error('Error:', error);
			});

		}