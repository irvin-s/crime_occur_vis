function loadData() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      /* document.getElementById("demo").innerHTML =
                      this.responseText;*/
      var arrMarker = JSON.parse(this.responseText);
      addMarker(arrMarker);
    }
  };
  var month = document.getElementById("ini_month").value;
  var brand = document.getElementById("brand").value;
  xhttp.open(
    "GET",
    "http://api.crimevis.work/getoccur?ini_month=" +
      month +
      "&brand=" +
      brand +
      "",
    true
  );
  xhttp.send();
}

//Adding markers
function addMarker(insMarker) {
  var i;
  for (i = 0; i < insMarker.length; i++) {
    var lat = insMarker[i].latitude;
    var lng = insMarker[i].longitude;
    var marca_celular = insMarker[i].marca_celular;
    var rubrica = insMarker[i].rubrica;
    if (marca_celular == "APPLE") {
      var marker = L.circleMarker([lat, lng], { color: "#ff0000" }).addTo(
        mymap
      );
      marker
        .bindPopup(
          "<b>Marca Celular: " + marca_celular + "</b><br>" + rubrica + ""
        )
        .openPopup();
    } else {
      var marker = L.circleMarker([lat, lng], { color: "#006600" }).addTo(
        mymap
      );
      marker
        .bindPopup(
          "<b>Marca Celular: " + marca_celular + "</b><br>" + rubrica + ""
        )
        .openPopup();
    }
  }
}
