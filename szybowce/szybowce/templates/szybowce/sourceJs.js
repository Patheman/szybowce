 var marker1, marker2;
      var poly, geodesicPoly;
    var markers = [];
    var polyTable = [];
    var tableOfPaths= [];
    var distanceBetweenPoints = [];
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
       var labelIndex = 0;
 

      function initMap() {

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 6,
          center: {lat: 52, lng: 19 }
        });

   
            document.getElementById('submit').addEventListener('click', function() {
              console.log("jestem");
              var geocoder = new google.maps.Geocoder();
            geocodeAddress(geocoder, map);
            
        });

         map.controls[google.maps.ControlPosition.TOP_CENTER].push(
            document.getElementById('info'));

       map.addListener('click', function(e) {
        placeMarkerAndPanTo(e.latLng, map);
       tableOfPaths.push(createNewPath(map));
        });


         marker1 = new google.maps.Marker({
          map: map,
          draggable: true,
          position: {lat: 52.41, lng: 16.92}
        });

        marker2 = new google.maps.Marker({
          map: map,
          draggable: true,
          position: {lat: 52.2340, lng: 21.0287}
        });
           
        var bounds = new google.maps.LatLngBounds(
            marker1.getPosition(), marker2.getPosition());
        map.fitBounds(bounds);

        google.maps.event.addListener(marker1, 'position_changed', update);
        google.maps.event.addListener(marker2, 'position_changed', update);

        poly = new google.maps.Polyline({
          strokeColor: '#FF0000',
          strokeOpacity: 1.0,
          strokeWeight: 3,
          map: map,
        });

        geodesicPoly = new google.maps.Polyline({   strokeColor: '#CC0099',
        strokeOpacity: 1.0,   strokeWeight: 3,   geodesic: true,   map: map
        });

        polyTable[0] = new google.maps.Polyline({
          strokeColor: '#FF0000',
          strokeOpacity: 1.0,
          strokeWeight: 3,
          map: map,
        });

        geodesicPoly2 = new google.maps.Polyline({
          strokeColor: '#CC0099',
          strokeOpacity: 1.0,
          strokeWeight: 3,
          geodesic: true,
          map: map
        });
     
       

       update();
      }
         function createNewPath(map){

          polyPath = new google.maps.Polyline({
            strokeColor: '#FF0000',
          strokeOpacity: 1.0,
          strokeWeight: 3,
            map : map,
        });
          return polyPath;
         }


        function placeMarkerAndPanTo(latLng, map) {
          var marker = new google.maps.Marker({
          position: latLng,
          map: map,
          draggable: true,
          label: labels[labelIndex++ % labels.length]
        });
        markers.push(marker);

  
      //  var dummy = '<span>Dystans:'+labelIndex +' <input type="text"><small>(ft)</small></span>\r\n';
    //document.getElementById('floating-panel').innerHTML += dummy;    

         google.maps.event.addListener(marker, 'position_changed', update);
         google.maps.event.addListener(map,'click', update);
      
         addElement(markers.length,marker);
       }

        function addPoint(marker){
        markers.push(marker);
    google.maps.event.addListener(marker, 'position_changed', update);
    google.maps.event.addListener(map,'mouseover', update);
    addElement(markers.length,marker);
        }


        function distance(point1,point2,i){

          var distance = google.maps.geometry.spherical.computeDistanceBetween(point1, point2)/ 1000;
          distanceBetweenPoints[i]= Round(distance,2);
          return distance;
        }

        function geocodeAddress(geocoder, resultsMap) {
        var address = document.getElementById('address').value;

        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);

             var marker = new google.maps.Marker({
              map: resultsMap,
              position: results[0].geometry.location,
               draggable: true,
              label: labels[labelIndex++ % labels.length]
            });
      //console.log(results[0].geometry.location);
           // placeMarkerAndPanTo(results[0].geometry.location,resultsMap);
            //tableOfPaths.push(createNewPath(resultsMap));
            addPoint(marker);
            tableOfPaths.push(createNewPath(resultsMap));
          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }

        });

    }



    function addElement(number,marker) {
      var z = document.createElement("div");
    z.id=number;
    var x = document.createElement("INPUT");
    var y = document.createElement("INPUT");
    x.id="pozycja"+number;
    y.id="odleglosc"+number;
    var para = document.createElement("P");
    var t = document.createTextNode("Punkt " +number);
    para.appendChild(t);
    x.setAttribute("type", "text");
    x.setAttribute("value", "Hello World!");

    document.getElementById('floating-panel').appendChild(z);
  document.getElementById(number).appendChild(para);
    document.getElementById(number).appendChild(x);
    document.getElementById(number).appendChild(y);

    //document.getElementById('floating-panel').appendChild(para);
  //  document.getElementById('floating-panel').appendChild(x);
    //document.getElementById('floating-panel').appendChild(y);


    document.getElementById('pozycja'+number).value= Round(marker.position.lat(), 2) + " "+Round(marker.position.lng(), 2)  ;
}

function Round(n, k)
{
    var factor = Math.pow(10, k);
    return Math.round(n*factor)/factor;
}

      function update() {
        var paths = []; 
        var path = [marker1.getPosition(), marker2.getPosition()];
        if(markers!=""){
        var lat = markers[0].getPosition();
      console.log("Pozycja pierwszego " +lat);

   
      for(var i = 1;i<markers.length;i++){
        console.log("Pozycja pierwszego " +i);
        paths[i]=[markers[i-1].getPosition(),markers[i].getPosition()];
        tableOfPaths[i].setPath(paths[i]);
        distance(markers[i-1].getPosition(),markers[i].getPosition(),i);
        document.getElementById('odleglosc'+i).value=distanceBetweenPoints[i];
        
      }

    }
        poly.setPath(path);
        geodesicPoly.setPath(path);
        var heading = google.maps.geometry.spherical.computeHeading(path[0], path[1]);

        var distanses = google.maps.geometry.spherical.computeDistanceBetween(path[0], path[1])/ 1000;

        document.getElementById('heading').value = heading;
        document.getElementById('origin').value = path[0].toString();
        document.getElementById('destination').value = path[1].toString();

        

        console.log(distanses);
         console.log(markers.length);
          console.log("update");


      }