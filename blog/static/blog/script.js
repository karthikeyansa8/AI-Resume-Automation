var sidenav = document.querySelector(".side-navbar");

function shownavbar() {
    sidenav.style.left = "0";

}

function closenavbar() {
    sidenav.style.left = "-60%";
}

function showalert(){
    alert("Successfully Submitted!");
}


// collection

var productcontainer = document.getElementById("product")
var search = document.getElementById("search")
var productlist = productcontainer.querySelectorAll("div")

search.addEventListener("keyup", function () {
    var searchvalue = event.target.value.toUpperCase()

    for (i = 0; i < productlist.length; i++) {

        var productname = productlist[i].querySelector("p").textContent

        if (productname.toUpperCase().indexOf(searchvalue) < 0) {
            productlist[i].style.display = "none"
        } else {
            productlist[i].style.display = "block"
        }
    }
})