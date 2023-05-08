		let headers = new Headers();
		headers.append('Content-Type', 'application/json');
		headers.append('Accept', 'application/json');
		headers.append('Access-Control-Allow-Origin', 'http://localhost:8000');
		headers.append('Access-Control-Allow-Credentials', 'true');
		headers.append('GET', 'POST', 'OPTIONS');


		function getSignIn(){
			//Obtener el valor de los inputs
			var username = document.querySelector("#username").value;
			var password = document.querySelector("#password").value;
			//Mando a hacer la peticion
			fetch('http://localhost:8000/getSignIn', {
  				method: 'POST',
  				headers: headers,
  				body: `{
    				"username":"${username}",
        			"password":"${password}"
                     }`,
				})

			.then(response => response.json())

			.then(data => {
				if(data.data=="admin"){
                    alert('Ingresando como administrador')
                    window.location.replace('https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_url_relative')
				}
				else if(data.data=="true"){
					window.location.replace('../NormalUser/normalUser.html')
				}else{
					alert('Usuario o contraseña incorrecto')
				}
  		
			})
			.catch((error) => {
  				console.error('Error:', error);
			});

		}
