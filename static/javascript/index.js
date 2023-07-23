  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      mapId: "c0b1d8ce173615cf",
      center: { lat: 49.08650609057263, lng: 9.612711183128699 },
      zoom: 12,
    });
    // Center at Landgashof Sonne for the two markers
    // 49.08650609057263, 9.612711183128699

    // Location in Mainhardt for the buffet
    const markerLocation1 = new google.maps.Marker({
        position: { lat: 49.080781310008774, lng: 9.555482320505403 },
        map,
        title: "P&J Wedding Buffet"
    });

    // Location in Schwäbisch Hall for the ceremony
    const markerLocation2 = new google.maps.Marker({
      position: { lat:  49.10327521742791, lng: 9.711595577594238 },
      map,
      title: "P&J Wedding Ceremony"
  });
  }