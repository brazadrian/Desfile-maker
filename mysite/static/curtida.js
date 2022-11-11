const button = document.querySelector('#like');
const number = document.querySelector('#number');
const curtida = document.querySelector('.curida')

/*button.addEventListener('click', () => {
  let likeValue = document.querySelector('#number').textContent;
  let newValue = Number(likeValue) + 1;
  button.classList.add('like');
  number.innerHTML = newValue;
});*/

curtida.addEventListener('click', trocarCoracao)  

function trocarCoracao(){
  curtida.style.backgroundColor = 'red';
}

