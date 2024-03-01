import requests
# este archivo enviará solicitudes al servidor
# requests.get(http...) realiza una solicitud GET a la URL
# estamos interesados en el metodo para enviar mensajes al servidor requests.post(http...)
# lo que hace json es transferir al servidor
name = input('Введите имя: ')
while True:
    text = input('Введите сообщение: ')
    response = requests.post('http://127.0.0.1:5000/send',
                             json={
                                 'name': name,
                                 'text': text
                             }
                            )
