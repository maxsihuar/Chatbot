
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
            "<div class='container overflow-auto  p-1 h-25 mh-50 mw-50 position-relative' style='height: auto; '>"+
                "<div id = 'chat-content' class='container shadow-sm p-2 bg-body-tertiary rounded tm-5 position-absolute start-0 w-50 mw-70 h-150 mh-200'>"+mensaje+"</div>"+
            "</div>";
    document.getElementById("chat").innerHTML+=ModelBot;
    
}

/**
 * Toma el mensaje ingresado por el usuario y lo muestra en el área del chat.
 * Utiliza `CreateChat()` para obtener el contenido del input.
 */

export function User(){
    var mensaje = CreateChat()
    var ModelUser =     
            "<div class='container overflow-auto  p-1 h-25 mh-50 mw-50 position-relative' style='height: auto;'>"+
                "<div id = 'chat-content' class='container shadow-sm p-2 bg-body-tertiary rounded tm-4  position-absolute start-50 w-50 mw-70' style='height: auto;'>"+mensaje+"</div>"+
            "</div>";

    document.getElementById("chat").innerHTML+=ModelUser;
}
