$(document).ready(function(){
    console.log("Document ready");   
    const settings = {
      "async": true,
      "crossDomain": true,
      "url": "https://api.nal.usda.gov/fdc/v1/foods/list?api_key=",
      "method": "GET",
      
    };
    
    $.ajax(settings).done(function (response) {
      console.log(response)

      Object.keys(response).forEach(k => {
        console.log(k, ':', response[k].foodNutrients)
      })

    });

  });
