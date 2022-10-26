
const btn = document.getElementsByClassName('toggle')
let escondido = document.querySelector('.hiden')

if(btn){
    btn.addEventListener('click', swapper, menu);
  }

function menu() {
    escondido.classList.toggle('escondido')
    alert("ola")
}
