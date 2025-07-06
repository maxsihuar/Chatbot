import {Bot, User} from './Chat.js'


function GetText(){
    var Input = document.getElementById("prompt").value;
    return Input
}

document.addEventListener("DOMContentLoaded",()=>{
  const Btn = document.getElementById('Btn-PostData');
  Btn.addEventListener('click',()=>{
    User()
    PostData()
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
