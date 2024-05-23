//Carga de todas las categorias en el lateral
function getCategories(){
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
}

//Carga de todos los podcasts
function getPodcasts(){
    //Selector de grupo de los botones de categorias
    var podcastList = document.getElementById('contenido-central');

    //Request contra el Apirestful GET CATEGORIES
    fetch("http://localhost:8000/podcasts/",{method:"GET"})
    .then((response) => response.json())
    .then((podcasts) => {
        //Carga en el DOM de los datos de categorias
        //Generacion automatica de botones datos de categorias
        var podcastListDOM=""

        podcasts.map((podcast,index)=>{
            index=index+1
            podcastListDOM=podcastListDOM+`
            <!-- PODCAST -->
            <div class="card border-5 border-danger" style="width: 18rem;">
                <h6 class="card-title text-uppercase text-white text-center pt-2">${podcast.title}</h6>
                <div class="card-body">
                    <p class="card-text text-body-secondary">${podcast.description.split(' ').slice(0, 10).join(' ')+" ..."}</p>
                    <a href="#"><img src="./img/btn_play.png" alt=""></a>
                </div>
            </div>
            <!-- PODCAST -->
            `
        })

        //Cargamos las categorias
        podcastList.innerHTML=podcastListDOM    
    })
    .catch((err) => console.log("Error", err))
}



//Carga de datos en index.html
getCategories()
getPodcasts()



