// ---------- SIGNALER MODAL FORM ON CHANGE ---------------
 
var select = document.querySelector('#signaler-form');
var textarea = document.querySelector('#textarea');
select.addEventListener('change', function () {
    console.log(this.value)
            if(this.value=="Autres"){
                textarea.style.display = block;
            }else{
                textarea.style.display = none;
            }
});
// ----------- SECTION  --------------------
function change_section(number){
    if (number==1){
        $(".part_info").css("display","block");
        $(".part_info_2").css("display","none");
        $(".part_info_3").css("display","none");
        $("#item1").css("color","black");
        $("#item2").css("color","gray");
        $("#item3").css("color","gray");
    }
    if (number==2){
        $(".part_info").css("display","none");
        $(".part_info_2").css("display","block");
        $(".part_info_3").css("display","none");
        $("#item2").css("color","black");
        $("#item1").css("color","gray");
        $("#item3").css("color","gray");
       
    }
    if (number==3){
        $(".part_info").css("display","none");
        $(".part_info_2").css("display","none");
        $(".part_info_3").css("display","block");
        $("#item3").css("color","black");
        $("#item1").css("color","gray");
        $("#item2").css("color","gray");
    }
}

// ----------- MODAL CONTACTER-------------------
     // Get the modal
var modalContacter = document.getElementById("modal-contacter");

// Get the button that opens the modal
function btn_modal_contacter() {
modalContacter.style.display = "block";
}

// Get the <span> element that closes the modal
function close_contacter() {
modalContacter.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modalContacter) {
    modalContacter.style.display = "none";
}
}
// ----------- MODAL MESSAGE-------------------
     // Get the modal
var modalmessage = document.getElementById("modal-messsage");

// Get the button that opens the modal
function btn_modal_message() {
modalmessage.style.display = "block";
}

// Get the <span> element that closes the modal
function close_message() {
modalmessage.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modalmessage) {
    modalmessage.style.display = "none";
}
}
/* ----------- MODAL EVALUATION -------------------*/
 /*Get the modal*/
 var modalevaluatiion = document.querySelector("#myModal");

/* Get the button that opens the modal*/
function btn_modal_evaluation() {
    modalevaluatiion.style.display = "block";
}

 /*Get the <span> element that closes the modal*/
function close_evaluation() {
modalevaluatiion.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modalevaluatiion) {
    modalevaluatiion.style.display = "none";
}
}

// ------------------- Ajax -------------------------------
$(document).on('submit', '#evaluation-form', function(e){
e.preventDefault()
e.preventDefault();
var evaluation = document.querySelector('input[name="evaluation"]:checked').id;
console.log(evaluation);

//name = $('#fiable').val()
//name = $('#nofiable').val()
idannonce = $("#uidannonce").attr("data-uidannonce");
uid = $("#uid").attr("data-uid");
console.log(evaluation);
console.log(uidannonce);
console.log(uid);
$.ajax({
type: 'POST',
url: "{% url 'evaluation' %}",
data: {
    evaluation: evaluation,
    uidannonce: uidannonce,
    uid: uid,
    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
},
success: function(data) {
    alert(data);
    modalevaluatiion.style.display = "none";
},
})
   
});

$(document).on('submit', '#evaluation-form', function(e){
e.preventDefault()
e.preventDefault();
var evaluation = document.querySelector('input[name="evaluation"]:checked').id;
console.log(evaluation);

//name = $('#fiable').val()
//name = $('#nofiable').val()
uidannonce = $("#uidannonce").attr("data-uidannonce");
uid = $("#uid").attr("data-uid");
console.log(evaluation);
console.log(uidannonce);
console.log(uid);
$.ajax({
type: 'POST',
url: "{% url 'evaluation' %}",
data: {
    evaluation: evaluation,
    uidannonce: uidannonce,
    uid: uid,
    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
},
success: function(data) {
    alert(data);
    modalevaluatiion.style.display = "none";
},
})
   
});
// 

// ----------- MODAL SiGNALER-------------------
    // Get the modal
    var modalSignaler = document.getElementById("modal-signaler");

// Get the button that opens the modal
function btn_modal_signaler() {
    modalSignaler.style.display = "block";
}

// Get the <span> element that closes the modal
function close_signaler() {
    modalSignaler.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
if (event.target == modalSignaler) {
    modalSignaler.style.display = "none";
}}

$("#btn_message_fermer").click(function (){
   $(".message").css("display","none");
  });