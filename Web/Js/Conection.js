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
 * Coloca una pregunta frecuente en el input, muestra el mensaje del usuario
 * y llama directamente a PostData().
 * 
 * @param {string} pregunta - Pregunta frecuente a enviar al chatbot.
 */
window.sendFAQ = function(pregunta) {
    const input = document.getElementById('prompt');
    if (!input) return;

    input.value = pregunta;
    User();
    PostData();
    input.value = "";
};


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
    document.getElementById("prompt").value = "";
  })
})


document.addEventListener("DOMContentLoaded",()=>{
      PostData()
      document.getElementById("prompt").value = "";
})

/**
 * Realiza una petición POST a la API `/api/v1/consulta` enviando el texto del usuario.
 * Espera una respuesta JSON con la clave 'respuesta' y la muestra usando `Bot()`.
 */

document.addEventListener("DOMContentLoaded",()=>{
  document.addEventListener('keydown', function(event){
    if(event.key==="Enter"){
      User()
      PostData()
      document.getElementById("prompt").value = "";
    }
  })
})

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
