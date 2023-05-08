
		//Agregando validaciones de  cors para que no suframos
		let headers = new Headers();
		headers.append('Content-Type', 'application/json');
		headers.append('Accept', 'application/json');
		headers.append('Access-Control-Allow-Origin', 'http://localhost:5001');
		headers.append('Access-Control-Allow-Credentials', 'true');
		headers.append('GET', 'POST', 'OPTIONS');

		//Esta sera la funcion de login 
		function iniciarsesion(){
			//Obtener el valor de los inputs
			var username = document.querySelector("#username").value;
			var password = document.querySelector("#password").value;
			//Mando a hacer la peticion
			fetch('http://localhost:8000/iniciarsesion', {
  				method: 'POST',
  				headers: headers,
  				body: `{
    				"username":"${username}",
        			"password":"${password}"
                     }`,
				})
			//Aca espero a mi respuesta
			.then(response => response.json())
			//Aca yo ya trabajo con la respuesta
			.then(data => {
				if(data.data=="admin"){
                    alert('El usuario es el admin')
                    window.location.replace('https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_url_relative')
				}
				else if(data.data=="true"){
					window.location.replace('https://www.youtube.com/watch?v=ws00k_lIQ9U&ab_channel=BadBunny')
				}else{
					alert('Verifique sus credenciales')
				}
  		
			})
			.catch((error) => {
  				console.error('Error:', error);
			});

		}
