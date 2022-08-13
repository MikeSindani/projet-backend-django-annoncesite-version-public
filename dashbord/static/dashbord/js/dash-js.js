// *********************** AJAX FAVORIS *********************************
/*
function get_favoris_user(variable){
if(variable == "Home"){
  console.log("fonctionner");
  var vr = "favoris"
  var Box = document.getElementById("favoris-containe")
}
  var uid = $("#uid").attr("data-uid"); 
  
  $.ajax({
      type: 'GET',
      url: `/get_favoris_user/${uid}/${vr}`,
      success: function(response){
          console.log(response)
          var data = response.data
          setTimeout(()=>{
              
              console.log(data)
              
              //const donnee = new Array(data);
          
              data.forEach(el=> {
                  Box.innerHTML += `
                  <div class="card-long">
                  <div class="thumbnail" >
                        <img src="https://images.pexels.com/photos/375510/pexels-photo-375510.jpeg?auto=compress&cs=tinysrgb&w=600" alt="" class="card-image" height="620" width="620">
                  </div>
                  <div class="contenain" onClick='window.location.href="/description/{{work.categorie}}/{{iden.id}}"' >
                      <h2 class="titre">${el.titre}</h2>
                      <div class="prix">
                          
                      </div>
                      <div class="subtitle" style="color:${el.delai.color}">${el.delai.disponible}</div>
                      <div class="element lieu">
                          <span class="vu"><i class="fa fa-map-marker" aria-hidden="true"></i> {{data.quartier|default:"???"}}</span>
                      </div>
                      <div class="description"> ${el.description}</div>
                      <div class="commentaire"><strong>Commentaire: |50|</strong></div>
                      <div class="element">
                          <span class="vu"><i class="fa fa-users" aria-hidden="true"></i> {{data.prenom}} {{data.nom}}</span>
                          <span class="vu"><i class="fas fa-clock "></i> ${el.date}</span>
                          <span class="vu"><i class="fas fa-eye"></i> ${el.vues}</span>  
                      </div> 
                  </div>
                  <div  class="more" style="display:none;">
                      <a href="/description/{{work.categorie}}/{{iden.id}}">Voir Plus</a>
                  </div>
                  <div class="dash_control">
                      <div  class="more" id="modifier">
                          <a href="/description/{{work.categorie}}/{{iden.id}}/"><i class="fas fa-eye"></i></a>
                      </div>
                      <div  class="more" id="supprimer">
                          <a href="/supprannonce/{{work.categorie}}/{{iden.id}}"><i class="fa fa-trash"></i></a>
                      </div>
                  </div>     
              </div>   
                  `
              });
              
          }, 1000)
          //chargementBox.textContent=""
          console.log(response.size)
          if (response.size === 0) {
              //chargementBox.textContent = 'Pas de commentaire'
          }
          else if (response.size <= visible) {
              //loadBtn.classList.add('not-visible')
              //chargementBox.textContent = 'Il y a plus de commantaire...'
          }
      },
      error: function(error){
          console.log(error)
      }
  })
     
}*/





// *********************** TAB *********************************

/*
var modal = document.querySelector(".modal");
var overlay = document.querySelector(".overlay");
var wrapper = document.querySelector(".wrapper");
var button = document.querySelector(".button");
var tabButton = document.querySelector(".tabButton");

function buttonFunction(event){
  event.preventDefault();
  tabButton.style.display="none";
  modal.classList.add("is-active");
  button.classList.add("button-modal-showing");
  overlay.classList.add("overlay-modal-showing");
}

function overlayFunction(event){
  event.preventDefault();
  event.stopImmediatePropagation();
  tabButton.style.display="block";
  modal.classList.remove("is-active");
  overlay.classList.remove("overlay-modal-showing");
  button.classList.remove("button-modal-showing");
};
/* for tab fonctionement */ 
/*
function openPage(pageName,elmnt) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.border = "";
    }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.borderBottom = '4px solid black';
  //get_favoris_user(pageName);
}*/

// Get the element with id="defaultOpen" and click on it
//document.getElementById("defaultOpen").click();

/*
function checkfrom(a){
var titre = document.getElementById("titre");
var produit = document.getElementById("produit");
var quatite = document.getElementById("quatite");
  if(a==1){
    if(titre.value != "" && produit.value != "" && quatite.value !=""){
      document.getElementById("btn_suivant_1").disabled = true;
    }
  }
}*/