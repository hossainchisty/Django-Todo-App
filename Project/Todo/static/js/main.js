const dropitems = document.querySelector('.drop-items')

new Sortable(dropitems, {
    animation: 330,

});

const completed = document.querySelector('.drop-completed')

new Sortable(completed, {
    animation: 330,
})


function myFunction(){
    var element = document.body;
    element.classList.toggle("dark-mode");
}