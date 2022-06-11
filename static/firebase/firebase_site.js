      
      // Get a reference to the storage service, which is used to create references in your storage bucket
         
          function uploadimage(){
            progressBar(0);
             // Your web app's Firebase configuration
            // For Firebase JS SDK v7.20.0 and later, measurementId is optional
            const Config = {
              apiKey: "AIzaSyB8EzstENagg8-JjE-C90sdowpd58AInN8",
              authDomain: "appmemoire-a5a2a.firebaseapp.com",
              databaseURL: "https://appmemoire-a5a2a-default-rtdb.firebaseio.com",
              projectId: "appmemoire-a5a2a",
              storageBucket: "appmemoire-a5a2a.appspot.com",
              messagingSenderId: "86048778948",
              appId: "1:86048778948:web:12646f497c766ed9f5b791"
            };
            firebase.initializeApp(Config);
            progressBar(25);

              var storage = firebase.storage();

              var file = document.getElementById("files").files[0];

              var storageRef = storage.ref();

              var thisref = storageRef.child("profils").child(file.name).put(file);

              thisref.on('state_changed',function(snapshot){

              console.log("file uplaoded succesfully");
            progressBar(50);
          },
          function(error) {

          },

          function() {
          // Upload completed successfully, now we can get the download URL
          var downloadURL = thisref.snapshot.downloadURL;
          console.log("got url");
          progressBar(75);
          document.getElementById("url").value = downloadURL;
          console.log("file uploaded successfully");
          progressBar(100);
          document.getElementById("message").innerHTML='<span style="color:green;"></i>Photo de Profil Envoyer</span>'
          // activation du bouton quand c'est upload
          document.getElementById("loginBtn").disabled = false;
          
          
             
        });
      }
      // fonctioon qui gerer la progression du transfert 
      function  progressBar(value){
        if(value == 0){
        document.querySelector(".per-0").style.display="none";
        document.querySelector(".per-0").style.display="block";
        }
        if(value == 25){
          document.querySelector(".per-25").style.display="none";
          document.querySelector(".per-0").style.display="none";
          document.querySelector(".per-25").style.display="block";
        }
        if(value == 50){
         document.querySelector(".per-50").style.display="none";
         document.querySelector(".per-25").style.display="none";
         document.querySelector(".per-50").style.display="block";
        }
        if(value == 75){
          document.querySelector(".per-75").style.display="none";
          document.querySelector(".per-50").style.display="none";
          document.querySelector(".per-75").style.display="block";
        }
        if(value == 100){
          document.querySelector(".per-75").style.display="none";
          document.querySelector(".per-75").style.display="none";
          document.querySelector(".per-100").style.display="block";
        }
      }