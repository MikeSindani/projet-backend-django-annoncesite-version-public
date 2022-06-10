      
      // Get a reference to the storage service, which is used to create references in your storage bucket
         
          function uploadimage(){
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

              var storage = firebase.storage();

              var file = document.getElementById("files").files[0];

              var storageRef = storage.ref();

              var thisref = storageRef.child(file.name).put(file);

              thisref.on('state_changed',function(snapshot){

              console.log("file uplaoded succesfully");

          },
          function(error) {

          },

          function() {
          // Upload completed successfully, now we can get the download URL
          var downloadURL = thisref.snapshot.downloadURL;
          console.log("got url");
          document.getElementById("url").value = downloadURL;
          console.log("file uploaded successfully");
          var btnLogin = document.getElementById("loginBtn").disabled = false;
          document.getElementById("message").innerHTML=""     
        });
      }