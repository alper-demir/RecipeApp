  $(document).ready(function(){
            const url = $(location).attr('href')
            if(url=='http://127.0.0.1:8000/maincourse'|| url == 'http://127.0.0.1:8000/sweet' || url == 'http://127.0.0.1:8000/vegetable'){

                $('#input-search').on('input',function(e){
                    $(".recipe-title #title").each( function() {
                        if($(this).text().toLowerCase().includes(e.target.value.toLowerCase()) == false){
                            $(this).parents('.card-main').hide()
                        }
                        else{
                            $(this).parents('.card-main').show()
                        }
                    });
                })
            }
        });

        var date = new Date;
        let year = date.getFullYear();
        document.getElementById('year').innerHTML = year;
