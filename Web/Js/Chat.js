
export function CreateChat(){
    var Chat = document.getElementById("prompt").value;

    return Chat;

}

export function Bot(mensaje){
    var ModelBot =
            "<div class='container overflow-auto  p-1 h-25 mh-50 mw-50 position-relative' style='height: auto; '>"+
                "<div id = 'chat-content' class='container shadow-sm p-2 bg-body-tertiary rounded tm-5 position-absolute start-0 w-50 mw-70 h-150 mh-200'>"+mensaje+"</div>"+
            "</div>";
    document.getElementById("chat").innerHTML+=ModelBot;
    
}


export function User(){
    var mensaje = CreateChat()
    var ModelUser =     
            "<div class='container overflow-auto  p-1 h-25 mh-50 mw-50 position-relative' style='height: auto;'>"+
                "<div id = 'chat-content' class='container shadow-sm p-2 bg-body-tertiary rounded tm-4  position-absolute start-50 w-50 mw-70' style='height: auto;'>"+mensaje+"</div>"+
            "</div>";

    document.getElementById("chat").innerHTML+=ModelUser;
}
