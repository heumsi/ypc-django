$(document).ready(function(){
	if( $(window).width() < 600 ){
		$('#topbar').scrollupbar.destroy
	}else{
		$('#topbar').scrollupbar();
	}

    $(".menu-icon").on("click", function(){
        $(".menu").toggle();
    })
})
