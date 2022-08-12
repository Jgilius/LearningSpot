
 const happy_button_select = document.getElementById("hs").value;
 const unsure_button_select = document.getElementById("us").value;
 const sad_button_select = document.getElementById("ss").value;
 const happy_button_unselect = document.getElementById("hu").value;
 const unsure_button_unselect = document.getElementById("uu").value;
 const sad_button_unselect = document.getElementById("su").value;
 const happy_form = document.getElementById("happy_form").value;
 var counterVal = 0;

 function all_active(){
     hs.disabled = false; 
     us.disabled = false;
     ss.disabled = false; 
}

function disableUnsure(){
    us.disabled = true;
}


function incrementClick() {
    updateDisplay(++counterVal);
}

function resetCounter() {
    counterVal = 0;
    updateDisplay(counterVal);
}


function happy_onclick() {
    incrementClick();

    if(counterVal != 0){
        disableUnsure();
    }
}

// function unsure_onclick(){
//      hs.disabled = true;
//      ss.disabled = true; 
//  }

//  function sad_onclick(){
//      hs.disabled = true;
//      us.disabled = true; 
//  }
