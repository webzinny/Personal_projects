console.log("Script exectuing succesfully");
$(document).ready(function(){
    $("#dashboard-btn").click(function(){
        $("#dashboard-btn").addClass("active");
        $("#pushcontents-btn").removeClass("active");
        $("#pushcontents").hide();
        $("#dashboard").show();
    });

    $("#pushcontents-btn").click(function(){
      $("#pushcontents").show();
      $("#dashboard").hide();
        $("#pushcontents-btn").addClass("active");
        $("#dashboard-btn").removeClass("active");
    });

    $("#add-new-card").click(function(){
      console.log("button is working");
      $("#content-upload-form").slideDown(1000);
    });

})
$.ajax({
    url: "adminContent",
    type: "GET",
    datatype: "JSON",
    success: function(content){
      console.log(content)
      $.each(content,function(key,value){
        $("#content-table").append("<tr>"+
          "<td>"+ key+"</td>"+
          "<td>"+ "<img src="+value.img+">"  +"</td>"+
          "<td>"+ value.tag+"</td>"+
          "<td>"+ value.description+"</td>"+
          "<td>"+"<form>"+"<button type="+"submit"+">"+"DELETE"+"</button>"+"</form"+"</td>"
          +"</tr>")
      });
    }
  });
