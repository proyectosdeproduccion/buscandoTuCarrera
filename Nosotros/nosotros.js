const carrera = document.getElementById('carreras');
let info = document.querySelector('.info');

carrera.addEventListener('click', ()=>{
    info.classList.toggle('active');
});
//Curso
const cursos = document.getElementById('curso');
let infoCursos = document.querySelector('.cursos');

cursos.addEventListener('click', ()=>{
    infoCursos.classList.toggle('activec');
});