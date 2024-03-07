<<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<h1>VulnForge | herramienta de phishing</h1><br>
	<p>Aqui les presento una herramienta programada en python3<br>
		que funciona para poder configurar un login falso en tu servidor<br>
		apache2 desde tu distro de linux.<br>
	</p><br>
	<h2>Requisitos de instalacion</h2><br>
	<p>Lo primero que debemos hacer es instalar python3 con el siguiente comando<br><br>
		sudo apt -y install python3 <br>
		sudo apt -y install python3-pip<br>
		tar -xf sites.tar.gz<br>
		pip3 install colorama<br><br>
		luego debemos instalar apache2:<br><br>
		sudo apt -y install apache2</p><br><br>
		<h1>Manual de uso</h1><br>
		<p>
			=========================<br>
			COMANDOS DE LA CONSOLA
			=========================<br>
			cd : sirve para navegar a algun directorio<br>
			su uso es : cd /example/<br>
			ls : funciona para listar un directorio<br>
			help : puedes solicitar ayuda<br>
			==========================
			Como instalar un login???
			==========================
			Para instalar un login utilizaremos el comando LOAD<br><br>
			VulnForge>> LOAD /phish/instagram<br><br>
			Como pudimos observar utilizamos el comando LOAD<br>
			seguido de la ruta del fichero a instalar.<br>
			Para listar los ficheros a instalar utilizaremos el siguiente<br>
			comando<br>
			<br>
			VulnForge>> list phishing
			<br><br>
			De este modo seleccionando nuestro fichero podremos instalar<br>
			Despues de haber selecciondo nuestro login a generar<br>
			podremos ver los comandos que tenemos disponibles con el comando help<br>
		</p>
</body>
</html>