

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
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

// code for next page
// get the number step 
var item1 = document.querySelector(".item1");
var item2 = document.querySelector(".item2");
var item3 = document.querySelector(".item3");
// get the div step button
var part_info = document.querySelector(".part_info");
var part_info_2 = document.querySelector(".part_info_2"); 
var part_photo = document.querySelector(".part_photo"); 
var modal_content = document.querySelector(".modal-content");

var titre = document.getElementById("titre");
var produit = document.getElementById("produit");
// create function top change de step 
function Suivant(a,height){
    if(a == 1){
      modal_content.style.height = height;
     item1.classList.remove("isactived-item");
      part_info.classList.remove("isactived");
      item2.classList.add("isactived-item");
      part_info_2.classList.add("isactived");
    }
    if(a == 2){
      modal_content.style.height = height;
     // item1.classList.add("isactived");
      item2.classList.remove("isactived-item");
      part_info_2.classList.remove("isactived");
      item3.classList.add("isactived-item");
      part_photo.classList.add("isactived");
      document.getElementById("text-annonce").innerHTML="Ajouter 3 Photos upload et Appuyer sur Botton Envoyer";
    }
   
    
}
function Precedent(a,height){
    if(a == 2){
      modal_content.style.height = height;
      item2.classList.remove("isactived-item");
      part_info_2.classList.remove("isactived");
      item1.classList.add("isactived-item");
      part_info.classList.add("isactived");
    }
    if(a == 3){
     
      modal_content.style.height = height;
      item3.classList.remove("isactived-item");
      part_photo.classList.remove("isactived");
      item2.classList.add("isactived-item");
      part_info_2.classList.add("isactived");
      document.getElementById("text-annonce").innerHTML="Remplir les champs et appuyer sur suivant";
     
    }
}
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