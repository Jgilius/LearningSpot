
 const happy_button_select = document.getElementById("hs").value;
 const unsure_button_select = document.getElementById("us").value;
 const sad_button_select = document.getElementById("ss").value;
 const happy_button_unselect = document.getElementById("hu").value;
 const unsure_button_unselect = document.getElementById("uu").value;
 const sad_button_unselect = document.getElementById("su").value;
 const happy_form = document.getElementById("happy_form").value;

 let happy_clicked;

 function all_active(){
     hs.disabled = false; 
     us.disabled = false;
     ss.disabled = false; 
 }


 function happy_onclick(){

        us.disabled = true;
        ss.disabled = true;
 }

 function unsure_onclick(){
     hs.disabled = true;
     ss.disabled = true; 
 }

 function sad_onclick(){
     hs.disabled = true;
     us.disabled = true; 
 }
