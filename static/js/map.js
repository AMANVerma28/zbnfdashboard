
$( document ).ready(  function(){


google.charts.load('current', {'packages':['corechart']});
     google.charts.setOnLoadCallback(hi);

    
      
});
  function drawChart(data) {

        var data = google.visualization.arrayToDataTable(data);

        var options = {
           width: 400,
            height: 240,  
          title: 'area percentage of crops',
           is3D: true,
              
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
google.visualization.events.addListener(chart, 'click', function () {
    chart.clearChart()
});
google.visualization.events.addListener(chart, 'ready', function () {
  
});
        chart.draw(data, options);
}
  function getLocation() {
    if (navigator.geolocation) {
   
        navigator.geolocation.getCurrentPosition(setMap());
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function makeTableHTML(myArray,array) {
    var result = "<table class='table'>";
    result += "<thead><tr><th>Crop</th><th>Yield</th></tr></thead><tbody>";

    for(var i=0; i<myArray.length; i++) {
        result += "<tr>";
            result += "<td>"+myArray[i]+"</td>";
        result += "<td>"+array[i]+"</td>";
        result += "</tr>";
    }
    result += "</tbody></table>";

    return result;
}
function hello(farm,households){

 $.getJSON( "../../static/json/members.json", function( data ) {
  for(row in data)
  {

    if(data[row].HouseHold==households && data[row].Relation=="head")
     {

 var owner=data[row].Name
} 
  }

  $.getJSON( "../../static/json/crops.json", function( data ) {
    var crop=[]
    var yield=[]
  for(row in data)
  {

    if(data[row].Farm==farm.id && data[row].Season==document. getElementById("season").value &&data[row].DateTime.substring(4,-1)==document.getElementById("value").innerHTML)
    { crop.push(data[row].Crop )
yield.push(data[row].Yield)
    }}
  
  document.getElementById('farmdetails').innerHTML="<p><b>owner</b> : "+owner+"</p><br><p><b>Totalarea </b>: "+farm.TotalArea+" hectors</p><br>"+makeTableHTML(crop,yield)
});
 });



}
function hi(farm){

if(farm)
  { 
    $('#myModal').modal();


    $.getJSON( "../../static/json/crops.json", function( data ) {
      var piedata=[["crop","extent"]]
    for (row in data)
    {

var temp=[]
      if(data[row].Farm==farm &&data[row].Season==document. getElementById("season").value &&data[row].DateTime.substring(4,-1)==document. getElementById("value").innerHTML )
      {

        temp.push(data[row].Crop)
        temp.push(data[row].Extent)
          piedata.push(temp)
      }  
    
     
  }
  drawChart(piedata)
  

  
});}

}

function setMap(position) {

var myCenter = new google.maps.LatLng(16.002730,81.072235);
var mapCanvas = document.getElementById("map");
var mapOptions = {center: myCenter, zoom: 14, mapTypeId: 'terrain'};
var map = new google.maps.Map(mapCanvas, mapOptions);
var srcImage = 'https://developers.google.com/maps/documentation/' +
      'javascript/examples/full/images/talkeetna.png';

  // The custom USGSOverlay object contains the USGS image,
  // the bounds of the image, and a reference to the map.

var infowindow = new google.maps.InfoWindow();
$.getJSON( "../../static/json/households.json", function( data ) {


  var marker
  var house_icon = {
    url:"../../static/img/house.png", 
    scaledSize: new google.maps.Size(30, 30), 
    origin: new google.maps.Point(0,0), 
    anchor: new google.maps.Point(0, 0)
};
for (row in data)
{ 
  marker = new google.maps.Marker({
        position: new google.maps.LatLng(data[row].Location.coordinates[1], data[row].Location.coordinates[0]),
        icon:house_icon,
         
      });
 google.maps.event.addListener(marker, 'mouseover', (function(marker, row) {
  
        return function() {

          infowindow.setContent("<b>members : </b>"+data[row]. Number_of_members+ "<br><br>"+"<b>income :</b> "+data[row].Monthly_income+ "");
          infowindow.open(map, marker);
        }
      })(marker, row));
  marker.setMap(map);
}
});

$.getJSON( "../../static/json/wells.json", function( data ) {
  var marker
  var well_icon = {
    url:"../../static/img/well.png", // url
    scaledSize: new google.maps.Size(30, 30), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
};
for (row in data)
{

  marker = new google.maps.Marker({
        position: new google.maps.LatLng(data[row].Location.coordinates[1], data[row].Location.coordinates[0]),
        map: map,
        icon:well_icon,
         
      });
 google.maps.event.addListener(marker, 'mouseover', (function(marker,row) {
        return function() {
          infowindow.setContent("<b>Depth : </b>"+data[row].Depth+"<br> <br>"+" <b>Yield :</b> "+ data[row].Average_yield);
          infowindow.open(map, marker);
        }
      })(marker, row));
  marker.setMap(map);
}
});
$.getJSON( "../../static/json/farms.json", function( data ) {
  
 
for (row in data)
{ 
  var path=[]
for (rows in data[row].Location.coordinates[0])  
 {
path.push(new google.maps.LatLng(data[row].Location.coordinates[0][rows][1],data[row].Location.coordinates[0][rows][0]))

 }

  var flightPath = new google.maps.Polygon({
    path: path,
    strokeColor: "green",
    strokeOpacity: 1,
    strokeWeight: 2,
    fillColor: "green",
    fillOpacity: 0.4,
   
  });   

  flightPath.setMap(map);
  google.maps.event.addListener(flightPath, 'click', (function(marker,row) {
        return function() {
          hi(data[row].id)
          hello(data[row],data[row].HouseHold)
        }
      })(flightPath, row));

}
});

}
