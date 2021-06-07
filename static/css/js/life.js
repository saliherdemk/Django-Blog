document.getElementById('child').style.opacity = "0";
document.getElementById('chess').style.opacity = "0";

function rangeSlider(value){

    if (value > 18){
        document.getElementById('range').value = 18;
        value = 18;
    }
    document.getElementById('rangevalue').innerHTML = value;
    document.getElementById('fillrangevalue').style.width = +value + "%";
    
    document.getElementById('baby').style.opacity = + (value * 10) + "%";

    document.getElementById('baby2').style.opacity = + (value * 7) + "%";

    document.getElementById('child').style.opacity = + (value * 5) + "%";

    document.getElementById('read').style.opacity = + (value * 3) + "%";

    document.getElementById('chess').style.opacity = + (value * 0.9 ) + "%";

    document.getElementById('comp').style.opacity = + (value * 0.3) + "%";

}
