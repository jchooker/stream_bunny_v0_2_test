const search = document.getElementById('search')
const search_input = document.getElementById('movie_titles')
const results_box = document.getElementById('results-box')
const movie_details = document.getElementById('movie-details')

const debounce = (func, timer) =>{
    let timeId = null;
    return (...args) =>{
        if(timeId){
            clearTimeout(timeId);
        }
        timeId = setTimeout(()=>{
            func(...args);
        }, timer)
    }
}

function movie_search(){
    let input_field = document.querySelector('#movie_titles');
    input_field.addEventListener('keyup', debounce((e)=>{
        console.log(e.target.value)
        if (e.target.value.length > 2) {
            $.ajax({
                url: `/search/${e.target.value}`,
                type: 'GET',
                success: function(data){
                    console.log(data)
                    results_box.innerHTML=''
                    data.forEach(movie=> { // correct way to access the various '${movie.[thing]} elements from imdbpy database??
                    results_box.innerHTML += `
                        <a href="" class="item" movie-id="${movie.id}"> 
                            <div class="row mt-2 mb-2">
                                <div class="col-10">
                                    <h5>${movie.title}</h5>
                                    <p class="text-muted">${movie.year}</p>
                                    <a href="like/${movie.id}">Like</a>
                                </div>
                            </div>
                        </a>`
                    })
                    results_box.classList.remove('not-visible')
                    document.querySelectorAll(".item").forEach(function(movie){
                        movie.addEventListener("click", function(e){
                            e.preventDefault()
                            $.ajax({
                                url: `/get_movie/${this.getAttribute("movie-id")}`,
                                type: `GET`,
                                success: function(response){
                                    if ('director' in response) {

                                        console.log(response.streaming_on);  

                                        movie_details.innerHTML=''
                                        movie_details.innerHTML += `
                                        <h3>${response.title}</h3>
                                        <h5>${response.year}</h5>
                                        <img src="${response.poster_link}" class="movie-img">
                                        <h5>${response.director}</h5>
                                        <p>${response.plot}</p>
                                        <h5>Streaming at: </h5>
                                        <div class='stream-div d-inline-flex justify-content-center'>
                                        <a href='${response.go_to_stream}'><img src='/static/images/${response.streaming_on}.png' class='stream-logo'></a>
                                        </div>`
    
    
                                    } else {

                                        console.log(response);  

                                        movie_details.innerHTML=''
                                        movie_details.innerHTML += `
                                        <h3>${response.title}</h3>
                                        <h5>${response.year}</h5>
                                        <img src="${response.poster_link}" class="movie-img">
                                        <p>${response.plot}</p>
                                        <h5>Streaming at: </h5>
                                        <div class='stream-div d-inline-flex justify-content-center'>
                                        <a href='${response.go_to_stream}'><img src='/static/images/${response.streaming_on}.png'></a>
                                        </div>`                                   
                                    }
                                    // console.log(response.streaming_on.stream_link, response.streaming_on.stream)
                                    movie_details.classList.remove('not-visible')
                                }
                            })
                        })
                    })
                }
            })
        }
        
    }, 200))
}

movie_search()

// search_input.addEventListener('keyup', e=>{
//     console.log(e.target.value)
//     if (e.target.value.length > 2) {
//         $.ajax({
//             url: `/search/${e.target.value}`,
//             type: 'GET',
//             success: function(data){
//                 console.log(data)
//                 results_box.innerHTML=''
//                 data.forEach(movie=> { // correct way to access the various '${movie.[thing]} elements from imdbpy database??
//                 results_box.innerHTML += `
//                     <a href="" class="item" movie-id="${movie.id}"> 
//                         <div class="row mt-2 mb-2">
//                             <div class="col-2">
//                                 <img src="${movie.poster_link}" class="movie-img"> 
//                             </div>
//                             <div class="col-10">
//                                 <h5>${movie.title}</h5>
//                                 <p class="text-muted">${movie.year}</p>
//                                 <a href="like/${movie.id}">Like</a>
//                             </div>
//                         </div>
//                     </a>`
//                 })
//                 results_box.classList.remove('not-visible')
//                 document.querySelectorAll(".item").forEach(function(movie){
//                     movie.addEventListener("click", function(e){
//                         e.preventDefault()
//                         $.ajax({
//                             url: `/get_movie/${this.getAttribute("movie-id")}`,
//                             type: `GET`,
//                             success: function(response){
//                                 if ('director' in response) {
//                                     movie_details.innerHTML=''
//                                     movie_details.innerHTML += `
//                                     <h3>${response.title}</h3>
//                                     <h5>${response.year}</h5>
//                                     <img src="${response.poster_link}" class="movie-img">
//                                     <h5>${response.director}</h5>
//                                     <p>${response.plot}</p>
//                                     <h5>Streaming at: </h5>
//                                     <div class='stream-div'>
//                                     <a href='${response.go_to_stream}'><img src='/static/images/${response.streaming_on}.png'></a>
//                                     </div>`


//                                 } else {
//                                     movie_details.innerHTML=''
//                                     movie_details.innerHTML += `
//                                     <h3>${response.title}</h3>
//                                     <h5>${response.year}</h5>
//                                     <img src="${response.poster_link}" class="movie-img">
//                                     <p>${response.plot}</p>
//                                     <h5>Streaming at: </h5>
//                                     <div class='stream-div'>
//                                     <a href='${response.go_to_stream}'><img src='/static/images/${response.streaming_on}.png'></a>
                                    
//                                     </div>`                                   
//                                 }
//                                 console.log(response.streaming_on.stream_link, response.streaming_on.stream)
//                                 movie_details.classList.remove('not-visible')
//                             }
//                         })
//                     })
//                 })
//             }
//         })
//     }
// })