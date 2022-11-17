let btnMenu = document.querySelector('.toggle-menu');
let menuHamburguer = document.querySelector('.menu-hamburguer')
let body = document.querySelector('body')
let video = document.querySelector('#videos-link')
let contatos = document.querySelector('.contatos-link')


function menu(){
  menuHamburguer.classList.toggle('show')
  btnMenu.classList.toggle('active')
  body.classList.toggle('block')
}

btnMenu.addEventListener("click", menu);
contatos.addEventListener("click", menu);
video.addEventListener("click", menu);
