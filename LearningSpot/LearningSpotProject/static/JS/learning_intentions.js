
//  const happy_button_select = document.querySelector(".hs").value;
//  const unsure_button_select = document.querySelector(".us").value;
//  const sad_button_select = document.querySelector(".ss").value;
//  const happy_button_unselect = document.querySelector(".hu").value;
//  const unsure_button_unselect = document.querySelector(".uu").value;
//  const sad_button_unselect = document.querySelector(".su").value;


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
