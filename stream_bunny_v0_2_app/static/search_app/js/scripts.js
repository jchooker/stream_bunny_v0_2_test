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
                    data.forEach(movie=> {
                        final_cast = '';
                            if (movie.cast.length === 0) {
                                final_cast = final_cast;
                            } else if (movie.cast.length === 1) {
                                final_cast = movie.cast;
                            } else {
                                for (i = 0; i < movie.cast.length - 1; i++) {
                                    final_cast += (movie.cast[i] + ', ');
                                }
                                final_cast += movie.cast[movie.cast.length - 1];
                            }
                        results_box.innerHTML += `
                            <a href="" class="item" movie-id="${movie.id}"> 
                            <div class="row mt-2 mb-2 blue-hov">
                                <div class="col-10">
                                    <h5>${movie.title}&nbsp;(${movie.year})</h5>
                                    <div class="dd-cast"><a href="like/${movie.id}">Like</a>
                                        <span id="space">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</span>
                                        <span id="cast-parent">${final_cast}</span>
                                    </div>
                                </div>
                            </div>
                        </a>`
                        })
                    $(".blue-hov").hover(function(){
                        $(this).addClass("mouse-on1")
                    }, function(){
                        $(this).removeClass("mouse-on1")
                    })
                    results_box.classList.remove('not-visible')
                    document.querySelectorAll(".item").forEach(function(movie){
                        movie.addEventListener("click", function(e){
                            e.preventDefault()
                            $.ajax({
                                url: `/get_movie/${this.getAttribute("movie-id")}`,
                                type: `GET`,
                                success: function(response){
                                    let streams = ""
                                    for (stream of response.streams) {
                                        if (stream.stream) {
                                            streams+=`<a href='${stream.stream_link}'><img src='/static/images/${stream.stream}.png' class='stream-logo'></a>`
                                        }
                                    }
                                    movie_details.innerHTML = ''
                                    if ('title' in response) {
                                        movie_details.innerHTML += `<h2 class="yellow_text"><i>${response.title}</i></h2>`
                                    } else {
                                        movie_details.innerHTML += `<h3></h3>`
                                    }
                                    if ('year' in response) {
                                        movie_details.innerHTML += `<h4>${response.year}</h4>`
                                    } else {
                                        movie_details.innerHTML += `<h4></h4>`
                                    }
                                    if ('poster_link' in response) {
                                        movie_details.innerHTML += `<img src="${response.poster_link}" class="movie-img" alt="movie poster">`
                                    } else {
                                        movie_details.innerHTML += `<img src="/static/images/noposter.png" class="movie-img" alt="no poster">`
                                    }
                                    if (response.genres) {
                                        if (response.genres.length === 1) {
                                            movie_details.innerHTML += `<p class="mb-1"><i>${response.genres[0]}</i></p>`
                                        } else if (response.genres.length === 2) {
                                            movie_details.innerHTML += `<p class="mb-1"><i>${response.genres[0]}, ${response.genres[1]}</i></p>`
                                        } else if (response.genres.length >= 3) {
                                            movie_details.innerHTML += `<p class="mb-1"><i>${response.genres[0]}, ${response.genres[1]}, ${response.genres[2]}</i></p>`
                                        }
                                    } else {
                                        movie_details.innerHTML += `<p></p>`
                                    }
                                    if ('director' in response) {
                                        movie_details.innerHTML += `<h5>Dir. ${response.director}</h5>`
                                    } else {
                                        movie_details.innerHTML += `<h3></h3>`
                                    }
                                    if ('plot' in response) {
                                        movie_details.innerHTML += `<p class="mb-1">${response.plot}</p>`
                                    } else {
                                        movie_details.innerHTML += `<p></p>`
                                    }
                                    if ('rating' in response) {
                                        movie_details.innerHTML += `<p class="mb-1">IMDB Rating: ${response.rating}</p>`
                                    } else {
                                        movie_details.innerHTML += `<p></p>`
                                    }
                                    movie_details.innerHTML += `<h5>Streaming on: </h5>`
                                    if (streams) {
                                        movie_details.innerHTML += `
                                        <div class='stream-div d-inline-flex justify-content-center'>
                                        ${streams}
                                        </div>`
                                    } else {
                                        movie_details.innerHTML += `
                                        <div class='stream-div no-stream-result'>
                                        <h5 class='text-redify'>Title not found streaming anywhere!</h5>
                                        <img class="tyr-big" src="/static/images/tyrion.gif" alt="tyrion-no-stream">
                                        </div>`
                                    }
                                    movie_details.classList.remove('not-visible')
                                    results_box.classList.add('not-visible')
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