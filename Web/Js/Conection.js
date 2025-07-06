import {Bot, User} from './Chat.js'

/**
 * Obtiene el texto ingresado por el usuario desde el input con id 'prompt'.
 * @returns {string} Texto ingresado por el usuario.
 */

function GetText(){
    var Input = document.getElementById("prompt").value;
    return Input
}

/**
 * Espera a que el DOM esté completamente cargado para asignar eventos.
 * Agrega un evento al botón con id 'Btn-PostData' que:
 * 1. Ejecuta la función `User()` para mostrar el mensaje del usuario.
 * 2. Llama a `PostData()` para enviar la consulta al backend.
 */


document.addEventListener("DOMContentLoaded",()=>{
  const Btn = document.getElementById('Btn-PostData');
  Btn.addEventListener('click',()=>{
    User()
    PostData()
  })
})

/**
 * Realiza una petición POST a la API `/api/v1/consulta` enviando el texto del usuario.
 * Espera una respuesta JSON con la clave 'respuesta' y la muestra usando `Bot()`.
 */

function PostData(){
  fetch("/api/v1/consulta",{
    method: "POST",
    headers: {
      "Content-Type" : "application/json"
    },
    body:JSON.stringify({
      consulta : GetText()
    })
  })
  .then(res => res.json())
  .then(data => {console.log(data);
    return data;
  }).then(data => Bot(data["respuesta"]))
  
}
