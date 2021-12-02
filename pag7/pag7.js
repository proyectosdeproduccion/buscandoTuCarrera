const carrera = document.getElementById('carreras');
let info = document.querySelector('.info');

carrera.addEventListener('click', ()=>{
    info.classList.toggle('active');
    infoCursos.classList.remove("activec")
});
//Curso
const cursos = document.getElementById('curso');
let infoCursos = document.querySelector('.cursos');

cursos.addEventListener('click', ()=>{
    infoCursos.classList.toggle('activec');
    info.classList.remove("active")
});