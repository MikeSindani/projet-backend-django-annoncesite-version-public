 // get the number step 
 const item1 = document.querySelector(".item1");
 const item2 = document.querySelector(".item2");
 const item3 = document.querySelector(".item3");
 const item4 = document.getElementById("item4");
 // get the div step button
 const part_pass = document.querySelector(".pass");
 const part_personnel = document.querySelector(".personnel_info"); 
 const part_contact = document.querySelector(".contact_info");
const profil_info = document.querySelector(".profil_info");  
const body_second = document.querySelector(".body-second");
 const from_main = document.querySelector(".form-main "); 
 // create function top change de step 
function Suivant(a){
     if(a == 1){
       from_main.classList.add("form-main-2")
       body_second.classList.add("body-second-2")
       item1.classList.add("isactived");
       part_pass.classList.remove("isactived");
       item2.classList.add("isactived");
       part_personnel.classList.add("isactived");
       // message a transmettre 
       var message = document.getElementById("message").innerHTML='';
     }
     if(a == 2){
      
       item1.classList.add("isactived");
       item2.classList.add("isactived");
       part_personnel.classList.remove("isactived");
       item3.classList.add("isactived");
       part_contact.classList.add("isactived");
     }
     if(a == 3){
       item1.classList.add("isactived");
       item2.classList.add("isactived");
       item3.classList.add("isactived");
       part_contact.classList.remove("isactived");
       item4.classList.add("isactived");
       profil_info.classList.add("isactived");
     }
}
function Precedent(a,height){
     if(a == 2){
       item2.classList.remove("isactived");
       part_personnel.classList.remove("isactived");
       item1.classList.add("isactived");
       part_pass.classList.add("isactived");
     }
     if(a == 3){
       item3.classList.remove("isactived");
       part_contact.classList.remove("isactived");
       item1.classList.add("isactived");
       item2.classList.add("isactived");
       part_personnel.classList.add("isactived");
      
     }
     if(a == 4){
       item4.classList.remove("isactived");
       profil_info.classList.remove("isactived");
       item1.classList.add("isactived");
       item2.classList.add("isactived");
       item3.classList.add("isactived");
       part_contact.classList.add("isactived");
      
     }
}
 
function check(){
// get the value for form password 
 var password = document.forms["myForm"]["password"].value;
 var confirmpassword = document.forms["myForm"]["confirm_password"].value;
 var email = document.forms["myForm"]["email"].value;
 var suivant_part_pass = document.getElementById("suivant_part_pass");

 if(email != '' && password !='' && confirmpassword != ''){
   if(password.length < 8){
       var message = document.getElementById("message").innerHTML='<span style="color:red;"><i class="fa fa-circle-exclamation"></i>Mot de passe doit etre superieur a 8</span>.';
       }else{
           var message = document.getElementById("message").innerHTML="";
           if(password == confirmpassword){
               var message = document.getElementById("message").innerHTML='<span style="color:green;"><i class="fa fa-triangle-exclamation"></i>Ca Correspondre!</span>';
               suivant_part_pass.disabled = false;
           }else{
               var message = document.getElementById("message").innerHTML='<span style="color:rgb(134, 43, 43);"><i class="fa fa-circle-exclamation"></i>Doit Correspondre!</span>';
               suivant_part_pass.disabled = true;
           }
     }   
  }
}

function img_profil(event){
           if (event.target.files.length > 0) { 
           var src = URL.createObjectURL(event.target.files[O]) ;  
           var preview = document.getEIementById("img_profil") ; 
           preview. src = src;
           preview.style.display = "block";
         }
   }
  