# FlipperZero_Authenticator_Import


## Steps

1. Cloning google-authenticator-exporter
2. Build google-authenticator-exporter container (you need docker to be installed) for exporting in JSON format out TOTP secret
3. Exporting QR from Google Authenticator App
3. Download add2FA.py script
4. Executing add2FA.py for creating the 'totp.conf' file for flipperzero

## Instructions

1. Let clone the goole-authenticator-exporter repository
	```	bash
	git clone https://github.com/krissrex/google-authenticator-exporter
	```
	
2. Let build the docker container
	```	bash
	cd google-authenticator-exporter && docker build . --tag google-authenticator-exporter:0.0.1
	```

3. Let put this container on fire
	```	bash
	mkdir my_totps && docker run -v ./my_totps:/src -it --rm google-authenticator-exporter:0.0.1
	```

	- SUGGEST: You can use '**zbarcam**' command to scan the QR Code exported from Google Authenticator. It should look like this '**otpauth-migration://offline?data=ttteoetjrhejhte...etc**'

4. Decode the QR and copy the value
	1. The script once the container is running will ask for totpUri. Just paste the QR code value copied & press enter

	2. Just type '**y**' & press enter

	3. Choose the name for the json file just be sure that includes '**/src/**. Example
		- 	```bash
			/src/my_totp.json
			```
	
5. Check if json has been created & download script
	```bash
	cd my_totps && wget https://raw.githubusercontent.com/IadRabbit/FlipperZero_Authenticator_Import/main/add2FA.py
	```

6. Let execute this beauty
	1. First download from your flipper the '**totp.conf**' file (DO NOT CHANGE NAME FILE & BACKUP your current '**totp.conf**' file) and put it inside the '**my_totps**' folder

	2. Let execute the script
		- ### INFORMATION 
			- The '**totp.conf**' would be just updated no previous configuration will be deleted

			- If you have multiple json file exported DO NOT worry all '**.json**' file will be parsed and added to '**totp.conf**'

		```bash
		python3 add2FA.py
		```

7. Your new dolphin key
	Replace the '**totp.conf**' file with the new one inside your FlipperZero