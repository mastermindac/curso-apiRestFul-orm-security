//Selector de grupo de los botones de categorias
var categoryList = document.getElementById('categorias-selectores');

//Datos de prueba
var categoriesData = [
    {name:"music"},
    {name:"technology"}
]

//Request contra el Apirestful GET CATEGORIES
fetch("http://localhost:8000/categories/",{method:"GET"})
.then((response) => response.json())
.then((categorias) => {
    //Carga en el DOM de los datos de categorias
    //Generacion automatica de botones datos de categorias
    var categoryListDOM=""

    categorias.map((cat,index)=>{
        index=index+1
        categoryListDOM=categoryListDOM+`
        <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio${index}" autocomplete="off" checked>
        <label class="btn btn-outline-danger" for="vbtn-radio${index}">${cat.name}</label>`
    })

    //Cargamos las categorias
    categoryList.innerHTML=categoryListDOM    
})
.catch((err) => console.log("Error", err))

