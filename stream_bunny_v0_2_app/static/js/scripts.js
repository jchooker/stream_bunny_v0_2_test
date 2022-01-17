const search = document.getElementById('search')
const search_input = document.getElementById('movie_titles')
const results_box = document.getElementById('results-box')

search_input.addEventListener('keyup', e=>{
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
                            <div class="col-2">
                                <img src="${movie.poster_link}" class="movie-img"> 
                            </div>
                            <div class="col-10">
                                <h5>${movie.title}</h5>
                                <p class="text-muted">${movie.year}</p>
                            </div>
                        </div>
                    </a>`
                })
                results_box.classList.remove('not-visible')
            }
        })
    }
})

document.querySelectorAll(".item").forEach(function(movie){
    movie.addEventListener("click", function(e){
    e.preventDefault()
    $.ajax({
        url: `/get_movie/${this.getAttribute("movie-id")}`,
        type: `GET`,
        success: function(response){
            console.log(response)
        }
    })
})
})