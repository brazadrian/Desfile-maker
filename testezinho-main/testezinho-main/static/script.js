let btnMenu = document.querySelector('.toggle-menu');
let menuHamburguer = document.querySelector('.menu-hamburguer')
let body = document.querySelector('body')
let video = document.querySelector('#videos-link')
let contatos = document.querySelector('#contatos-link')

btnMenu.addEventListener("click", menu);


function link(){
  menuHamburguer.classList.toggle('show')
  btnMenu.classList.toggle('active')
  body.classList.toggle('block')
}

function menu(){
  menuHamburguer.classList.toggle('show')
  btnMenu.classList.toggle('active')
  body.classList.toggle('block')
}

video.addEventListener('click', link)
contatos.addEventListener('click', link)