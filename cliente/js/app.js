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

//Carga de todas las categorias en el formulario
function getCategoriesForm(){
    //Selector de grupo de los botones de categorias
    var categoryList = document.getElementById('categoria');


    //Request contra el Apirestful GET CATEGORIES
    fetch("http://localhost:8000/categories/",{method:"GET"})
    .then((response) => response.json())
    .then((categorias) => {
        //Carga en el DOM de los datos de categorias
        //Generacion automatica de botones datos de categorias
        var categoryListDOM=""

        categorias.map((cat,index)=>{
            var opt = document.createElement('option');
            opt.value = cat.id;
            opt.innerHTML = cat.name;
            categoryList.appendChild(opt);
        })
    })
    .catch((err) => console.log("Error", err))
}

//Carga de todos los autores en el formulario
function getAuthorsForm(){
    //Selector de grupo de los botones de categorias
    var autorList = document.getElementById('autor');


    //Request contra el Apirestful GET CATEGORIES
    fetch("http://localhost:8000/authors/",{method:"GET"})
    .then((response) => response.json())
    .then((authors) => {
        //Carga en el DOM de los datos de categorias
        //Generacion automatica de botones datos de categorias
        var autorListDOM=""

        authors.map((author,index)=>{
            var opt = document.createElement('option');
            opt.value = author.id;
            opt.innerHTML = author.name;
            autorList.appendChild(opt);
        })
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

//Carga de todos los episodios para un podcast
function getPodcastAuthors(podcast){
    //Selector de grupo de los botones de categorias
    var authorsList = document.getElementById('contenido-central');

    //Request contra el Apirestful GET CATEGORIES
    fetch(`http://localhost:8000/podcasts/${podcast}/authors`,{method:"GET"})
    .then((response) => response.json())
    .then((podcasts) => {
        //Guardo los autores
        authors=podcasts.authors;
        //Carga en el DOM de los datos de autores para un podcast
        var authorsListDOM=""
        if(authors.length>0){
            authors.map((author,index)=>{
                index=index+1
                authorsListDOM=authorsListDOM+`
                <!-- AUTHOR -->
                <div class="card border-5 border-danger" style="width: 18rem;">
                    <img src="./img/btn_author.png" class="card-img-top" alt="${author.name}">
                    <h6 class="card-title text-uppercase text-white text-center pt-2">${author.name}</h6>
                    <div class="card-body">
                        <p class="card-text text-body-secondary">${author.nationality}</p>
                    </div>
                </div>
                <!-- AUTHOR -->
                `
            })
        }else{
            authorsListDOM=authorsListDOM+`
            <!-- AUTHOR -->
            <div class="card border-5 border-danger" style="width: 18rem;">
                <h6 class="card-title text-uppercase text-white text-center pt-2">PODCAST SIN AUTORES</h6>
                <div class="card-body">
                    <p class="card-text text-body-secondary">Este podcast es totalmente anónimo</p>
                </div>
            </div>
            <!-- AUTHOR -->
            `            
        }
        //Cargamos las categorias
        authorsList.innerHTML=authorsListDOM    
    })
    .catch((err) => console.log("Error", err))
}

//Carga de todos los podcasts
function getPodcastsSimpleList(conEnlaces){
    //Selector de grupo de los botones de podcasts
    var podcastList = document.getElementById('podcasts-selectores');
    //Detectamos si los botones de podcast realizan accion
    var accionBotonPodcast=``

    //Request contra el Apirestful GET CATEGORIES
    fetch("http://localhost:8000/podcasts/",{method:"GET"})
    .then((response) => response.json())
    .then((podcasts) => {
        //Carga en el DOM de los datos de categorias
        //Generacion automatica de botones datos de categorias
        var podcastListDOM=""

        podcasts.map((podcast,index)=>{
            if(conEnlaces){
                accionBotonPodcast=`onclick="getPodcastAuthors(${podcast.id});return false;"`
            }
            index=index+1
                podcastListDOM=podcastListDOM+`
                <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio${index}" ${accionBotonPodcast} autocomplete="off" ">
                <label class="btn btn-outline-danger" for="vbtn-radio${index}">${podcast.title}</label>`
        })

        //Cargamos las categorias
        podcastList.innerHTML=podcastListDOM    
    })
    .catch((err) => console.log("Error", err))
}



//Nuevo
function addPodcast(){
    //Recogemos datos del formulario
    var podcastTitle = document.getElementById('title');
    var podcastDescription = document.getElementById('description');
    var podcastUrl = document.getElementById('url');
    var podcastCat = document.getElementById("categoria");
    var podcastAuthor = document.getElementById("autor");

    //Request contra el Apirestful PUT PODCAST
    fetch("http://localhost:8000/podcasts/",
        {method:"POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"title": `${podcastTitle.value}`, "category_id": `${podcastCat.value}`,"description": `${podcastDescription.value}`,"url": `${podcastUrl.value}`,
            "authors": [{"id":`${podcastAuthor.value}`}]})
        }
    )
    .then((response) => response.json())
    .then(() => {
        //Recarga de podcasts
        getPodcastsSimpleList(false)
    })
    .catch((err) => console.log("Error", err))

}




