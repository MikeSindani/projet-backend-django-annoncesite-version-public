    // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      const Config = {
        apiKey: "AIzaSyBuwWCDpsLuwcrygf5qGuTkiznBMjFclNA",
        authDomain: "annoncesite-5d608.firebaseapp.com",
        databaseURL: "https://annoncesite-5d608-default-rtdb.firebaseio.com",
        projectId: "annoncesite-5d608",
        storageBucket: "annoncesite-5d608.appspot.com",
        messagingSenderId: "729688890729",
        appId: "1:729688890729:web:30db15c91ef10f9d2e31f8",
        measurementId: "G-E13XZ4TGFL"
      };
      firebase.initializeApp(Config);
      // Get a reference to the storage service, which is used to create references in your storage bucket

          function uploadimage(){

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

        });
      }