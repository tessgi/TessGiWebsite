$("#sectors").change(function(){
var optionSelected = $("option:selected", this);
    var valueSelected = this.value;
    $(".drn").hide();
    $("#" + valueSelected).show();
})
