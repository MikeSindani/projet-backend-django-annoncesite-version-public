
            // Get the modal
            var modal = document.getElementById("myModal");

            // Get the button that opens the modal
            var btn = document.getElementById("btn-modal-annonce");
    
            // Get the <span> element that closes the modal
            var clos = document.getElementsByClassName("close")[0];
    
            // When the user clicks on the button, open the modal
            btn.onclick = function() {
            modal.style.display = "block";
            }
    
            // When the user clicks on <span> (x), close the modal
            clos.onclick = function() {
            modal.style.display = "none";
            }
    
            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "block";
            }
            }
           

            document.body.addEventListener('change', function (e) {
                let target = e.target;
                switch (target.id) {
                    case 'prix-fixe-btn':
                        document.getElementById("prix-interval").style.display = 'none';
                        document.getElementById("autres-moyens").style.display = 'none';
                        document.getElementById("prix-fixe").style.display = 'block';
                        
                        break;
                    case 'prix-interval-btn':
                        
                        document.getElementById("autres-moyens").style.display = 'none';
                        document.getElementById("prix-fixe").style.display = 'none';
                        document.getElementById("prix-interval").style.display = 'block';
                        $("#prix-fixe").val(" ");
                        break;
                    case 'autres-moyens-btn':   
                        document.getElementById("prix-fixe").style.display = 'none';
                        document.getElementById("prix-interval").style.display = 'none';
                        document.getElementById("autres-moyens").style.display = 'block';
                        break;
                }
                
            });
            /*
            Suivant1.document.getElementById("btn_suivant_1");
            Suivant1.onclick = function(){
            titre =                 if(email != '' && password !='' && confirmpassword != ''){

            }*/

           