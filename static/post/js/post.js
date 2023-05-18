let headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS');




function post() {



	//Obteniendo la data para el registro
	var username = document.querySelector("#username").value;
	var headline = document.querySelector("#headline").value;
	var body_post = document.querySelector("#body_post").value;
	//Mando a hacer la peticion
	fetch('http://localhost:5000/add_post', {
		method: 'POST',
		headers: headers,
		body: `{  
					"username":"${username}",
					"headline":"${headline}",
    				"body_post":"${body_post}"
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