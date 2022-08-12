
      var myIndex = 0;
      carousel();
      bonjour();
      
      function carousel() {
        var i;
        var x = document.getElementsByClassName("mySlides");
        for (i = 0; i < x.length; i++) {
          x[i].style.display = "none";  
        }
        myIndex++;
        if (myIndex > x.length) {myIndex = 1}    
        x[myIndex-1].style.display = "block";  
        setTimeout(carousel, 3000); // Change image every 2 seconds
      }

      function bonjour(){
        var b = document.getElementById("bjr");
        var darkmode = document.getElementsByTagName("body");
        var d = new Date();
        var x=d.getHours();
        if(x=>18 && x<=6){
          b.innerHTML ="Bonsoir";
        }else{
          b.innerHTML ="Bonjour";
        }
      }