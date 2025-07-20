
/**
 * Obtiene el mensaje actual escrito por el usuario en el input con id 'prompt'.
 * @returns {string} Texto ingresado por el usuario.
 */

export function CreateChat(){
    var Chat = document.getElementById("prompt").value;

    return Chat;

}

/**
 * Muestra el mensaje generado por el modelo (bot) en el área del chat.
 *
 * @param {string} mensaje - Texto generado por la IA que será mostrado al usuario.
 */

export function Bot(mensaje){
    var ModelBot =
        `<div class='container-fluid d-flex justify-content-start my-2 px-2'>
            <div class='p-2 bg-light rounded shadow-sm' style='display: inline-block; max-width: 85%; word-wrap: break-word;'>
                <i class='fas fa-robot me-2'></i>${mensaje}
            </div>
        </div>`;
    
    document.getElementById("chat").innerHTML += ModelBot;
}

/**
 * Toma el mensaje ingresado por el usuario y lo muestra en el área del chat.
 * Utiliza `CreateChat()` para obtener el contenido del input.
 */

export function User(){
    var mensaje = CreateChat()
    var ModelUser =
        `<div class='container-fluid d-flex justify-content-end my-2 px-2'>
            <div class='p-2 bg-secondary text-white rounded shadow-sm' style='display: inline-block; max-width: 85%; word-wrap: break-word;'>
                ${mensaje}
            </div>
        </div>`;

    document.getElementById("chat").innerHTML+=ModelUser;

}
