let btnMenu = document.querySelector('.toggle-menu');
let menuHamburguer = document.querySelector('.menu-hamburguer')

btnMenu.addEventListener("click", menu);

function menu(){
  menuHamburguer.classList.toggle('show')
  btnMenu.classList.toggle('active')
}